import React from 'react';
import './Message.css';

const SuccessMessage = ({ message, onClose }) => {
  return (
    <div className="message success-message">
      <div className="message-content">
        <div className="message-icon">✅</div>
        <div className="message-text">
          <h4>Éxito</h4>
          <p>{message}</p>
        </div>
        <button className="message-close" onClick={onClose}>
          ×
        </button>
      </div>
    </div>
  );
};

export default SuccessMessage;
