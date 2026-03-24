import dkim
from email.mime.text import MIMEText
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key  = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048
)

pem_bytes = private_key.private_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm = serialization.NoEncryption()
)

msg = MIMEText("This is a test message.")
msg["From"] = "sender@example.com"
msg["To"] = "recipient@example.com"
msg["Subject"] = "CIS Practical 5"

selector = b"myselector"
domain = b"example.com"
headers = [b"from", b"to", b"subject"]
signature = dkim.sign(
    message = msg.as_bytes(),
    selector = selector,
    domain = domain,
    privkey = pem_bytes,
    include_headers = headers
)

sig_value = signature.decode().split(":",1)[1].strip()
msg["DKIM-Signature"] = sig_value
print(msg.as_string())