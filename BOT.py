import discord
import asyncio


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(588719932187869184)
        while not self.is_closed():
            await channel.send('Не забывайте обновлять свои приглашения!\n'
                               '    — приглашения в гильдии удаляются при достижении 7-дневного возраста;\n'
                               '    — посты в канале для десанта удаляются при достижении 14-дневного возраста;\n'
                               '    — приглашения в альянсы удаляются при достижении 30-дневного возраста')
            await asyncio.sleep(259200)


client = MyClient()
client.run('NjgyNTU2OTUzMjE3NTk3NDQw.XlfIpg.AZf3o3_tVc-OL784vmP-XwiEEOo')
