#===================================================
#IMPORT'S
#===================================================

import discord
import asyncio
import secreto
import random
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

    if message.content.lower().startswith('test'):
        await client.send_message(message.channel,"Qual foi Otário? Tá testando oq?")

    if message.content.lower().startswith('julio'):
        await client.send_message(message.channel,"~~viado~~ gente boa")

    if message.content.lower().startswith('me mama'):
        await client.send_message(message.channel,"Júlio é o primeiro a querer")		
        
    if message.content.lower().startswith('tururu'):
        await client.send_message(message.channel,"https://youtu.be/wEWF2xh5E8s")

    if message.content.lower().startswith('ygopro'):
    if message.content.lower().startswith('mediafire'):
        await client.send_message(message.channel,"**Aqui estar a `Cloud` do grupo**"
                                                  "https://www.mediafire.com/folder/4od2j7tu3nnoh/Upload_-_Discord")

    if message.content.lower().startswith('invite'):
        await client.send_message(message.channel,"https://discord.gg/pjRSBK4")	

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

    if message.content.lower().startswith('thinking'):
        thinking = discord.Embed(
            title="Fascinante!",
            color=COR,)

        botmsg = await client.send_message(message.channel, embed=thinking)

        await client.send_message(message.channel, "http://prntscr.com/jnu8g3")
        await client.send_message(message.channel, "http://prntscr.com/jnu2t2")
        await client.send_message(message.channel, "http://prntscr.com/jnu31b")
        await client.send_message(message.channel, "http://prntscr.com/jnu3a2")
# ===================================================
# FINALCRAFT REGRAS
# ===================================================
    if message.content.lower().startswith('regras'):
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

    if message.content.lower().startswith('moeda'): #Condição
        ##if message.author.id == "336311215099740160": #permissão por ID
        ##if message.author.id == "author.id":  # permissão por ID
        ##if message.author.id == msg.server.roles(STAFF):
        #if message.author.role == ("STAFF"):
        ##role = discord.utils.find(lambda r: r.name == "STAFF", msg.server.roles)
            choice = random.randint(1,2)
            if choice == 1:
              await client.add_reaction(message, '😑') #Reação por Emoji
            if choice == 2:
              await client.add_reaction(message, '👑') #Reação por Emoji
    ##else:
    ##        await client.send_message(message.channel, " Você não tem permissão para usar esse comando")
# ===================================================
#MUTE
# ===================================================

# ===================================================
#CARGOS
# ===================================================

#===================================================
#MÚSICA
#===================================================

#===================================================
#PARA FUNCIONAR
#===================================================
client.run(Token)
#===================================================
