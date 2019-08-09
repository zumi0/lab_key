import pandas as pd
import nfc
import id_detect

id_list = pd.read_csv('sids.csv').sid.tolist()

while True:
    clf = nfc.ContactlessFrontend('usb')
    try:
        clf.connect(rdwr={'on-connect': id_detect.CONNECTED})
    finally:
        clf.close()
    f = open('sid', 'r')
    if int(f.read()) in id_list:
        print("OK")
