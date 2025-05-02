"""
Email Filter Module
Filters important emails based on keywords and sender addresses.
"""

DEFAULT_KEYWORDS = [
    'urgent', 'invoice', 'meeting', 'bank', 'payment',
    'approved', 'deadline', 'action required', 'important',
    'offer', 'interview', 'result', 'scholarship'
]


def is_important(subject: str, keywords: list = None) -> bool:
    """
    Check if an email is important based on subject keywords.
    
    Args:
        subject: Email subject line
        keywords: List of keywords to match (uses defaults if None)
    
    Returns:
        True if email matches any keyword, False otherwise
    """
    if keywords is None:
        keywords = DEFAULT_KEYWORDS

    subject_lower = subject.lower()
    return any(keyword.lower() in subject_lower for keyword in keywords)


def filter_emails(emails: list, keywords: list = None) -> list:
    """
    Filter a list of (sender, subject) tuples for important emails.
    
    Args:
        emails: List of (sender, subject) tuples
        keywords: Keywords to filter by
    
    Returns:
        List of important (sender, subject) tuples
    """
    return [
        (sender, subject)
        for sender, subject in emails
        if is_important(subject, keywords)
    ]


def format_alert(batch: list) -> str:
    """
    Format a batch of emails into a WhatsApp message string.
    
    Args:
        batch: List of (sender, subject) tuples
    
    Returns:
        Formatted message string
    """
    lines = ["📧 *New Email Alerts*\n"]
    for i, (sender, subject) in enumerate(batch, 1):
        lines.append(f"*{i}.* From: {sender}\n   Subject: {subject}")
    return "\n\n".join(lines)

# update 25 - 2025-01-25
# update 44 - 2025-02-05
# update 47 - 2025-02-06
# update 74 - 2025-02-20
# update 89 - 2025-03-06
# update 90 - 2025-03-06
# update 94 - 2025-03-09
# update 99 - 2025-03-11
# update 108 - 2025-03-18
# update 111 - 2025-03-19
# update 150 - 2025-04-14
# update 152 - 2025-04-15
# update 165 - 2025-04-20
# update 182 - 2025-04-29
# update 186 - 2025-05-02