
import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.members = True



default_prefix = "f!"




client = commands.Bot(command_prefix= default_prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
 print(f'BotName {client.user.name} Botid {client.user.id}')
 while True:
  await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} guilds"))
  await asyncio.sleep(30)
  await client.change_presence(activity=discord.Game(name=f"Over {len(client.users)}  Members!"))
  await asyncio.sleep(30)

#fun commands
@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000, 1)
    embed = discord.Embed(title='<a:ping:957655962615943218> pong',description=f' **:robot: Bot Ping:**\n`{round(client.latency * 1000)}ms`\n\n**:hourglass: Api Latency:**\n`{latency}ms`')
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.guild.icon.url}")
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")
    await ctx.send(embed=embed)


@client.command()
async def botinfo(ctx):
 latency = round(client.latency * 1000, 1)  
 embed=discord.Embed()
 embed.add_field(name="❓ My Prefix is:",value=f"`{default_prefix}`",inline=False)
 embed.add_field(name="🏓My Ping is:",value=f"`{latency}ms`")
 embed.add_field(name="<a:developer:957347306875781240> My Developer is:",value=f"<@941455820535775302> | `φully`",inline=False)
 embed.add_field(name="<:adminperms:957348347268722818> My Owners are:",value="<@941455820535775302>, <@512911725339738112>",inline=False)
 embed.add_field(name="<a:ping:957655962615943218> Discord.py Version",value="`1.7.3`",inline=False)
 embed.add_field(name="<a:ping:957655962615943218> Python Version",value="`3.9.5`",inline=False)
 embed.add_field(name="<a:ping:957655962615943218> Pycord Version",value=f"`2.0.0b4`")
 embed.add_field(name="🧩 Server",value=f"`{len(client.guilds)}`",inline=False)
 embed.add_field(name="👥 Member",value=f"`{len(client.users)}`",inline=False)
 embed.set_author(name=f"{ctx.author.name}", icon_url=f'{ctx.author.avatar.url}')
 embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")
 await ctx.send(embed=embed)
 await ctx.message.delete()


@client.command()
async def serverinfo(ctx):
    guild = ctx.guild
    memberCount = str(guild.member_count)
    owner = str(guild.owner)
    guildid = str(ctx.message.guild.id)
    Region = str(ctx.guild.region)
    soon = "soon"
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    kanal = text_channels + voice_channels


    embed=discord.Embed()
    embed.add_field(name='👑Owner',value=owner,inline=True)
    embed.add_field(name='🆔Server ID', value=guildid, inline=True)
    embed.add_field(name="🌎 Region",value=Region,inline=True)
    embed.add_field(name="👥 Member",value=memberCount,inline=True)
    embed.add_field(name="🤖 Bots",value=soon,inline=True)
    embed.add_field(name="👥 User",value=soon,inline=True)
    embed.add_field(name="🟢 Online User",value=soon,inline=True)
    embed.add_field(name="🔴 Offline User",value=soon,inline=True)
    embed.add_field(name="💬 Channel",value=kanal,inline=True)
    embed.add_field(name="📆 Servererstellung",value=soon,inline=False)
    embed.add_field(name='🗂 Kategorien', value=soon,inline=False)
    embed.add_field(name='Rollen', value=soon, inline=False)
    embed.add_field(name='✅ Verifizierungslevel', value=soon, inline=False)
    embed.add_field(name='✨ Boosts', value=soon, inline=True)
    embed.add_field(name='🥇 Boostlevel', value=soon, inline=True)
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")
    await ctx.send(embed=embed)




#help commands
@client.group()
async def help(ctx):
 embed=discord.Embed(title="Help",description=f"Use {default_prefix}help <command> for more information about a command.")
 embed.add_field(name='❓ My Prefix is:',value=f"`{default_prefix}`",inline=False)
 embed.add_field(name="help_moderation",value=f"Shows the orders of the moderators",inline=True)
 embed.add_field(name="help_fun",value="Displays Fun cmd`s",inline=True)
 embed.set_author(name=f"{ctx.author.name}", icon_url=f'{ctx.author.avatar.url}')
 embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}") 
 await ctx.send(embed=embed)


@client.group()
async def help_fun(ctx):
    embed=discord.Embed(title="help Fun")
    embed.add_field(name="`serverinfo`",value="Displays information about the server",inline=True)
    embed.add_field(name="`botinfo`",value="Shows you the statistics of the bot",inline=True)
    embed.set_author(name=f"{ctx.author.name}", icon_url=f'{ctx.author.avatar.url}')
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")
    await ctx.send(embed=embed) 



@client.group()
async def help_moderation(ctx):
 embed=discord.Embed(title="Moderation")
 embed.add_field(name="`kick`",value=f"Kicks a user",inline=True)
 embed.add_field(name="`ban`",value=f"Ban a user",inline=True)
 embed.add_field(name="`unban`",value=f"Unban a banned user",inline=True)
 embed.add_field(name="`clear`",value="deletes messages",inline=True)
 embed.add_field(name="`embed`",value="Write an embedded message with the bot",inline=True)
 embed.add_field(name="`say`",value="Write a message with the bot",inline=True)
 embed.add_field(name="`lock`",value="does the channel that no one can write anymore",inline=True)
 embed.add_field(name="`unlock`",value="makes the channel open so that everyone can write",inline=True)
 embed.add_field(name="`slowmode`",value="With this you can set the slow mode of the respective channel ⏲",inline=True)
 embed.set_author(name=f"{ctx.author.name}", icon_url=f'{ctx.author.avatar.url}')
 embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")
 await ctx.send(embed=embed)   



#mod commands
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f' Kicked {member.mention}')

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@commands.has_permissions(manage_messages=True)
@client.command()
async def clear(ctx, count=1):
    messages = await ctx.channel.purge(limit=count+1)
    embed=discord.Embed(title=f"{len(messages)-1} messages successfully deleted!")
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_author(name=f"{ctx.author.name}", icon_url=f'{ctx.author.avatar.url}')
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon.url}")
    await ctx.send(embed=embed, delete_after=5)

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx,user : discord.User,*,reason=None):
    guild = ctx.guild
    mbed =  discord.Embed(title='Success!',description=f"{user} has successfully been unbanned.")
    await ctx.send(embed=mbed)
    await guild.unban(user=user)
    
@client.command()
async def embed(ctx,*, saymsg=None):
    if saymsg==None:
        return await ctx.send("Please write a sentence you want the bot to say!")
     
    sayEmbed = discord.Embed(color = discord.Color.blue(), description=f"{saymsg}")
    await ctx.send(embed = sayEmbed)
    await ctx.message.delete()

@client.command()
async def say(ctx,*, message=None):
    await ctx.send(message)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

    embed=discord.Embed(title=f'🔒 Locked',description=f'Reason: {reason}')

    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed=discord.Embed(title=f'🔓 Unlocked',description=f'Reason: {reason}')
    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx,seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"set the slowmode delay in this channel to {seconds} seconds!",delete_after=5) 
    await ctx.message.delete()
#events

client.run("")  
