import React, { useState } from "react";
import { motion } from "framer-motion";

const Header = ({ toggleTheme, isDarkMode }) => {
  return (
    <header className="header">
      <h1>EdBot</h1>
      <motion.button
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        onClick={toggleTheme}
        className="theme-toggle"
      >
        {isDarkMode ? "☀️ Light" : "🌙 Dark"}
      </motion.button>
    </header>
  );
};

export default Header;
