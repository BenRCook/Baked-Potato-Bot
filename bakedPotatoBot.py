# bot.py
import os
import random
import string
import asyncio

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


class Potato:
    def __init__(self):
        self.adviceList = [
            ["Wash your hands and stay indoors.", "Only go to grocery stores."],
            ["Keep some distance, Make some space.", "Remember not to touch your face."],
            ["Do be good. Don\'t be bad.", "Do be happy. Don\'t be sad."],
            ["Do be early. Don\'t be late.", "Allways eat what\'s on your plate."],   
        ]
        self.newVerse = True
        self.currentVerse = None

    def getResponse(self):
        if self.newVerse == True:
            self.currentVerse = random.choice(self.adviceList)
            self.newVerse = False
            return self.currentVerse[0]
        else:
            self.newVerse = True
            return self.currentVerse[1]

class Antitato(Potato):
    def __init__(self):
        super().__init__()
        self.adviceList = [
            ["Leave your hands, Don\'t stay indoors.", "Go to many different stores."],
            ["Keep no distance. Make no space.", "Remember you must touch your face."],
            ["Don\'t be good, Do be bad.", "Don\'t be happy. Do be sad."],
            ["Don\'t be early. Do be late.", "Never eat what\'s on your plate."]
        ]


class Contradictato(Potato):
    def __init__(self):
        super().__init__()
        self.adviceList = [
            ["Wash your hands and stay indoors.", "Leave your hands, Don\'t stay indoors."],
            ["Only go to grocery stores.", "Go to many different stores."],
            ["Keep some distance, Make some space.", "Keep no distance. Make no space"],
            ["Remember not to touch your face.", "Remember you must touch your face."],
            ["Do be good. Don\'t be bad.", "Don\'t be good, Do be bad."],
            ["Do be happy. Don\'t be sad.", "Don\'t be happy. Do be sad."],
            ["Do be early. Don\'t be late.", "Don\'t be early. Do be late."],
            ["Allways eat what\'s on your plate.", "Never eat what\'s on your plate."]      
        ]

    


potato = Potato()
antitato = Antitato()
contradictato = Contradictato()

@client.event # this is called a decorator
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 
    global potato, antitato

    if message.content == "!help":
        print(str(message.author) + ": !help")
        response = ""
        response += "!help - Gives a list of options\n"
        response += "!potato - Gives a conventional potato response\n"
        response += "!antitato - Gives a reverse potato response\n"
        response += "!contradictato - Gives a conventional potato response, followed by the corresponding reverse potato response\n"
        response += "!spell - Reminds you how to spell \"baked potato\" \n"
        response += "!misspell - Reminds you how to spell somthing vaguely simmilar to \"baked potato \""
        response += "!link - Sends the link to the video"
        await message.channel.send(response)
    elif message.content == "!potato":
        print(str(message.author) + ": !potato")
        await message.channel.send(potato.getResponse())
    elif message.content == "!antitato":
        print(str(message.author) + ": !antitato")
        await message.channel.send(antitato.getResponse())
    elif message.content == "!contradictato":
        print(str(message.author) + ": !contradictato")
        await message.channel.send(contradictato.getResponse()) 
    elif message.content == "!spell":
        print(str(message.author) + ": !spell")
        await letter_by_letter(message.channel, "BAKEDPOTATO")
        await message.channel.send("Baked Potato")
    elif message.content == "!misspell":
        print(str(message.author) + ": !misspell")
        alphabet = [f"**{letter}**" for letter in string.ascii_uppercase]
        potato_letters = ["**B**", "**A**", "**K**", "**E**", "**D**", "**P**", "**O**", "**T**", "**A**", "**T**", "**O**"]
        count = 0
        response = []
        while count < len(potato_letters) :
            rand = random.randint(0,10)
            if (rand == 4):
                letter = random.choice(alphabet)
                response += [letter]
                # await message.channel.send(potato_letters)
            elif rand == 3:
                count += 1
            else:
                letter = potato_letters[count]
                response += [letter]
                # await message.channel.send(potato_letters)
                count += 1
        await letter_by_letter(message.channel, response)
        await message.channel.send("".join(response).replace("*", "").title())
    elif message.content == "!link":
        print(str(message.author) + ": !link")
        await message.channel.send("https://www.youtube.com/watch?v=yYOkgCkxj9I")


async def letter_by_letter(channel, content):
    message = await channel.send(content[0])
    for letter in content[1:]:
        await asyncio.sleep(0.8)
        await message.edit(content=message.content + " " + letter)
    return message
    


        
# print("Your token is: ", TOKEN)
client.run(TOKEN)