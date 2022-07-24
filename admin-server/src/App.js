import './App.css'
import React from 'react';
import { useState, useEffect } from "react";
import io from 'socket.io-client';

const socket = io.connect("http://127.0.0.1:6001");

function App() {
  const [messages, setMessages] = useState([]);
  
  useEffect(() => {
      getMessages();
  }, [messages.length]);
  
  const getMessages = () => {
    socket.on("receive_message", msg => {
      setMessages([...messages, msg]);
    });
  };

  return (
    <div className='container'>
      <div className='header'>
        <h1>end_user_id</h1>
        <h1>wep_page_url</h1>
      </div>
      <div className='body'>
      {messages.length > 0 && messages.map(msg => (
          <div className='body-items'>
            <p>{msg.end_user_id}</p>
            <p>{msg.web_page_url}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
