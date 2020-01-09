import discord
import json
from discord.ext import commands

# client = discord.Client()
TOKEN = 'NjY0MjU2ODY4NTQ1NDYyMzAz.XhbQAQ.fS5lpcKJeh2pwXKcpXaZUe_qRT0'

client = commands.Bot(command_prefix='-')


# welcome stranger i will be your guild in this world, i am your god
# first off choose a name
# now choose a race your options are ect
# lastly choose a class, options are ect
# fighting will be turn based story scenarios
# each race will have a special skill


class playerCharacter:
    def __init__(self, name, class_is, race, level):
        self.name = name
        self.class_is = class_is
        self.race = race
        self.level = level

    # def create_player(self, player_input):
    #     self.name = player_input
    #     self.class_is = player_input
    #     self.race = player_input


class playerClass:
    def __init__(self, attack, defense, craft, magic):
        self.attack = attack
        self.defense = defense
        self.craft = craft
        self.magic = magic

    name = 'un-named please choose a name'
    class_is = 'no class'
    race = 'no race'



    data = {
        'name': name,
        'class': class_is,
        'race': race
    }
    player = {
        'player_info': data
    }
    warrior = {
        'attack': 10,
        'defense': 5,
        'craft': 0,
        'magic': 0
    }
    thief = {
        'attack': 0,
        'defense': 0,
        'craft': 10,
        'magic': 5
    }


@client.event
async def on_message(message):
    channel = message.channel
    mc = message.content
    pc = playerClass
    if pc.data.get('class') == 'no class':
        if mc.startswith('-class'):
            await channel.send('choose class:\nwarrior\nthief')

            def check(m):
                return m.content == 'warrior' or \
                       m.content == 'thief' and m.channel == channel

            msg = await client.wait_for('message', check=check)
            await channel.send('chosen {.content} class!'.format(msg))
            a = msg.content
            pc.data['class'] = a
            print(pc.data)
    # if pc.data.get('class') == 'warrior':
    #     await channel.send("class has all ready been set")
    if mc.startswith('-name'):
        await channel.send('choose name:')
        msg = await client.wait_for('message')
        await channel.send('hello {.content}!'.format(msg))
        a = msg.content
        pc.data['id'] = msg.author.id
        pc.data['name'] = a
        print(pc.player)

    if mc.startswith('-get class'):
        await channel.send(pc.data.get('class'))
    if mc.startswith('-get race'):
        await channel.send(pc.data.get('race'))
    if mc.startswith('-get name'):
        await channel.send(pc.data.get('name'))
    if mc.startswith('-stats'):
        if pc.data.get('class') == 'warrior':
            await channel.send(pc.warrior)
        if pc.data.get('class') == 'thief':
            await channel.send(pc.thief)
        if pc.data.get('class') == 'no class':
            await channel.send("need to pick a class to get stats")

    with open('data.txt', 'w') as outfile:
        json.dump(pc.player, outfile)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
