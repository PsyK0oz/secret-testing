# Sample Secrets File for Scanning with TruffleHog and Gitleaks

# Verified Secret: API key for a real service (Real secret)
API_KEY_1 = "sk_live_51HxxxxxYYYYYYYYYxxxxZZZZZZZZZZZZ"  # Verified secret (Real)
API_KEY_2 = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXXXX"  # Verified secret (Real)

# False Positive: This looks like a password but is not
FAKE_PASSWORD_1 = "pass123"  # False positive (Not a real secret)
FAKE_PASSWORD_2 = "dummyPassword!"  # False positive (Not a real secret)

# Verified Secret: AWS Access Key ID (Real secret)
AWS_ACCESS_KEY_ID_1 = "AKIAIOSFODNN7EXAMPLE"  # Verified secret (Real)
AWS_ACCESS_KEY_ID_2 = "AKIAJHFLKJSLDKFJSLDKF"  # Verified secret (Real)

# False Positive: A random string that looks like an AWS Secret Access Key
AWS_SECRET_ACCESS_KEY_1 = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Verified secret (Real)
AWS_SECRET_ACCESS_KEY_2 = "xJfksjXpntLSFKEFZDOFKERJDFlsdfsfd"  # False positive (Not a real secret)

# False Positive: This could be mistaken as a credit card number, but it's not
CREDIT_CARD_FAKE_1 = "1234 5678 9012 3456"  # False positive (Not a real secret)
CREDIT_CARD_FAKE_2 = "4321 8765 2109 6543"  # False positive (Not a real secret)

# Unverified Secret: API Key that needs manual verification (Not sure if real or false)
POTENTIAL_API_KEY_1 = "api_test_aBcdEfGhIJKlmnopQrStUv"  # Unverified (May be real or false)
POTENTIAL_API_KEY_2 = "api_prod_ZYXWVuTsrQPonmlkjihgfedcba"  # Unverified (May be real or false)

# Verified Secret: GitHub Personal Access Token (Real secret)
GITHUB_PAT_1 = "ghp_A1B2C3D4E5F6G7H8I9J0KLMNOPQRST"  # Verified secret (Real)
GITHUB_PAT_2 = "ghp_1234abcd5678efgh9012ijklmnopqrstuvwx"  # Verified secret (Real)

# False Positive: Random string that might trigger entropy check
RANDOM_STRING_1 = "abc123efg456hij789klm012"  # False positive (Not a real secret)
RANDOM_STRING_2 = "YgTXrO95PJmQfRtLlN8H3yD4X7wvZK2A"  # False positive (Not a real secret)

# Unverified Secret: This might be a database connection string
DB_CONNECTION_STRING_1 = "mysql://user:password@localhost/db"  # Unverified (May be real or false)
DB_CONNECTION_STRING_2 = "postgresql://admin:pass@127.0.0.1/mydb"  # Unverified (May be real or false)

# Verified Secret: OAuth Token (Real secret)
OAUTH_TOKEN_1 = "ya29.A0ARrdaM_xxxxxyyyyyzzzzzz"  # Verified secret (Real)
OAUTH_TOKEN_2 = "ya29.C0B2EfGhJklMnOpQrStUvWxYz1234567890"  # Verified secret (Real)

# False Positive: This is a comment that might confuse scanners
COMMENT_1 = "The secret is not here, it's just a note."  # False positive (Not a real secret)
COMMENT_2 = "This string might look like a password: abcd1234."  # False positive (Not a real secret)

# More verified API keys
TWITTER_API_KEY = "AAAAAAAAAAAAAAAAAAAAA:ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"  # Verified secret (Real)
SLACK_TOKEN = "xoxb-1234567890-abcdefghij"  # Verified secret (Real)

# Additional unverified secrets
UNVERIFIED_KEY_1 = "token_test_A1B2C3D4E5F6G7H8I9J0"  # Unverified (May be real or false)
UNVERIFIED_KEY_2 = "secret_test_abcdefghijklmn123456789"  # Unverified (May be real or false)

# Even more false positives
FAKE_TOKEN_1 = "abcdefg-hijklmnop-qrstuv-wxyz123456789"  # False positive (Not a real secret)
FAKE_TOKEN_2 = "xyz12345-hijklmno-abcdef-890123456789"  # False positive (Not a real secret)

# Verified secrets to cover more cases
STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Verified secret (Real)
PAYPAL_SECRET = "AXxYoXlGnD_eV5js_YbZTlhzJMR7j-DohXu0oNdlYZ4"  # Verified secret (Real)

# More database connection strings to cover unverified secrets
DB_CONNECTION_STRING_3 = "mongodb://root:password@localhost:27017/dbname"  # Unverified (May be real or false)
DB_CONNECTION_STRING_4 = "sqlserver://username:password@localhost:1433;database=mydb"  # Unverified (May be real or false)

# More real AWS secrets
AWS_ACCESS_KEY_ID_3 = "AKIAIOSFODNN7EXAMPLE2"  # Verified secret (Real)
AWS_SECRET_ACCESS_KEY_3 = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY2"  # Verified secret (Real)

# False positives with numeric strings
NUMERIC_STRING_1 = "1111222233334444"  # False positive (Not a real secret)
NUMERIC_STRING_2 = "9876543210123456"  # False positive (Not a real secret)

# Verified Google API key
GOOGLE_API_KEY = "AIzaSyD-L1234567890abcdefghIJklMnOpQRs"  # Verified secret (Real)
