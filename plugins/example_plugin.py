"""Example plugin."""
from pyrogram import filters
from tesimp_bot.plugins.base import BasePlugin

class ExamplePlugin(BasePlugin):
    name = "example"
    version = "1.0.0"
    description = "Demo plugin"
    author = "Tesimp"
    
    def __init__(self, bot):
        super().__init__(bot)
        self.count = 0
        
    async def on_start(self):
        await super().on_start()
        
        @self.bot.on_message(filters.command("example"))
        async def cmd(c, m):
            await m.reply(f"🎉 Plugin aktif!\n📊 Count: {self.count}")
            
        @self.bot.on_message(filters.group & filters.text)
        async def counter(c, m):
            self.count += 1
