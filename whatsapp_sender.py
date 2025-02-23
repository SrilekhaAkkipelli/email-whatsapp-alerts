"""
WhatsApp Sender Module
Sends WhatsApp messages via Twilio API.
"""

from twilio.rest import Client


def send_whatsapp_message(
    body: str,
    twilio_sid: str,
    twilio_auth: str,
    from_number: str,
    to_number: str
) -> bool:
    """
    Send a WhatsApp message using Twilio.

    Args:
        body: Message content
        twilio_sid: Twilio Account SID
        twilio_auth: Twilio Auth Token
        from_number: Twilio sandbox number (whatsapp:+14155238886)
        to_number: Recipient number (whatsapp:+91XXXXXXXXXX)

    Returns:
        True if sent successfully, False otherwise
    """
    try:
        client = Client(twilio_sid, twilio_auth)
        message = client.messages.create(
            body=body,
            from_=from_number,
            to=to_number
        )
        print(f"✅ WhatsApp message sent. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")
        return False

# update 6 - 2025-01-14
# update 14 - 2025-01-19
# update 32 - 2025-01-29
# update 34 - 2025-01-29
# update 35 - 2025-01-30
# update 40 - 2025-02-03
# update 58 - 2025-02-11
# update 73 - 2025-02-19
# update 79 - 2025-02-22
# update 81 - 2025-02-23