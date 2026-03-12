"""Configuration management."""
import os
from dataclasses import dataclass

@dataclass
class BotConfig:
    api_id: int
    api_hash: str
    bot_token: str
    session_name: str = "tesimp_bot"
    workers: int = 8
    
    @classmethod
    def from_env(cls):
        return cls(
            api_id=int(os.getenv("API_ID", "0")),
            api_hash=os.getenv("API_HASH", ""),
            bot_token=os.getenv("BOT_TOKEN", ""),
            session_name=os.getenv("SESSION_NAME", "tesimp_bot"),
            workers=int(os.getenv("WORKERS", "8")),
        )
    
    def validate(self):
        return all([self.api_id > 0, len(self.api_hash) > 0, len(self.bot_token) > 0])
