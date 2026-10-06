import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

const AddReview = ({ username }) => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [dealer, setDealer] = useState(null);
  const [cars, setCars] = useState([]);
  
  const [formData, setFormData] = useState({
    name: username || 'Test User',
    review: 'Fantastic services',
    purchase: true,
    purchase_date: '2026-03-01',
    car_make: 'Toyota',
    car_model: 'RAV4',
    car_year: 2025
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [sentimentPreview, setSentimentPreview] = useState('positive');

  useEffect(() => {
    fetchDealerAndCars();
  }, [id]);

  const fetchDealerAndCars = async () => {
    try {
      const dealerRes = await fetch(`/api/dealers/${id}/`);
      if (dealerRes.ok) {
        const dealerData = await dealerRes.json();
        setDealer(dealerData);
      }

      const carsRes = await fetch('/api/cars/');
      if (carsRes.ok) {
        const carsData = await carsRes.json();
        setCars(carsData);
      }
    } catch (err) {
      console.error('Error fetching data:', err);
    }
  };

  const handleChange = async (e) => {
    const { name, value, type, checked } = e.target;
    const newVal = type === 'checkbox' ? checked : value;
    const updatedData = { ...formData, [name]: newVal };
    setFormData(updatedData);

    if (name === 'review' && value.trim().length > 3) {
      try {
        const res = await fetch('/api/analyze-review/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: value })
        });
        const resData = await res.json();
        if (resData.sentiment) {
          setSentimentPreview(resData.sentiment);
        }
      } catch (err) {
        console.error(err);
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await fetch(`/api/dealers/${id}/add_review/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          name: username || formData.name || 'Anonymous User'
        })
      });

      if (response.ok) {
        navigate(`/dealer/${id}`);
      } else {
        const data = await response.json();
        setError(data.error || 'Failed to submit review.');
      }
    } catch (err) {
      setError('Error connecting to the server.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-card" style={{ maxWidth: '650px' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '0.5rem', color: 'var(--primary)' }}>
        Submit Review for {dealer ? dealer.name : `Dealer #${id}`}
      </h2>
      <p style={{ textAlign: 'center', color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
        Share your purchase and service experience with our national customer community.
      </p>

      {error && <div style={{ color: '#dc2626', background: '#fee2e2', padding: '0.75rem', borderRadius: '8px', marginBottom: '1rem' }}>{error}</div>}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="review">Review Comment</label>
          <textarea
            id="review"
            name="review"
            rows="4"
            value={formData.review}
            onChange={handleChange}
            placeholder="Type your honest review here..."
            required
          ></textarea>
        </div>

        {formData.review && (
          <div style={{ marginBottom: '1rem', background: '#f8fafc', padding: '0.75rem', borderRadius: '8px', border: '1px solid var(--border)' }}>
            <strong>Live Sentiment Analysis Preview: </strong>
            <span className={`badge-sentiment badge-${sentimentPreview}`}>
              {sentimentPreview}
            </span>
          </div>
        )}

        <div className="form-group" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <input
            type="checkbox"
            id="purchase"
            name="purchase"
            checked={formData.purchase}
            onChange={handleChange}
            style={{ width: 'auto' }}
          />
          <label htmlFor="purchase" style={{ margin: 0 }}>Did you purchase a car from this dealer?</label>
        </div>

        {formData.purchase && (
          <>
            <div className="form-group">
              <label htmlFor="purchase_date">Purchase Date</label>
              <input
                type="date"
                id="purchase_date"
                name="purchase_date"
                value={formData.purchase_date}
                onChange={handleChange}
              />
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
              <div className="form-group">
                <label htmlFor="car_make">Car Make</label>
                <select id="car_make" name="car_make" value={formData.car_make} onChange={handleChange}>
                  <option value="Toyota">Toyota</option>
                  <option value="Honda">Honda</option>
                  <option value="Ford">Ford</option>
                  <option value="Chevrolet">Chevrolet</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="car_model">Car Model</label>
                <select id="car_model" name="car_model" value={formData.car_model} onChange={handleChange}>
                  <option value="RAV4">RAV4</option>
                  <option value="Camry">Camry</option>
                  <option value="Civic">Civic</option>
                  <option value="CR-V">CR-V</option>
                  <option value="F-150">F-150</option>
                  <option value="Tahoe">Tahoe</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="car_year">Car Year</label>
                <input
                  type="number"
                  id="car_year"
                  name="car_year"
                  value={formData.car_year}
                  onChange={handleChange}
                  min="2000"
                  max="2026"
                />
              </div>
            </div>
          </>
        )}

        <button type="submit" className="btn-submit" disabled={loading}>
          {loading ? 'Submitting Review...' : 'Submit Review'}
        </button>
      </form>
    </div>
  );
};

export default AddReview;
