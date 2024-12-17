# from flask import Flask,request,jsonify

# app=Flask(__name__)


# @app.route('/',methods=["POST"])
# def handle_call():
#     file_data =dict(request.get_json())
#     global file_name 
#     file_name=file_data["file_name"]
#     global action
#     action=file_data["action"]
#     if(action=="encrypt"):
#      encrypt_file(file_name)

#     if(action=="decrypt"):
#      decrypt_file(file_name)

#     return jsonify({"gbr":0})

def encrypt_file(file_name):
   file_name=str(file_name)
   original_file_name="C:\\Users\\TUSHAR PC\\Desktop\projects\\file_encoder\\backend\\files\\"+file_name
   original_file = open(original_file_name,"rb")
   binary_data=original_file.read()
   original_file.close()
   string_binary_data=binary_data.hex()

   print(string_binary_data)
   encrypt_file_name="C:\\Users\\TUSHAR PC\\Desktop\projects\\file_encoder\\backend\\files\\enc_"+file_name
   encrypted_file = open(encrypt_file_name,"wb")
   new_binary_data=(string_binary_data.encode())
   encrypted_file.write(bytes.fromhex(string_binary_data))
   encrypted_file.close()

   
   pass
encrypt_file("hello.jpg")

def decrypt_file(file_name):
   
   pass


# print(file_name)
# if(__name__=="__main__"):
#     app.run(debug=True,port=4000)