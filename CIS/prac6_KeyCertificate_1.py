import os
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta, timezone

private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048
)

with open("server.key", "wb") as key_file:
    key_file.write(
        private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.NoEncryption()
        )
    )
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, 'localhost')
])

certificate = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.now(timezone.utc)
).not_valid_after(
    datetime.now(timezone.utc) + timedelta(days=365)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("localhost")]),
    critical = False
).sign(private_key, hashes.SHA256())

with open("server.crt", "wb") as cert_file:
    cert_file.write(certificate.public_bytes(serialization.Encoding.PEM))