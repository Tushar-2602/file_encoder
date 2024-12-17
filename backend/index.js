import express from 'express';
import cors from "cors";
import bodyParser from 'body-parser';
import multer from 'multer';
import 'dotenv/config'
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
app.post('/uploadfile',upload.single("file"), (req, res) => {
  
  console.log(req.file);

})
app.post('/uploaddata',(req,res)=> {
  const  password = req.body.password;

})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})