import time


class RateLimiter:
    def __init__(self, max_calls: int, period_seconds: int):
        self.max_calls = max_calls
        self.period = period_seconds
        self.calls = {}

    def allow(self, key: str) -> bool:
        now = time.time()
        if key not in self.calls:
            self.calls[key] = []

        self.calls[key] = [
            ts for ts in self.calls[key] if now - ts < self.period
        ]

        if len(self.calls[key]) >= self.max_calls:
            return False

        self.calls[key].append(now)
        return True
