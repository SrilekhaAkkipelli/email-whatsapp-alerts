"""
Daily Limit Tracker Module
Tracks daily WhatsApp message count and resets at midnight.
"""

from datetime import datetime


class DailyLimitTracker:
    def __init__(self, daily_limit: int = 9):
        self.daily_limit = daily_limit
        self.sent_today = 0
        self.reset_date = datetime.now().date()

    def _check_reset(self):
        """Reset counter if a new day has started."""
        today = datetime.now().date()
        if today != self.reset_date:
            self.sent_today = 0
            self.reset_date = today

    def can_send(self) -> bool:
        """Check if we can still send messages today."""
        self._check_reset()
        return self.sent_today < self.daily_limit

    def record_sent(self):
        """Record that a message was sent."""
        self._check_reset()
        self.sent_today += 1

    def remaining(self) -> int:
        """Return number of messages we can still send today."""
        self._check_reset()
        return max(0, self.daily_limit - self.sent_today)

# update 20 - 2025-01-22
# update 21 - 2025-01-22