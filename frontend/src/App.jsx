import { useEffect, useState } from "react"
import axios from "axios";
function App() {
const [act,setact]=useState("default");
const [disb,setdisb]=useState(false);
const [pass,setpass]=useState("");
const [data,setdata]=useState(1);
useEffect(()=>{
  if (act=="default") {
    setdisb(true)
  }
  if (act!="default") setdisb(false)
},[act]);
function sending() {
  if (data==1) {
    alert('please select file');
  }
  else if (act=="decrypt" && (!(data.name.includes('.txt')))) {
    alert('encrypted file must be a text file')
  }
    else if (pass.length<8 || pass.length>16) {
      alert('password must be 8 to 16 characters long');
    }
    else{
      // const user_data={
      //   "password":pass,
      //   "action":act
      // }
      //console.log(data.name);
      
      const formData = new FormData();
      formData.append('file', data);
      formData.append('password', pass);
      formData.append('action', act);
      axios.post("http://localhost:3000/uploadfile",formData).then((res)=>{
        // alert("wrong key")
        console.log(res.data.status);
        console.log(res.data.sent_file_name);
        if (res.data.status=="wrong key") {
          alert('wrong key');
        }
        
      }).then
      // axios.post("http://localhost:3000/uploaddata",user_data);
      console.log(formData);
      
      
    }
}
  return (
    <>
    <form className="absolute left-[40%] top-[20%]" method="post" action="http://localhost:3000/">
      <input type="radio" name="rg1" id="enc" className="m-1" value="encrypt" onFocus={(e)=>setact("encrypt")}/>
      <label htmlFor="">Encrypt</label><br />
      <input type="radio" name="rg1" id="dec" className="m-1" value="decrypt" onFocus={(e)=>setact("decrypt")}/>
      
      <label htmlFor="">Decrypt</label><br />
      <input type="file" name="encrypt" id="fileip" disabled={disb} onChange={(e)=>{setdata(e.target.files[0])}} /><br />
      <input type="password" name="" id="" className="m-5 border-2 border-sky-500 " placeholder="password" onChange={(e)=>setpass(e.target.value)}/> <br />
      <button type="button" className="m-5 border-2 border-sky-500 cursor-pointer" onClick={sending}> submit</button>


    </form>
       
    </>
  )
}

export default App
