import { useState,useEffect,useRef } from "react"
import axios from 'axios';
import MessageBubble from "../Components/MessageBubble";

const BACKEND_URL=import.meta.env.VITE_BACKEND_URL;

const Home = () => {
  const [queryText,setQueryText]=useState('');
  const [messages,setMessages]=useState([]);
  const [isLoading,setIsLoading]=useState(false);
  const [faqList,setFaqList]=useState([]);
  const messagesEndRef = useRef(null);


  const handleAskClick=()=>{
    if(!queryText) return
    setIsLoading(true);
    const newUserQuery=[...messages,{role:'user',text:queryText}]
    setMessages(newUserQuery)
    setQueryText("")
    axios.get(`${BACKEND_URL}/api/ask/?question=${queryText}`).then(res=>{setMessages(prev=>[...prev,{role:"bot",text:res.data.answer}]);setIsLoading(false)})
  }

  const handleFAQClick=(ques)=>{
    setIsLoading(true);
    const newUserQuery=[...messages,{role:'user',text:ques}]
    setMessages(newUserQuery)
    setQueryText("")
    axios.get(`http://localhost:8000/api/ask/?question=${ques}`).then(res=>{setMessages(prev=>[...prev,{role:"bot",text:res.data.answer}]);setIsLoading(false)})
  }
  const handleKeyDown=(e)=>{
    if(e.key!=='Enter'||!queryText) return
    handleAskClick()
  }

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading])

  useEffect(() => {
    axios.get(`http://localhost:8000/api/get_faq/`).then(res=>{setFaqList(res.data);})
  }, [])
 
  return (
    <div className="bg-gray-500 flex items-center justify-center h-screen">
      <div className="w-[500px]  bg-white rounded p-5">
      <h4 className="font-bold text-xl">ChatBot</h4>
      <div className="h-max-[500px] h-[500px] overflow-y-auto">
        <div>
          <h4>Some Frequently Asked Question</h4>
          {faqList.map((ques)=><li key={ques.id} className="hover:text-blue-500 cursor-pointer" onClick={()=>{handleFAQClick(ques.question)}}>{ques.question}</li>)}
        </div>
      <div className="messages space-y-2">
        {messages.map((msg, index) => (
          <MessageBubble key={index} role={msg.role} text={msg.text} />
        ))}
          {isLoading && <MessageBubble role="bot" text="loading" />}

        <div ref={messagesEndRef} />
      </div>
      </div>
      <div className="flex gap-x-2">
      <input type="text" className="border border-black-2 rounded p-2 w-full" onChange={(e)=>setQueryText(e.target.value)} value={queryText} onKeyDown={handleKeyDown} disabled={isLoading}/>
      <button className="bg-blue-500 px-2 py-1 rounded w-20 text-white" onClick={handleAskClick} disabled={isLoading}>Ask</button>
      </div>
      </div>
    </div>
  )
}

export default Home
