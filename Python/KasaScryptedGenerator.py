"""
Kasa Camera FFmpeg Input Stream Argument Generator
"""

import base64
email = input("Enter Email: ")
pw = input("Enter PW: ")
ipaddr = input("Enter Camera IP Address: ")

def bencode(string):
    pw_encode = string.encode("UTF-8")
    b64_1 = base64.b64encode(pw_encode)
    return b64_1.decode()
pw2 = f'{email}:{bencode(pw)}'

b64_2 = bencode(pw2)

#print(f"B64: {b64_1} \nB64 2: {b64_2}")
print(str(b64_2))

print(f"""Please enter the following to Scrypted FFmpeg Input Stream Arguments, adjust as needed:\n 
      -headers \"Authorization: Basic {str(b64_2)}\" -f h264 -i https://{ipaddr}:19443/https/stream/mixed?video=h264&audio=g711&resolution=hd""")

