import express from 'express';
import axios from "axios";
import cors from "cors";
import bodyParser from 'body-parser';
import pkg from 'body-parser'
import multer from 'multer';
import 'dotenv/config'
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
let order="oek"
app.post('/uploadfile',upload.single("file"), (req, res) =>{
  
  console.log(req.file);
  console.log(req.body.password);
  console.log(req.body.action);
  
  axios.post("http://127.0.0.1:4000",{
    "file_name":req.file.filename,
    "action":req.body.action,
    "password":req.body.password
}).then((resp)=>{order=resp.data.decrypting;
}).then((resp)=>{console.log(order)
   
  res.send({"status":order})
})


})
// app.post('/uploaddata',(req,res)=> {
//   const  password = req.body.password;

// })


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})