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
# update 26 - 2025-01-26
# update 30 - 2025-01-27
# update 52 - 2025-02-08
# update 66 - 2025-02-16
# update 77 - 2025-02-22
# update 83 - 2025-02-24
# update 84 - 2025-02-27
# update 85 - 2025-03-01
# update 100 - 2025-03-12
# update 118 - 2025-03-27
# update 119 - 2025-03-27
# update 134 - 2025-04-04
# update 140 - 2025-04-06
# update 156 - 2025-04-17
# update 166 - 2025-04-21
# update 167 - 2025-04-22
# update 168 - 2025-04-23