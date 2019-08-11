# This script is one part of on-connect function.
# It is for detecting student ID
import nfc

def DETECT_SID(tag):
    servc = 0x100B
    service_code = [nfc.tag.tt3.ServiceCode(servc >> 6, servc & 0x3f)]
    # bc_id -> student ID
    bc_id = [nfc.tag.tt3.BlockCode(i) for i in range(3)]
    with open('./id', mode='w') as f:
        f.write(tag.read_without_encryption(service_code, bc_id)[14:23].decode())
        return False
