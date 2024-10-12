import React, { useState, useEffect } from 'react';
import api from '../api';
import '../styles/Chat.css';

const ChatApp = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  useEffect(() => {
    // Fetch messages when the component mounts
    api.get('chat/messages/')
      .then(response => {
        setMessages(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the messages!', error);
      });
  }, []);

  const handleSendMessage = () => {
    if (!newMessage.trim()) return; // Don't send empty messages

    api.post('chat/messages/', { user_message: newMessage })
      .then(response => {
        setMessages([response.data, ...messages]); // Add new message to the state
        setNewMessage(''); // Clear the input field
      })
      .catch(error => {
        console.error('Error sending message:', error);
      });
  };

  return (
    <div className="chat-container">
      <div className="chat-history">
        {messages.map((msg, index) => (
          <div key={index} className="chat-message">
            <p><strong>User:</strong> {msg.user_message}</p>
            <p><strong>Bot:</strong> {msg.bot_response}</p>
          </div>
        ))}
      </div>

      <div className="chat-input">
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatApp;
