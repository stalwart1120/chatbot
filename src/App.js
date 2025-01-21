import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  // Fetch messages from the backend when the component loads
  useEffect(() => {
    // Clear previous messages when the app starts
    setMessages([]);

    axios.get('http://localhost:3001/messages')
      .then((response) => {
        // Optionally fetch and display the messages from the database, if needed
        // setMessages(response.data);
      })
      .catch((error) => {
        console.error('Error fetching messages:', error);
      });
  }, []);

  // Handle form submission to send a message
  const handleSendMessage = (e) => {
    e.preventDefault();
    if (newMessage.trim() === '') return;

    // Send user message to backend
    axios.post('http://localhost:3001/messages', { message: newMessage })
      .then((response) => {
        const { userMessage, botReply } = response.data;

        // Update the messages state with both user and bot's messages
        setMessages([...messages, { content: userMessage, sender: 'user' }, { content: botReply, sender: 'bot' }]);
        setNewMessage('');
      })
      .catch((error) => {
        console.error('Error sending message:', error);
      });
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Chatbot</h1>
      <div style={styles.chatContainer}>
        {messages.map((msg, index) => (
          <div key={index} style={msg.sender === 'user' ? styles.userMessage : styles.botMessage}>
            <strong>{msg.sender}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <form onSubmit={handleSendMessage} style={styles.form}>
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type a message..."
          style={styles.input}
        />
        <button type="submit" style={styles.button}>Send</button>
      </form>
    </div>
  );
};

const styles = {
  container: {
    padding: '20px',
    fontFamily: 'Arial, sans-serif',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    backgroundColor: '#f0f4f8'
  },
  title: {
    fontSize: '2rem',
    marginBottom: '20px',
    color: '#4a90e2'
  },
  chatContainer: {
    border: '1px solid #ccc',
    borderRadius: '10px',
    padding: '15px',
    width: '100%',
    maxWidth: '600px',
    height: '400px',
    overflowY: 'scroll',
    backgroundColor: '#fff',
    boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
  },
  userMessage: {
    backgroundColor: '#e0f7fa',
    padding: '10px',
    borderRadius: '10px',
    marginBottom: '10px',
    alignSelf: 'flex-end',
    maxWidth: '70%',
  },
  botMessage: {
    backgroundColor: '#fff9c4',
    padding: '10px',
    borderRadius: '10px',
    marginBottom: '10px',
    alignSelf: 'flex-start',
    maxWidth: '70%',
  },
  form: {
    display: 'flex',
    marginTop: '15px',
    justifyContent: 'center',
    width: '100%',
    maxWidth: '600px',
  },
  input: {
    width: '80%',
    padding: '10px',
    fontSize: '16px',
    borderRadius: '20px',
    border: '1px solid #ccc',
    marginRight: '10px',
  },
  button: {
    padding: '10px 20px',
    fontSize: '16px',
    borderRadius: '20px',
    backgroundColor: '#4a90e2',
    color: '#fff',
    border: 'none',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
};

export default App;
