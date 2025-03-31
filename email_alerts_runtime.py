"""
Email Alerts Runtime Module
Main backend logic: fetch → filter → batch → send via WhatsApp.
"""

import os
import pickle
from authenticate_gmail import authenticate_gmail, get_unread_emails, extract_subject_sender
from email_filter import is_important
from whatsapp_sender import send_whatsapp_message
from batch_manager import BatchManager
from daily_limit import DailyLimitTracker


def run_alerts(
    credentials_file: str,
    twilio_sid: str,
    twilio_auth: str,
    from_number: str,
    to_number: str,
    batch_size: int = 3,
    daily_limit: int = 9,
    keywords: list = None,
    unread_threshold: int = 50
):
    """
    Main function to run the email alert system.
    
    Steps:
      1. Authenticate Gmail
      2. Fetch unread emails
      3. Check unread threshold warning
      4. Filter important emails
      5. Batch and send WhatsApp alerts
      6. Respect daily message limits
    """
    # Authenticate and connect to Gmail
    service = authenticate_gmail(credentials_file)
    messages = get_unread_emails(service)
    print(f"📬 Found {len(messages)} unread emails.")

    tracker = DailyLimitTracker(daily_limit)
    batcher = BatchManager(batch_size)
    alerted_subjects = set()

    # Step 3: Unread threshold warning
    if len(messages) >= unread_threshold:
        warning = f"⚠️ You have {len(messages)}+ unread emails. Please check your inbox."
        if tracker.can_send():
            send_whatsapp_message(warning, twilio_sid, twilio_auth, from_number, to_number)
            tracker.record_sent()

    # Step 4-6: Filter and batch
    for msg in messages:
        if not tracker.can_send():
            limit_msg = "🚫 Daily WhatsApp message limit reached. Alerts resume tomorrow."
            send_whatsapp_message(limit_msg, twilio_sid, twilio_auth, from_number, to_number)
            break

        sender, subject = extract_subject_sender(service, msg['id'])

        # Skip duplicates
        if subject in alerted_subjects:
            continue

        if is_important(subject, keywords):
            alerted_subjects.add(subject)
            batch_ready = batcher.add(sender, subject)

            if batch_ready:
                alert_msg = batcher.flush()
                send_whatsapp_message(alert_msg, twilio_sid, twilio_auth, from_number, to_number)
                tracker.record_sent()

    # Send remaining batch (< batch_size)
    if batcher.has_pending() and tracker.can_send():
        alert_msg = batcher.flush()
        send_whatsapp_message(alert_msg, twilio_sid, twilio_auth, from_number, to_number)
        tracker.record_sent()

    print(f"✅ Done. Messages sent today: {tracker.sent_today}/{daily_limit}")

# update 3 - 2025-01-11
# update 11 - 2025-01-17
# update 12 - 2025-01-17
# update 15 - 2025-01-19
# update 23 - 2025-01-23
# update 38 - 2025-01-31
# update 55 - 2025-02-10
# update 56 - 2025-02-10
# update 67 - 2025-02-17
# update 76 - 2025-02-21
# update 80 - 2025-02-23
# update 105 - 2025-03-16
# update 110 - 2025-03-19
# update 114 - 2025-03-22
# update 121 - 2025-03-28
# update 123 - 2025-03-29
# update 124 - 2025-03-29
# update 127 - 2025-03-31