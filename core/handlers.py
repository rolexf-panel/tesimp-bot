"""Default handlers."""
import logging
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = logging.getLogger(__name__)

class DefaultHandlers:
    def __init__(self, bot):
        self.bot = bot
        self._register()
        
    def _register(self):
        @self.bot.on_message(filters.command("start"))
        async def start(c, m):
            kb = InlineKeyboardMarkup([[InlineKeyboardButton("Help", callback_data="help")]])
            await m.reply(f"👋 Halo {m.from_user.first_name}!\n\nSaya Tesimp Bot.", reply_markup=kb)
            
        @self.bot.on_message(filters.command("help"))
        async def help(c, m):
            await m.reply("📋 Commands: /start, /help, /ping, /info, /example")
            
        @self.bot.on_message(filters.command("ping"))
        async def ping(c, m):
            import time
            s = time.time()
            r = await m.reply("🏓 Pong!")
            await r.edit_text(f"🏓 Pong! `{(time.time()-s)*1000:.2f}ms`")
            
        @self.bot.on_message(filters.command("info"))
        async def info(c, m):
            from platform import python_version
            import pyrogram
            await m.reply(f"🤖 Tesimp Bot\n🐍 Python {python_version()}\n📱 Pyrogram {pyrogram.__version__}")
