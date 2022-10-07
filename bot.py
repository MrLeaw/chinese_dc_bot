import discord
from discord.ext import commands, tasks
import os
import csv
import random
from cmds import register_commands
from command_list import register_commands2
from dotenv import load_dotenv
from enum import Enum

class GameMode(Enum):
    GUESS_TONE = 1



load_dotenv()

BOTTOKEN = os.getenv('BOTTOKEN')

bot = commands.Bot()

register_commands(bot)
register_commands2(bot)

async def send_all():
    # get list of subscribers
    users = []
    with open('users.txt', 'r') as f:
        c = f.read()
        if c.strip() == "":
            users = []
        else:
            users = [int(s) for s in c.split(';')]
    
    for user_id in users:
        await send(user_id)

async def send(user_id):
    csv_file = open('vocab.csv', 'r')
    csv_reader = csv.reader(csv_file, delimiter='|')
    # pick game mode
    game_mode = random.choice(list(GameMode))
    # pick a random line, excluding the header
    line = random.choice(list(csv_reader)[1:])

    if game_mode == GameMode.GUESS_TONE:
        user = await bot.fetch_user(user_id)
        correct_tone = line[1]
        # generate two incorrect tones by replacing the correct tone with a random tone
        # i.e. replace the "ˇ", "ˋ", "ˊ", "˙" with a random tone
        options = [correct_tone]
        for i in range(2):
            # if there is no tone marker in the correct tone, then just add a random tone marker
            incorrect_tone = correct_tone
            if [c for c in correct_tone if c in "ˇˋˊ˙"] == []:
                incorrect_tone = incorrect_tone + random.choice("ˇˋˊ˙")
            while incorrect_tone == correct_tone and incorrect_tone in options:
                incorrect_tone = correct_tone.replace(random.choice(["ˇ", "ˋ", "ˊ", "˙"]), random.choice(["ˇ", "ˋ", "ˊ", "˙"]))
            options.append(incorrect_tone)
        # send the three options to the user in a random order
        random.shuffle(options)
        await user.send(f"Guess the tone of the following word: {line[0]}", view=MyView(options, correct_tone))


class MyView(discord.ui.View):
    options = []
    
    # initializer with text for all three buttons
    def __init__(self, options, correct):
        super().__init__()
        self.options = options
        self.correct = correct

        for i in range(3):
            btn = discord.ui.Button(label=options[i], custom_id=str(i))
            btn.callback = self.callback
            self.add_item(btn)
       
    async def callback(self, interaction: discord.Interaction):
        # tell the user if they got it right or wrong
        if self.options[int(interaction.data['custom_id'])] == self.correct:
            await interaction.response.send_message("Correct!")
        else:
            await interaction.response.send_message("Incorrect! The correct answer is " + self.correct)
        
        # stop the buttons from showing up
        self.stop()
        await send(interaction.user.id)
        


@bot.event
async def on_ready():
    print("走吧")
    await send_all()

bot.run(BOTTOKEN)