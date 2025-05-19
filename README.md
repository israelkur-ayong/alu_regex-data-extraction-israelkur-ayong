# alu_regex-data-extraction-israelkur-ayong

## Project Overview

This project uses Python and Regular Expressions (regex) to extract specific data types from large text inputs.  
Extracted data types include:
- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Times (12-hour and 24-hour formats)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/israelkur-ayong/alu_regex-data-extraction-israelkur-ayong.git

2. Navigate to the project directory:

   cd alu_regex-data-extraction-israelkur-ayong

3. Run the main script
   python regex_extractor.py

   ```
## Features 
 
- Supports multiple formats for each data type.
- Handles edge cases like missing spaces, multiple domain levels, mixed case AM/PM, etc.
- Clean and documented code.

## Sample Output

=== Emails ===
['user@example.com', 'firstname.lastname@company.co.uk', 'info123@site.org']

=== URLs ===
['https://www.example.com', 'https://subdomain.example.org/page', 'http://test-site.net/path?query=1']

=== Phone Numbers ===
['(123) 456-7890', '123-456-7890', '123.456.7890', '123 456 7890', '1234567890', '456\n1234567', '123456\n1234']

=== Credit Cards ===
['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']

=== Times ===
['14:30', '2:30 PM', '09:05 am']