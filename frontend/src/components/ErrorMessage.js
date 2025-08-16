import React from 'react';
import './Message.css';

const ErrorMessage = ({ message, onClose }) => {
  return (
    <div className="message error-message">
      <div className="message-content">
        <div className="message-icon">❌</div>
        <div className="message-text">
          <h4>Error</h4>
          <p>{message}</p>
        </div>
        <button className="message-close" onClick={onClose}>
          ×
        </button>
      </div>
    </div>
  );
};

export default ErrorMessage;
