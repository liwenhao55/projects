# This is a discord Bot I made from a youtube tutorial
import os
import discord 
import asyncio
import random
import datetime

token = os.getenv("ODM2Nzk2MTQxMTgxNTk5NzU1.YIjNIg.Uc5VCNChNc1SX5eVm-vbHAdsaoM")

bot = discord.Client()


@bot.event
async def on_member_join(member):
	if member.id == bot.id:
		return
	channel = discord.utils.get(bot.guilds[0].channels, name="general")
	response = f"Welcome to the test, {member.name}."
	await channel.send(response)


@bot.event
async def on_message(message):
	print(vars(bot))
	if message.author == bot.user:
		return
	channel = message.channel
	keywords = ["hello", "morning", "see you", "what's up", "up", "good night", "test", "nice", "pie"]
	for keyword in keywords:
		if keyword.lower() in message.content.lower():
			response = f"Did someone say {keyword.lower()}? here is a hug <@{message.author.id}>!"
			await channel.send(response)


@bot.event
async def test():
	while(True):
		await bot.wait_until_ready()
		online_members = []
		for member in bot.get_all_members():
			if member.status != discord.Status.offline and member.id != bot.user.id:
				online_members.append(member.id)
		if len(online_members) > 0:
			user = random.choice(online_members)
			current_time = int(datetime.datetime.now().strftime("%I"))
			channel = discord.utils.get(bot.guilds[0].channels, name="general")
			message = f"It's {current_time} o'clock! Time for some food <@{user}>"

			await channel.send(message)
		await asyncio.sleep(3600)


bot.loop.create_task(test())
bot.run("ODM2Nzk2MTQxMTgxNTk5NzU1.YIjNIg.Uc5VCNChNc1SX5eVm-vbHAdsaoM")
