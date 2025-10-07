import React, { useState } from "react";
import { motion } from "framer-motion";

const InputBar = ({ onSend }) => {
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      onSend(input);
      setInput("");
      setIsTyping(false);
    }
  };

  return (
    <form className="input-bar" onSubmit={handleSubmit}>
      <textarea
        value={input}
        onChange={(e) => {
          setInput(e.target.value);
          setIsTyping(e.target.value.length > 0);
        }}
        placeholder="Ask EdBot anything..."
        className="input-text"
      />
      <motion.button
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        type="submit"
        className="send-button"
        animate={{ opacity: isTyping ? 1 : 0.7 }}
      >
        ↑
      </motion.button>
    </form>
  );
};

export default InputBar;
