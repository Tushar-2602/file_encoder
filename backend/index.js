import express from 'express';
import axios from "axios";
import cors from "cors";
import bodyParser from 'body-parser';
import pkg from 'body-parser'
import fs from 'fs'
import multer from 'multer';
import 'dotenv/config'
import { log } from 'console';
const {json} = pkg;
const app = express()
const port = process.env.PORT;

app.use(cors({
  origin: process.env.CORS_ORIGIN,
  credentials:true
}));

app.use(bodyParser.json());
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './files')
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname)
  }
})

const upload = multer({ storage: storage })
app.post('/uploadfile',upload.single("file"), (req, res) =>{
  let order="oek"
  
  console.log(req.file);
  console.log(req.body.password);
  console.log(req.body.action);
  
  axios.post("http://127.0.0.1:4000",{
    "file_name":req.file.filename,
    "action":req.body.action,
    "password":req.body.password
}).then((resp)=>{order=resp.data.decrypting;
                return resp
}).then((resp)=>{console.log(order)
  //let str=resp.data.loaded_file_name

  console.log(resp.data.loaded_file_name);
  
  res.send({"status":order,"sent_file_name":resp.data.loaded_file_name})
})


})
app.get('/downloadfile', function(req, res) {
  const down_file_name=req.query.down_file_name
  res.download("C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+down_file_name,(err)=>{
   if(!err) fs.unlink("C:\\Users\\TUSHAR PC\\Desktop\\projects\\file_encoder\\backend\\files\\"+down_file_name,(err)=>{console.log(err);
  })
  
  })
  
  
  
  
})




app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})