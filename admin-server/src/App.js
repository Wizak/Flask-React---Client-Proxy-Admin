import React, { useState, useEffect } from "react";
import io from "socket.io-client";

const socket = io.connect("http://127.0.0.1:6001");

function App() {
  const [messages, setMessages] = useState([""]);

  useEffect(() => {
    getMessages();
  }, [messages.length]);

  const getMessages = () => {
    socket.on("receive_id", msg => {
      //   let allMessages = messages;
      //   allMessages.push(msg);
      //   setMessages(allMessages);
      // console.log(msg.end_user_id)
      setMessages([...messages, msg]);
    });
    socket.on("receive_url", msg => {
      //   let allMessages = messages;
      //   allMessages.push(msg);
      //   setMessages(allMessages);
      // console.log(msg.end_user_id)
      setMessages([...messages, msg]);
    });
  };

  return (
    <div>
      {messages.length > 0 &&
        messages.map(msg => (
          <div>
            <br></br>
            {msg}
          </div>
        ))}
    </div>
  );
};

export default App;
