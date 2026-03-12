"""Core bot using Pyrogram."""
import logging
from pyrogram import Client
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TesimpBot:
    def __init__(self, config):
        self.config = config
        self.client = None
        self._plugins = []
        self._running = False
        
    def initialize(self):
        if not self.config.validate():
            raise ValueError("Invalid configuration!")
        self.client = Client(
            name=self.config.session_name,
            api_id=self.config.api_id,
            api_hash=self.config.api_hash,
            bot_token=self.config.bot_token,
            workers=self.config.workers,
            workdir="sessions"
        )
        logger.info(f"Bot initialized: {self.config.session_name}")
        
    def register_plugin(self, plugin_class):
        plugin = plugin_class(self)
        self._plugins.append(plugin)
        logger.info(f"Plugin registered: {plugin_class.__name__}")
        
    def on_message(self, filters=None, group=0):
        def decorator(func):
            if self.client:
                self.client.add_handler(MessageHandler(func, filters), group=group)
            return func
        return decorator
        
    def on_callback(self, filters=None, group=0):
        def decorator(func):
            if self.client:
                self.client.add_handler(CallbackQueryHandler(func, filters), group=group)
            return func
        return decorator
        
    async def start(self):
        if not self.client:
            self.initialize()
        self._running = True
        for plugin in self._plugins:
            if hasattr(plugin, 'on_start'):
                await plugin.on_start()
        await self.client.start()
        logger.info("Bot is running!")
        await self.client.idle()
        
    async def stop(self):
        self._running = False
        for plugin in self._plugins:
            if hasattr(plugin, 'on_stop'):
                await plugin.on_stop()
        if self.client:
            await self.client.stop()
        logger.info("Bot stopped.")
        
    @property
    def is_running(self):
        return self._running
