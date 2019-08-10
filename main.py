import csv
import nfc
import id_detect
import servo

with open("sids.csv", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    id_list = []
    for row in csv_obj:
        id_list.append(row[0])

while True:
    clf = nfc.ContactlessFrontend('usb')
    try:
        clf.connect(rdwr={'on-connect': id_detect.CONNECTED})
    finally:
        clf.close()
    f = open('sid', 'r')
    if f.read() in id_list:
        print("OK")
        servo.servo()
    f.close()
