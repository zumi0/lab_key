# This script is one part of on-connect function.
# It is for detecting Suica
import nfc
import binascii

def DETECT_Suica(tag):
    with open('./id', mode='w') as f:
        f.write(binascii.hexlify(tag.idm).decode())
        return False
