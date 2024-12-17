from flask import Flask,request,jsonify
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


app=Flask(__name__)


@app.route('/',methods=["POST"])
def handle_call():
    file_data =dict(request.get_json())
    global file_name 
    file_name=file_data["file_name"]
    global action
    action=file_data["action"]
    if(action=="encrypt"):
     encrypt_file(file_name)

    if(action=="decrypt"):
     decrypt_file(file_name)

    return jsonify({"gbr":0})

def encrypt_file(file_name):
   file_name=str(file_name)
   original_file_name="C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+file_name
   original_file = open(original_file_name,"rb")
   binary_data=original_file.read()
   original_file.close()
   string_binary_data=binary_data.hex()
   password = "password".encode()
   salt = b'\xe2\xaf\xbc:\xdd'
#    key1 = Fernet.generate_key()
#    f1 = Fernet(key1)
   kdf = PBKDF2HMAC(
       algorithm=hashes.SHA256(),
       length=32,
       salt=salt,
       iterations=390000,
   )
   key = base64.urlsafe_b64encode(kdf.derive(password))
   f = Fernet(key)
   token = f.encrypt(string_binary_data.encode())
  

   # b'...'
   flag=1
   try:
    new=(f.decrypt(token)).decode()
   except Exception:
    flag=0
    return "wrong key" #print("worng key")
   # b'Secret message!'

   encrypt_file_name="C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\enc_"+file_name
   if(flag):
     encrypted_file = open(encrypt_file_name,"wb")
     encrypted_file.write(bytes.fromhex(new))
     encrypted_file.close()
   

   
   pass
encrypt_file("hello.jpg")

def decrypt_file(file_name):
   
   pass



if(__name__=="__main__"):
    app.run(debug=True,port=4000)