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

@tasks.loop(minutes=3)
async def loop():
    csv_file = open('vocab.csv', 'r')
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    
    # get list of subscribers
    users = []
    with open('users.txt', 'r') as f:
        c = f.read()
        if c.strip() == "":
            users = []
        else:
            users = [int(s) for s in c.split(';')]
    
    for user_id in users:
        # pick game mode
        game_mode = random.choice(list(GameMode))
        # pick a random line, excluding the header
        line = random.choice(list(csv_reader)[1:])

        if game_mode == GameMode.GUESS_TONE:
            user = await bot.fetch_user(user_id)
            await user.send(f"Guess the tone of the following word: {line[0]}") 
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
            await user.send(f"1. {options[0]}     2. {options[1]}     3. {options[2]}")
            await user.send("Button", view=MyView())

class MyView(discord.ui.View):
    @discord.ui.button(label="Button 1", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!")

    @discord.ui.button(label="Button 2", row=1, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!")


@bot.event
async def on_ready():
    print("走吧")
    loop.start()

bot.run(BOTTOKEN)