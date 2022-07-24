import React from 'react';
import { useState, useEffect } from "react";
import io from 'socket.io-client';

function Provider() {
    const socket = io.connect("http://127.0.0.1:6001");
    const [messages, setMessages] = useState([]);
    
    useEffect(() => {
        getMessages();
    }, [messages.length]);
    
    const getMessages = () => {
        socket.on("receive_message", msg => {
        setMessages(oldMessages => [...oldMessages, msg]);
    });
    return messages;
};

export default Provider;