import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Dealers from './components/Dealers/Dealers';
import DealerDetail from './components/Dealer/DealerDetail';
import Register from './components/Register/Register';
import Login from './components/Login/Login';
import Logout from './components/Logout/Logout';
import AddReview from './components/Review/AddReview';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');

  useEffect(() => {
    checkUserStatus();
  }, []);

  const checkUserStatus = async () => {
    try {
      const res = await fetch('/api/user/');
      const data = await res.json();
      if (data.is_authenticated) {
        setIsLoggedIn(true);
        setUsername(data.username);
      }
    } catch (e) {
      console.error('Failed to check user status:', e);
    }
  };

  const handleLoginSuccess = (user) => {
    setIsLoggedIn(true);
    setUsername(user);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setUsername('');
  };

  return (
    <Router>
      <div className="app-container">
        <Navbar isLoggedIn={isLoggedIn} username={username} onLogout={handleLogout} />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dealers isLoggedIn={isLoggedIn} username={username} />} />
            <Route path="/dealer/:id" element={<DealerDetail isLoggedIn={isLoggedIn} />} />
            <Route path="/postreview/:id" element={isLoggedIn ? <AddReview username={username} /> : <Navigate to="/login" />} />
            <Route path="/register" element={<Register onLoginSuccess={handleLoginSuccess} />} />
            <Route path="/login" element={<Login onLoginSuccess={handleLoginSuccess} />} />
            <Route path="/logout" element={<Logout onLogout={handleLogout} />} />
          </Routes>
        </main>
        <footer>
          <p>&copy; 2026 Cars Dealership National Inc. All rights reserved. | Coursera / IBM Full-Stack Capstone Project</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
