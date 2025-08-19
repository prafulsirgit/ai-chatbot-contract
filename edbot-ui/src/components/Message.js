import React from "react";
import { motion } from "framer-motion";

const Message = ({ text, isUser }) => {
  return (
    <motion.div
      className={`message ${isUser ? "user" : "bot"}`}
      initial={{ opacity: 0, y: 20, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
    >
      <p>{text}</p>
    </motion.div>
  );
};

export default Message;
