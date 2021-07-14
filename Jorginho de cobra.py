# coding: utf-8
import discord
from discord.ext import commands
from discord.utils import get
import os
import youtube_dl
import asyncio
#from discord.ext.commands import Bot
import random
import praw
 reddit = praw.Reddit(client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                      password='1622001a', user_agent='textscript by /u/infantryBOT',
                      username='infantryBot')
#------------------------------------------------------------------------------#

                                #Token do bot
TOKEN = 'Njg4NDYxNDUzMzg4NTQ2MTEy.Xm2WJg.feO0MD5LhMZzOta_OybPRM3WZpY'
#------------------------------------------------------------------------------#

                                #Prefix do Bot
#Alterar para variável, para que futuramente seja alterado por msg
client = commands.Bot(command_prefix = '.')
#player de musica
players = {}

#------------------------------------------------------------------------------#

                        #Informa que o Bot esta funcionando
@client.event
async def on_ready():
    #await channel.send("Sim mestre!")
    #Seta o status do bot para online, não perturbe, invisivel ou ausente
    await client.change_presence(activity=discord.Game(name='I will do everything you want, but you will be charged!'))
    print('Bot esta pronto.')
#------------------------------------------------------------------------------#

                    #Informa que no chat foi feita alguma ação
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)
#------------------------------------------------------------------------------#
                                #teste de delete
@client.command()
async def is_me(m):
    return m.author == client.user
    deleted = await channel.purge(limit=100, check=is_me)
    await channel.send('Deleted {} message(s)'.format(len(deleted)))

#------------------------------------------------------------------------------#

            #Usa o comando ping para enviar as estatisticas do 'ping'
@client.command()
async def ping(channel):
    await channel.send('Pong {0}!'.format(round(client.latency, 1)))

#------------------------------------------------------------------------------#

                        #Usa o echo para o bot escrever algo
@client.command()
async def echo(channel,*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await channel.send(output)

#------------------------------------------------------------------------------#

                #Mostra a imagem do perfil do usuário requisitado
@client.command()
async def avatar(ctx, member: discord.Member):
     channel = ctx.message.channel
     author = ctx.message.author
     show_avatar = discord.Embed(
         color = discord.Color.blue()
     )
     show_avatar.set_footer(text=f"Solicitado por: {author.name}")
     show_avatar.set_image(url='{}'.format(member.avatar_url))
     await ctx.send(embed=show_avatar)

#------------------------------------------------------------------------------#
                    #mensagem apagada por qnt de msg enviada
@client.command()
async def clear(ctx,amount=1):
    await ctx.message.channel.purge(limit=amount+1)
    #await ctx.message.channel.send("Mensagem apagada!!")
#------------------------------------------------------------------------------#
                                #Embed == lista do bot
@client.command(pass_context=True)
async def displayembed(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Ao seu dispor!',
        description = 'Olá humanos... Meu mestre Gott me trouxe para esse mundo com um único objetivo, servir vocês.',
        colour = discord.Colour.dark_blue()
    )

    embed.set_footer(text='Copyright Gottschalk Raianne.')
    embed.set_image(url='https://cdn.discordapp.com/app-icons/688461453388546112/41dd77cdf750ffa5c5aa17e0991735c3.png?size=256')
    embed.set_author(name='infantry', icon_url='https://cdn.discordapp.com/app-icons/688461453388546112/41dd77cdf750ffa5c5aa17e0991735c3.png?size=256')
    embed.add_field(name='Version', value='0.0.1', inline=False)
    embed.add_field(name='Commands', value='.echo .ping .clear .avatar', inline=True)
    embed.add_field(name='About me', value='Eu playo musicas, converso com vcs, e mto NSFW', inline=True)

    await ctx.send(embed=embed)

#------------------------------------------------------------------------------#
                            #Lista de Comandos NSFW

@client.command(pass_context=True)
async def displaynsfw(ctx):
    channel = ctx.message.channel
    nsfw = discord.Embed(
        title = 'Comandos: ',
        colour = discord.Colour.teal()
    )

    nsfw.set_footer(text='Copyright Gottschalk Raianne.')
    nsfw.add_field(name='.boobs', value='Send boobs image', inline=False)
    nsfw.add_field(name='.ass', value='Send ass image', inline=False)
    nsfw.add_field(name='.lewd', value='Send lewd image', inline=False)
    nsfw.add_field(name='.pussy', value='Send pussy image', inline=False)
    nsfw.add_field(name='.hentai', value='Send hentai image', inline=False)
    nsfw.add_field(name='.anal', value='Send anal image', inline=False)
    nsfw.add_field(name='.gif', value='Send porn gif image', inline=False)
    nsfw.add_field(name='.4k', value='Send 4k porn image', inline=False)
    await ctx.send(embed=nsfw)
#------------------------------------------------------------------------------#
                                #Comandos NSFW

#------------------------------------------------------------------------------#
                                #lista de commandos
@client.command()
async def list(channel):
    await channel.send("```css\n.echo\n.ping\n.clear\n.avatar {usuario}\n.displayembed```")
#------------------------------------------------------------------------------#

                                 #Inicia o bot
client.run(TOKEN)

#-----------------------------------music--------------------------------------#
#conectar
#@client.command(pass_context=True)
#async def join(ctx):
    # global voice
    # channel = ctx.message.author.voice.channel
    # voice = get(client.voice_client, guild=ctx.guild)
    #
    # if voice and voice.is_connected():
    #     await voice.move_to(channel)
    # else:
    #     voice = await channel.connect()
    #     print(f"The bot has connect to {channel}\n")
    #
    # await ctx.send(f"Joined {channel}")
    # await voice.disconnect()
    # if ctx.message.author.voice:
    #     channel = ctx.message.author.voice.channel
    #     await channel.connect()
    #
    # await ctx.send(f"Conectou em: {channel}")
# #desconectar
# @client.command(pass_context=True)
# async def leave(ctx):
#     channel = ctx.message.author.voice.channel
#     voice = get(client.voice_client, guild=ctx.guild)
#
#     if voice and voice.is_connected():
#         await voice.disconnect()
#         print(f"The bot has left {channel}\n")
#         await ctx.send(f"Left {channel}")
#     else:
#         print(f"bot was told to leave voice channel, but was not is one")
#         await ctx.send("Don't think I am in a voice channel")
#     # await ctx.voice_client.disconnect()#disconecta o bot do canal
#
# @client.command(pass_context=True)
# async def play(ctx,url, str):
#     song_there = ps.path.isfile("song.mp3")
#     if song_there:
#         os.remove("song.mp3")
#         print("Removed old song file")
#

    # vc = await channel.connect()
    # vc.play(discord.FFmpegPCAudio('testing.mp3'), after=lambda e:print('done', e))
    # vc.is_playing()
    # vc.plause()
    # vc.resume()
    # vc.stop()
    # ghttps://www.facebook.com/brasilverso/videos/2510402345942753/UzpfSTEwMDAwMTcxODY5MTk0MToyOTYxMTcxNzYzOTUwMDg0/

#Diz oi para o usuario
# @client.command()
# async def oi(message):
#     id = client.get_guild(681178825484533820)
#
#     if message.content == ".oi":
#         await message.channel.send("Oi!")
#     elif message.content == ".qntd":
#         await channel.send(f"""São {id.member_count} usuários nessa bagaça""")

        # channel = message.channel
        # await channel.send('Say hello!')
        #
        # def check(m):
        #     return m.content == 'hello' and m.channel == channel
        #
        # msg = await client.wait_for('message', check=check)
        # await channel.send('Olá {.author}!'.format(msg))

    #channel = message.channel
    #author = message.author
    #await channel.send('Olá ',{}:, author)
# @client.event
# async def on_message(message):
#     channel = message.channel
#     if message.content.startswith('.ping'):
#         await message.channel.send('pong!')
#
#     if message.content.startswith('.echo'):
#         msg = message.content.split()
#         output = ''
#         for word in msg[1:]:
#             #.echo Hello World
#             #msg = ['.echo', 'Hello', 'World']
#             output += word
#             output += ' '
#
#             await message.channel.send'(output)
#
# @client.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     await message.channel.send('Apagou eheheh')
#     #await message.author.send('👋') abc.Messageable.send()
# @bot.event
# async def on_ready():
#     await channel.send('Hello World')
#
#
# apagar msg de bot
# def is_me(m):
#     return m.author == client.user
#
# deleted = await channel.purge(limit=100, check=is_me)
# await channel.send('Deleted {} message(s)'.format(len(deleted)))
