import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navbar = ({ isLoggedIn, username, onLogout }) => {
  const location = useLocation();

  return (
    <header className="nav-header">
      <Link to="/" className="brand-link">
        🚗 Cars Dealership
      </Link>
      <nav className="nav-links">
        <Link to="/" className={`nav-item ${location.pathname === '/' ? 'active' : ''}`}>
          Home / Dealerships
        </Link>
        <a href="/About.html" className="nav-item">
          About Us
        </a>
        <a href="/Contact.html" className="nav-item">
          Contact Us
        </a>

        {isLoggedIn ? (
          <>
            <span className="user-badge">👤 Welcome, {username}</span>
            <Link to="/logout" className="btn-logout">
              Logout
            </Link>
          </>
        ) : (
          <>
            <Link to="/login" className={`nav-item ${location.pathname === '/login' ? 'active' : ''}`}>
              Login
            </Link>
            <Link to="/register" className={`nav-item ${location.pathname === '/register' ? 'active' : ''}`}>
              Register
            </Link>
          </>
        )}
      </nav>
    </header>
  );
};

export default Navbar;
