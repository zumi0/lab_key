import nfc
import detect_sid as sid
import detect_suica as suica

def CONNECTED(tag):
    if tag.sys == 3:
        suica.DETECT_Suica(tag)
    elif tag.sys == 35096:
        sid.DETECT_SID(tag)
