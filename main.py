import nfc

def CONNECTED(tag):
    servc = 0x100B
    service_code = [nfc.tag.tt3.ServiceCode(servc >> 6, servc & 0x3f)]
    # bc_id -> student ID
    bc_id = [nfc.tag.tt3.BlockCode(i) for i in range(3)]
    print(tag.read_without_encryption(service_code, bc_id)[14:23].decode())
    return False

while True:
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': CONNECTED})
    clf.close()
