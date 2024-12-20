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
  if (data==1 || data==null || data==undefined || data.length==0) {
    alert('please select file');
  }
  else if (act=="decrypt" && (!(data.name.includes('.txt')))) {
    alert('encrypted file must be a text file')
  }
  else if (act=="default"||act==null||act==undefined) {
    alert('please select whether to encrypt or decrypt')
  }
    else if (pass.length<8 || pass.length>16) {
      alert('password must be 8 to 16 characters long');
    }
    else{
      const formData = new FormData();
      formData.append('file', data);
      formData.append('password', pass);
      formData.append('action', act);
      axios.post("http://localhost:3000/uploadfile",formData).then((res)=>{
        if (res.data.status=="wrong key") {
          alert('wrong key');
        }
        else if (res.data.status=="ok" && res.data.sent_file_name!="default") {
          window.location.href=("http://localhost:3000/downloadfile?down_file_name="+res.data.sent_file_name)
          
        }
        return res;
        
      })
      
     
      
      
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
