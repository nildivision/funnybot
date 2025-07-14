import discord


class DickBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        return
