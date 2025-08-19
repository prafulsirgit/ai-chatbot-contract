import React, { useRef, useEffect } from "react";
import Message from "./Message";

const ChatArea = ({ messages }) => {
  const chatRef = useRef(null);

  useEffect(() => {
    chatRef.current.scrollTop = chatRef.current.scrollHeight;
  }, [messages]);

  return (
    <div className="chat-area" ref={chatRef}>
      {messages.map((msg, index) => (
        <Message key={index} text={msg.text} isUser={msg.isUser} />
      ))}
    </div>
  );
};

export default ChatArea;
