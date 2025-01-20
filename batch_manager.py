"""
Batch Manager Module
Groups important emails into batches before sending alerts.
"""

from email_filter import format_alert


class BatchManager:
    def __init__(self, batch_size: int = 3):
        self.batch_size = batch_size
        self.current_batch = []

    def add(self, sender: str, subject: str) -> bool:
        """
        Add an email to the current batch.
        Returns True if batch is ready to send.
        """
        self.current_batch.append((sender, subject))
        return len(self.current_batch) >= self.batch_size

    def get_message(self) -> str:
        """Get formatted WhatsApp message for current batch."""
        return format_alert(self.current_batch)

    def flush(self) -> str:
        """Get message and clear batch."""
        msg = self.get_message()
        self.current_batch = []
        return msg

    def has_pending(self) -> bool:
        """Check if there are unsent emails in batch."""
        return len(self.current_batch) > 0

# update 9 - 2025-01-16
# update 16 - 2025-01-20