import re

def extract_emails(text):
    """
    Extracts valid email addresses from the input text.
    Handles most common email formats.
    """
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def extract_urls(text):
    """
    Extracts URLs starting with http or https.
    Stops extraction at whitespace or quotes.
    """
    pattern = r'https?://[^\s"]+'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    """
    Extracts phone numbers in formats like:
    (123) 456-7890, 123-456-7890, 123.456.7890, 123 456 7890
    """
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    """
    Extracts credit card numbers in these formats:
    1234 5678 9012 3456 or 1234-5678-9012-3456
    """
    pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_times(text):
    """
    Extracts time in 24-hour (14:30) or 12-hour (2:30 PM) formats.
    Handles optional spaces before AM/PM and case-insensitive.
    Returns the full matched time string.
    """
    pattern = r'\b((1[0-9]|2[0-3]|0?[0-9]):([0-5][0-9])(\s?[APMapm]{2})?)\b'
    matches = re.findall(pattern, text)
    # matches is list of tuples; extract full match (first group)
    return [match[0] for match in matches]

def main():
    # Read input data from file
    with open("test_cases.txt", "r", encoding="utf-8") as f:
        data = f.read()

    print("\n=== Emails ===")
    emails = extract_emails(data)
    print(emails)

    print("\n=== URLs ===")
    urls = extract_urls(data)
    print(urls)

    print("\n=== Phone Numbers ===")
    phones = extract_phone_numbers(data)
    print(phones)

    print("\n=== Credit Cards ===")
    cards = extract_credit_cards(data)
    print(cards)

    print("\n=== Times ===")
    times = extract_times(data)
    print(times)

if __name__ == "__main__":
    main()
