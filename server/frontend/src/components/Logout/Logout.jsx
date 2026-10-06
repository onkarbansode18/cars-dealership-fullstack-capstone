import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = ({ onLogout }) => {
  const navigate = useNavigate();

  useEffect(() => {
    const performLogout = async () => {
      try {
        await fetch('/api/logout/', { method: 'POST' });
      } catch (e) {
        console.error(e);
      }
      onLogout();
      navigate('/');
    };
    performLogout();
  }, [onLogout, navigate]);

  return (
    <div style={{ textAlign: 'center', margin: '4rem auto' }}>
      <h2>Logging out...</h2>
    </div>
  );
};

export default Logout;
