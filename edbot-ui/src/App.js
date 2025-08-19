import React, { useState } from "react";
import Header from "./components/Header";
import ChatArea from "./components/ChatArea";
import InputBar from "./components/InputBar";
import axios from "axios";
import "./styles.css";

const App = () => {
  const [messages, setMessages] = useState([]);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
    document.body.classList.toggle("dark-mode");
  };

  const handleSend = async (text) => {
    const userMessage = { text, isUser: true };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post("http://localhost:5000/api/chat", {
        message: text,
      });
      const botMessage = { text: response.data.reply, isUser: false };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error:", error);
      const errorMessage = {
        text: "Sorry, something went wrong.",
        isUser: false,
      };
      setMessages((prev) => [...prev, errorMessage]);
    }
  };

  return (
    <div className="chatbot-container">
      <Header toggleTheme={toggleTheme} isDarkMode={isDarkMode} />
      <ChatArea messages={messages} />
      <InputBar onSend={handleSend} />
    </div>
  );
};

export default App;
