# Sample Secrets File for TruffleHog and Gitleaks Testing

# =====================================
# Verified API Keys (Real and Real-Looking)
# =====================================
API_KEY_1 = "sk_live_51HxxxxxYYYYYYYYYxxxxZZZZZZZZZZZZ"  # Verified secret (Real)
API_KEY_2 = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"  # Verified secret (Real Stripe key)
API_KEY_3 = "AIzaSyD-KLMNOPQR1234567890StUvWxYz"  # Verified secret (Google API Key)
API_KEY_4 = "sk_prod_51ZZZyyyyyy8888xxxx3333zzzz0000"  # Verified secret (Real-looking)
API_KEY_5 = "sk_test_ABCD1234xyz6789abcdXYZ"  # Verified secret (Looks real)

# =====================================
# False Positive Passwords (Looks Like Secrets but Aren't)
# =====================================
FAKE_PASSWORD_1 = "super_secret_password"  # False positive (Fake)
FAKE_PASSWORD_2 = "notarealsecret123456789"  # False positive (Fake)
FAKE_PASSWORD_3 = "mypasswordisnotasecret"  # False positive (Fake)
FAKE_PASSWORD_4 = "admin1234"  # False positive (Fake but common pattern)
FAKE_PASSWORD_5 = "letmeinpls"  # False positive (Fake)

# =====================================
# Verified AWS Access Keys (Real)
# =====================================
AWS_ACCESS_KEY_ID_1 = "AKIAIOSFODNN7EXAMPLE"  # Verified secret (Real)
AWS_SECRET_ACCESS_KEY_1 = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Verified secret (Real)
AWS_ACCESS_KEY_ID_2 = "AKIAJHFLKJSLDKFJSLDKF"  # Verified secret (Looks real)
AWS_SECRET_ACCESS_KEY_2 = "xfjslskdf93wjl23WfjsdklDSK0sdflk3lSSJfd"  # Verified secret (Looks real)

# =====================================
# JWT Tokens (Real and Fake)
# =====================================
# Real JWT (Can be decoded for testing, do not use in production)
JWT_REAL_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
JWT_REAL_2 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiSm9obiIsImV4cCI6MTYzMjM4MjI5Nn0.xxxxxxxQssw5c"  # Partially real JWT for testing

# Fake JWT (Looks real but is not)
JWT_FAKE_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmYWtlX3VzZXIiOiJmYWtlIn0.qwertyuiopasdfghjklzxcvbnm123456"
JWT_FAKE_2 = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFlMmU4ZWVmNmY2YzNhODQ0ZDhiZDZhNTkwYjFiZmFlNGNmMmRlZjkifQ.FakeSign"

# =====================================
# SSH Private Keys (Fake and Real)
# =====================================
# Fake SSH Key (Not Real)
FAKE_SSH_PRIVATE_KEY_1 = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA0zgZZGJmP3v7Za3g/ptMQUUUSKd+9k5YwRLFBaxLnC+9RSKP
3fZfZr8KEZCxAy9Osn+VdY6YgScn8ViPiFWXX+x5xtTOc2xWmN+kOnUCY3PYPi+J
1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm=
-----END RSA PRIVATE KEY-----
"""

# Real-looking SSH Key (Not Real)
REAL_LOOKING_SSH_KEY_1 = """
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAUzIwMDAuMlNGU1FkZ2xhcjhwQUFFUGprcHJWUkJ5NTFu
bWFybG5tdjNtYXJlbHd3bW5vcg==
-----END OPENSSH PRIVATE KEY-----
"""

# =====================================
# OAuth Tokens (Real and Real-Looking)
# =====================================
OAUTH_TOKEN_1 = "ya29.A0ARrdaM_xxxxxyyyyyzzzzzz"  # Verified secret (Real OAuth token)
OAUTH_TOKEN_2 = "ya29.C0B2EfGhJklMnOpQrStUvWxYz1234567890"  # Verified secret (Real OAuth token)
OAUTH_TOKEN_3 = "ya29.FakeTokenWhichLooksRealButIsNot_1234567890"  # False positive (Fake OAuth token)

# =====================================
# Complex Secrets with High and Low Entropy (Hard to Detect)
# =====================================
LOW_ENTROPY_SECRET_1 = "abcdefghi12345"  # Unverified (Low entropy, may look fake)
LOW_ENTROPY_SECRET_2 = "A1B2C3D4E5F6"  # Unverified (Low entropy, may look fake but real)
LOW_ENTROPY_SECRET_3 = "abcdefghijklmno123456789"  # Unverified (May pass as a real key)

HIGH_ENTROPY_SECRET_1 = "YHdj9Df80sH09dfjsl38FJLSKFJjs09djf9FJfjs8Dfjs92slsfjKJd"  # Unverified (High entropy)
HIGH_ENTROPY_SECRET_2 = "23sd!fHsDF3@FJ4#Jfjs38dSJ3k*DFK2djfsl29"  # Unverified (May look real due to high entropy)
HIGH_ENTROPY_SECRET_3 = "skljdf03jf9DfJ8u3Qd93jfslf92e3FF23@!Fs9"  # Unverified (Hard to detect, real or fake?)

# =====================================
# Verified Database Connection Strings (Real)
# =====================================
DB_CONNECTION_STRING_1 = "postgresql://admin:realpassword@localhost/mydb"  # Verified secret (Real)
DB_CONNECTION_STRING_2 = "mongodb://user:password@remotehost:27017/database"  # Verified secret (Real)
DB_CONNECTION_STRING_3 = "mysql://admin:password@localhost:3306/mydatabase"  # Verified secret (Real)

# =====================================
# More Real-Looking API Keys (High and Low Entropy)
# =====================================
STRIPE_SECRET_KEY_1 = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Verified secret (Real Stripe key)
STRIPE_SECRET_KEY_2 = "sk_prod_51ZZZyyyyyy8888xxxx3333zzzz0000"  # Real-looking but fake
PAYPAL_SECRET_KEY_1 = "AXxYoXlGnD_eV5js_YbZTlhzJMR7j-DohXu0oNdlYZ4"  # Verified secret (Real PayPal key)
PAYPAL_SECRET_KEY_2 = "pyp_test_XXxxxxZZxxxxYY11223344"  # Real-looking but fake

# =====================================
# More AWS Keys (Real-Looking and Fake)
# =====================================
AWS_ACCESS_KEY_ID_3 = "AKIAIOWJKFJKDSFNJKZDFK"  # Verified secret (Looks real)
AWS_SECRET_ACCESS_KEY_3 = "A1234567890987654321abcdefgHIJKLMNopqrstuvwxyz12345678"  # Verified secret (Looks real)
AWS_ACCESS_KEY_ID_4 = "AKIAXYZABCDEFGHIJKLMNOPQ"  # Fake (Looks real)
AWS_SECRET_ACCESS_KEY_4 = "wjal2345XXXXXXYYYYZZZZ/abCdeFgHijKLmnOPQRSTUVWXYZ56789"  # Fake but real-looking

# =====================================
# Real-looking JWT Tokens (Fake and Real)
# =====================================
JWT_REAL_LOOKING_1 = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjE2YWFlYTJhYmU3ZTZmZjZkOGZiOTRkNzYxNzZlNmQifQ.1234abcd5678efgh9012ijklmnopqrstuvwx"  # Fake but real-looking JWT
JWT_REAL_LOOKING_2 = "eyJraWQiOiJrZXktaWQiLCJhbGciOiJSUzI1NiJ9.abcdEFGHIJKLMNOPQRST1234567890UVWXYZ"  # Fake JWT that looks real
JWT_REAL_LOOKING_3 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxlVXNlciIsImlhdCI6MTUxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"  # Real JWT

# =====================================
# Complex OAuth Tokens (Fake and Real)
# =====================================
OAUTH_TOKEN_COMPLEX_1 = "ya29.ABcDefGhIjKlMnOpQRsTUVwXyZ1234567890abcdefghijklmnopqrstu"  # Verified secret (Looks real)
OAUTH_TOKEN_COMPLEX_2 = "ya29.RealLookingButFake-XYZ1234567abcdefgh"  # Fake but real-looking OAuth token

# =====================================
# More False Positives (Tricky to Detect)
# =====================================
FAKE_TOKEN_COMPLEX_1 = "notARealSecretKey_1234567890abcdef"  # False positive (Looks real)
FAKE_TOKEN_COMPLEX_2 = "thisIsJustARandomStringForTesting_12345"  # False positive (Fake secret)

