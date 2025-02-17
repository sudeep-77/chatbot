/* eslint-disable react/prop-types */
import Spinner from "../Spinner";



const MessageBubble = ({ role, text }) => {
  return (
    <div className={`flex ${role=='user'?'justify-end':'justify-start'}`}>
    <div className={`w-fit w-max-[70%] p-2.5 rounded ${role==='user'?'bg-blue-200':'bg-gray-200'}`}>
     {text=='loading'?<Spinner />:<p>{text}</p>} 
    </div>
    </div>
  );
};

export default MessageBubble;
