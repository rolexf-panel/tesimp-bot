"""Utility helpers."""
class RateLimiter:
    def __init__(self, max_calls=5, period=60):
        self.max_calls = max_calls
        self.period = period
        self.calls = {}
        
    def is_allowed(self, user_id):
        from datetime import datetime
        now = datetime.now()
        user_calls = self.calls.get(user_id, [])
        user_calls = [c for c in user_calls if (now - c).seconds < self.period]
        if len(user_calls) < self.max_calls:
            user_calls.append(now)
            self.calls[user_id] = user_calls
            return True
        self.calls[user_id] = user_calls
        return False
