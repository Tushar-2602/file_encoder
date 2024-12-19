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
   #  global file_name 
    file_name=file_data["file_name"]
   #  global action
    action=file_data["action"]
   #  global password
    password = file_data["password"]
    status="ok"
    if(action=="encrypt"):
     encrypt_file(file_name,password)

    if(action=="decrypt"):
     status=decrypt_file(file_name,password)

    print(file_name," ",action," ",password)
    return jsonify({"decrypting":status})

def encrypt_file(file_name,password):
   file_name=str(file_name)
   original_file_name="C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+file_name
   original_file = open(original_file_name,"rb")
   binary_data=original_file.read()
   original_file.close()
   string_binary_data=binary_data.hex()
   pswd = password.encode()
   salt = b'\xe2\xaf\xbc:\xdd'
#    key1 = Fernet.generate_key()
#    f1 = Fernet(key1)
   kdf = PBKDF2HMAC(
       algorithm=hashes.SHA256(),
       length=32,
       salt=salt,
       iterations=390000,
   )
   key = base64.urlsafe_b64encode(kdf.derive(pswd))
   f = Fernet(key)
   token = f.encrypt(string_binary_data.encode())
   
   # b'...'
   # flag=1
   # try:
   #  new=(f.decrypt(token)).decode()
   # except Exception:
   #  flag=0
   #  return "wrong key" #print("worng key")
   # b'Secret message!'
   ext=""
   while(1):
    n=file_name[-1]
    file_name=file_name[:-1]
    ext+=n
    if(n=='.'):
      break
  
   ext=''.join(reversed(ext))
   encrypt_file_name="C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+file_name+".txt"
   # if(flag):
   encrypted_file = open(encrypt_file_name,"w")
   encrypted_file.write((token.decode()+ext))
   encrypted_file.close()
   os.remove(original_file_name)
   

   
   pass


def decrypt_file(file_name,password):
   file_name=str(file_name)
   original_file_name="C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+file_name
   original_file = open(original_file_name,"r")
   text_data=original_file.read()
   original_file.close()
   file_name=file_name[:-4]
   ext=""
   while(1):
      n=text_data[-1]
      text_data=text_data[:-1]
      ext+=n
      if(n=='.'):
         break
   ext=''.join(reversed(ext))
   pswd = password.encode()
   salt = b'\xe2\xaf\xbc:\xdd'
#    key1 = Fernet.generate_key()
#    f1 = Fernet(key1)
   kdf = PBKDF2HMAC(
       algorithm=hashes.SHA256(),
       length=32,
       salt=salt,
       iterations=390000,
   )
   key = base64.urlsafe_b64encode(kdf.derive(pswd))
   f = Fernet(key)
   flag=1
   try:
    string_data_in_hex=(f.decrypt(text_data.encode())).decode()
   except Exception:
    flag=0
    os.remove(original_file_name)
    return "wrong key" #print("worng key")
   
   if(flag):
    decrypt_file_name="C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+file_name+ext
    decrypted_file = open(decrypt_file_name,"wb")
    decrypted_file.write(bytes.fromhex(string_data_in_hex))
    decrypted_file.close()
    os.remove(original_file_name)
    return "ok"
   
    
#encrypt_file("hello.jpg","passsword")
#decrypt_file("hello.txt","passsword")

    
      



if(__name__=="__main__"):
    app.run(debug=True,port=4000)