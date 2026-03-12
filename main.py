#!/usr/bin/env python3
"""Tesimp Bot - Modular Telegram Bot."""
import asyncio, logging, signal, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from tesimp_bot.config.settings import BotConfig
from tesimp_bot.core.bot import TesimpBot
from tesimp_bot.core.handlers import DefaultHandlers
from tesimp_bot.plugins.example_plugin import ExamplePlugin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Runner:
    def __init__(self):
        self.bot = None
        
    async def shutdown(self):
        logger.info("Shutting down...")
        if self.bot and self.bot.is_running:
            await self.bot.stop()
        sys.exit(0)
        
    async def run(self):
        config = BotConfig.from_env()
        if not config.validate():
            logger.error("Invalid config! Check .env file")
            sys.exit(1)
            
        self.bot = TesimpBot(config)
        self.bot.initialize()
        DefaultHandlers(self.bot)
        self.bot.register_plugin(ExamplePlugin)
        
        for sig in (signal.SIGINT, signal.SIGTERM):
            asyncio.get_event_loop().add_signal_handler(sig, lambda: asyncio.create_task(self.shutdown()))
            
        await self.bot.start()

if __name__ == "__main__":
    try:
        asyncio.run(Runner().run())
    except KeyboardInterrupt:
        logger.info("Stopped by user")
