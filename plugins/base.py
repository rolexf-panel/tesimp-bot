"""Base plugin class."""
class BasePlugin:
    name = "base"
    version = "1.0.0"
    description = "Base plugin"
    author = "Unknown"
    enabled = True
    
    def __init__(self, bot):
        self.bot = bot
        self.client = bot.client
        self._initialized = False
        
    async def on_start(self):
        self._initialized = True
        
    async def on_stop(self):
        self._initialized = False
        
    def register_commands(self):
        return {}
