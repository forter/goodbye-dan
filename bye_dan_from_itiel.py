import base64
import hashlib
from subprocess import call
import time
import sys

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

print "Hi Dan, This is a (very) basic task. \nFind the key and you shall achieve great things!"

very_secret_msg = 'utjW0dfnyZOtyNuVm4TM2NyN3c_a2Im-3OM='
count = 0
while True:
    key = raw_input("Please enter the key: ").lower()
    hash_object = hashlib.md5(key.encode())
    if hash_object.hexdigest()!="4d77409e1e21dd90a19a47ae5681be11":
        if count == 0 :
            print "You are Wrong... so ill give you an hint\nThis is a very big project you worked on"
            count += 1
        elif count == 1:
            print "The answer is Not velocity!"
            count += 1
        elif count==2:
            print "No more hints for you."
            count += 1
        else:
            print "You have failed - goodbye, Also im killing myself"
            time.sleep(2)
            call(["rm", sys.argv[0]])
            break
    else:
        print decode(key,very_secret_msg)
        print "Also No Great things - your in the army now"
        break
