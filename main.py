import csv
import nfc
import connected
#import servo

with open("ids.csv", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    id_list = []
    for row in csv_obj:
        id_list.append(row[0])

rdwr_options = {
    'targets': ['212F' , '424F'],
    'on-connect': connected.CONNECTED
}

while True:
    clf = nfc.ContactlessFrontend('usb')
    try:
        clf.connect(rdwr=rdwr_options)
    finally:
        clf.close()
    f = open('id', 'r')
    if f.read() in id_list:
        print("OK")
        #servo.servo()
    f.close()
