#===================================================
#IMPORT'S
#===================================================

import discord
import asyncio
import secreto
#import random
#import cargos
#import moedas
#import reação
#import purge
#import music

#===================================================
client = discord.Client()
#===================================================
COR = 0x690FC3
Token = secreto.seu_token()
#cargos = cargos.cargos()
#coin = moedas.moeda()
msg_id = None
msg_user = None

#===================================================
#IDENTIDADE PELO CONSOLE
#===================================================

@client.event
async def on_ready():
    print('===================================================')
    print('BOT ONLINE: - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('===================================================')
    print('Version - 1.2')
    print('Dai Ikuyo! WariansForce!')
    print('===================================================')

#===================================================
#MODELO PARA COMANDOS
#===================================================

@client.event
async def on_message(message): #Condição
    if message.content.lower().startswith('#test'): #PREFIX DO COMANDO (Deste, no caso)
        await client.send_message(message.channel,"**não irei falar! Você não manda em mim!**") #Mensagem como resultado

    #if message.content.lower().startswith('test'):
    #    await client.send_message(message.channel,"Qual foi Otário? Tá testando oq?")

#===================================================
#Relacionados ao servidor
#===================================================	

#===================================================
# ==================================================

    #if message.content.lower().startswith('julio'):
    #    await client.send_message(message.channel,"~~viado~~ gente boa")

    #if message.content.lower().startswith('me mama'):
    #    await client.send_message(message.channel,"Júlio é o primeiro a querer")		
        
    if message.content.lower().startswith('tururu'):
        await client.send_message(message.channel,"https://youtu.be/wEWF2xh5E8s")

    if message.content.lower().startswith('launcher'):
        await client.send_message(message.channel,"**Aqui está o download!**"
                                                  "https://mc-launcher.com/launchers")
    #if message.content.lower().startswith('ygoprolink'):
    #    await client.send_message(message.channel,"**Aqui está o download!**"
    #                                             "https://mega.nz/#!tuYkRSbK!IlArObfQ5dDWwDrJW1RovgAoOQbUmk6S4cSWGSO1uYk")											  
    #if message.content.lower().startswith('mediafire'):
    #    await client.send_message(message.channel,"**Aqui está a `Cloud` do grupo**"
    #                                              "https://www.mediafire.com/folder/4od2j7tu3nnoh/Upload_-_Discord")	
    #if message.content.lower().startswith('#comandos'):
    #    await client.send_message(message.channel,"**# = Prefix.** `help, test`. **Sem prefix** `invite, fazer oq, aspectos, ygopro, mediafire, ygoprolink, tururu`")

    #if message.content.lower().startswith('invite'):
    #    await client.send_message(message.channel,"https://discord.gg/pjRSBK4")	
    #if message.content.lower().startswith('#help'):
    #    await client.send_message(message.channel,"**NÃO SETARAM NADA NESTE COMANDO NÃO ANIMAL!!**")	

# ===================================================
# Mensagens Contínuas
# ===================================================

# ===================================================
# Respostas por Embed | Imagens
# ===================================================

    if message.content.lower().startswith('fazer oq'): #PREFIX DO COMANDO (Deste, no caso)
        fazer = discord.Embed(
            title="**fazer o que né!**",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=fazer)

        await client.send_message(message.channel, "http://prntscr.com/jhraie")
# ===================================================
# YGOPRO
# ===================================================		
    if message.content.lower().startswith('ygopro'):
        ygopro = discord.Embed(
            title="**Aqui está o download!**",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=ygopro)
		
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/450114879387598848/469978629238161428/Ygopro-1.033.D-Percy_Windows_Installer.torrent")
        await client.send_message(message.channel, "Use `ygoprolink` pra baixar a versão LINK. Into the VRAINS!!")		
# ===================================================
# YGOPRO LINK
# ===================================================
    if message.content.lower().startswith('ygoprolink'):
        ygoprolink = discord.Embed(
            title="**Aqui está o download!**",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=ygoprolink)

        await client.send_message(message.channel, "https://mega.nz/#!tuYkRSbK!IlArObfQ5dDWwDrJW1RovgAoOQbUmk6S4cSWGSO1uYk")	
# ===================================================
# MEDIA FIRE
# ===================================================	
    if message.content.lower().startswith('#mediafire'):
        mediafire = discord.Embed(
            title="**Aqui está a `Cloud` do grupo**",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=mediafire)

        await client.send_message(message.channel, "https://www.mediafire.com/folder/4od2j7tu3nnoh/Upload_-_Discord")	
# ===================================================
# ASPECTOS THAUMCRAFT
# ===================================================
    if message.content.lower().startswith('aspectos'):
        aspectos = discord.Embed(
            title="**Aqui está a lista de aspectos**",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=aspectos)

        await client.send_message(message.channel, "```É RECOMENDADO DAR ZOOM```")		
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/430853602580627461/465940029982769162/Screenshot-2017-11-29_List_of_Aspects_Thaumcraft_4_-_Feed_The_Beast_Wiki1.png")		
# ===================================================
# 
# ===================================================
    if message.content.lower().startswith('thinking'):
        thinking = discord.Embed(
            title="Fascinante!",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=thinking)

        await client.send_message(message.channel, "http://prntscr.com/jnu8g3")
        await client.send_message(message.channel, "http://prntscr.com/jnu2t2")
        await client.send_message(message.channel, "http://prntscr.com/jnu31b")
        await client.send_message(message.channel, "http://prntscr.com/jnu3a2")
		
		
    #if message.content.lower().startswith('juliao'):
    #    julio = discord.Embed(
    #        title="**meu pau na sua mão! KKKKKKJJJKKK** ``TROLEI``",
    #        color=COR,)		

    #    botmsg = await client.send_message(message.channel, embed=julio)

    #    await client.send_message(message.channel, "http://prntscr.com/klfcbs")
# ===================================================
# FINALCRAFT REGRAS
# ===================================================
    if message.content.lower().startswith('#rules'):
        regras = discord.Embed(
            title="Aqui estar as regras da Network **FinalCraft**",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=regras)

        await client.send_message(message.channel, "http://prntscr.com/kcygj5")
        await client.send_message(message.channel, "http://prntscr.com/kcygnv")
        await client.send_message(message.channel, "http://prntscr.com/kcygte")
		
#===================================================
#FLIP COIN
#===================================================

    # if message.content.lower().startswith('moeda'): #Condição
    #     ##if message.author.id == "336311215099740160": #permissão por ID
    #     ##if message.author.id == "author.id":  # permissão por ID
    #     ##if message.author.id == msg.server.roles(STAFF):
    #     #if message.author.role == ("STAFF"):
    #     ##role = discord.utils.find(lambda r: r.name == "STAFF", msg.server.roles)
    #         choice = random.randint(1,2)
    #         if choice == 1:
    #           await client.add_reaction(message, '😑') #Reação por Emoji
    #         if choice == 2:
    #           await client.add_reaction(message, '👑') #Reação por Emoji
    ##else:
    ##        await client.send_message(message.channel, " Você não tem permissão para usar esse comando")
# ===================================================
#MUTE
# ===================================================

# ===================================================
#CARGOS
# ===================================================
@client.event

async def on_message(message):
    if message.content.lower().startswith("#cargo"):
     if message.author.id == "336311215099740160":
     #if message.author.role == "STAFF":

        embed =discord.Embed(

        title="Escolha seu Cargo!",

        color=COR,

        description="- League Of Legends = 📘\n"

                    "- Paladins  =  📕\n"

                    "- Minecraft  = 📗",)
    botmsg = await client.send_message(message.channel, embed=embed)
    await client.add_reaction(botmsg, "📘")
    await client.add_reaction(botmsg, "📕")
    await client.add_reaction(botmsg, "📗")

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):

    msg = reaction.message

    if reaction.emoji == "📘" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "League Of Legends", msg.server.roles)
     await client.add_roles(user, role)

     print("add")

    if reaction.emoji == "📕" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Paladins", msg.server.roles)
     await client.add_roles(user, role)

     print("add")

    if reaction.emoji == "📗" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Minecraft", msg.server.roles)
     await client.add_roles(user, role)

     print("add")

@client.event
async def on_reaction_remove(reaction, user):

    msg = reaction.message

    if reaction.emoji == "📘" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "League Of Legends", msg.server.roles)
     await client.remove_roles(user, role)

     print("remove")

    if reaction.emoji == "📕" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Paladins", msg.server.roles)
     await client.remove_roles(user, role)

     print("remove")

    if reaction.emoji == "📗" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Minecraft", msg.server.roles)
     await client.remove_roles(user, role)

     print("remove")
# ===================================================
#
# ===================================================

#===================================================
#MÚSICA
#===================================================

#===================================================
#PARA FUNCIONAR
#===================================================
client.run(Token)
#===================================================
