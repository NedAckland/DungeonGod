import discord

from discord.ext import commands

# client = discord.Client()
TOKEN = 'NjY0MjU2ODY4NTQ1NDYyMzAz.XhUd2w.Nl_cjts2BNRmbtTm3-1AUGBXx1U'

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

    def is_warrior(self, player_input):
        self.attack = 10
        self.defense = 5
        self.craft = 0
        self.magic = 0

    def is_thief(self):
        self.attack = 0
        self.defense = 5
        self.craft = 10
        self.magic = 0

    def set_class(self, player_input):
        if player_input == 'warrior':
            self.is_warrior(self)
        elif player_input == 'thief':
            self.is_thief()
        else:
            print("invalid input")


def set_name(message):
    pass


def print_stats(player_input):
    if player_input == "stats":
        stats = playerCharacter
        return stats


@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('-class'):
        await channel.send('choose class:\nwarrior\nthief')

        def check(m):
            return m.content == 'warrior' or \
                   m.content == 'thief' and m.channel == channel
        msg = await client.wait_for('message', check=check)

        await channel.send('chosen {.content} class!'.format(msg))
    if message.content.startswith('-name'):
        await channel.send('choose name:')
        msg = await client.wait_for('message')
        await channel.send('hello {.content}!'.format(msg))



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
