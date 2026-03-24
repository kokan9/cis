import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random

import xml.etree.ElementTree as ET

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    b = pad(plain_text.encode("UTF-8", "ignore"), AES.block_size)
    return base64.b64encode(cipher.iv + cipher.encrypt(b))

def decrypt(enc_text, key):
    enc_text = base64.b64decode(enc_text)
    iv = enc_text[:AES.block_size]
    enc_text = enc_text[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    b = unpad(cipher.decrypt(enc_text), AES.block_size)
    return b.decode("UTF-8", "ignore")

key = Random.get_random_bytes(16)
plain_text = "This is the secret text to encrypt"

print("Key: ", base64.b64encode(key))
print("plain_text: ", plain_text)

try:
    tree = ET.parse('msg.xml')
    root = tree.getroot()

    for msg in root.iter('msg'):
        enc_msg = encrypt(msg.text, key)
        msg.text = enc_msg.decode("UTF-8")
        msg.set('encryption', 'AES-128 CBC')
    
    tree.write("encrypted_msg.xml")
    print("Encrypted messages stored in encrypted_msg.xml")

    tree = ET.parse("encrypted_msg.xml")
    root = tree.getroot()

    for msg in root.iter('msg'):
        dec_msg = decrypt(msg.text, key)
        msg.text = str(dec_msg)

    tree.write("decrypted_msg.xml")
    print("Decrypted messages stored in decrypted_msg.xml")

except(ValueError,KeyError):
    print("Error occured")
        

