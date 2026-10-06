import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

const DealerDetail = ({ isLoggedIn }) => {
  const { id } = useParams();
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDealerAndReviews();
  }, [id]);

  const fetchDealerAndReviews = async () => {
    setLoading(true);
    try {
      const dealerRes = await fetch(`/api/dealers/${id}/`);
      if (dealerRes.ok) {
        const dealerData = await dealerRes.json();
        setDealer(dealerData);
      }

      const reviewsRes = await fetch(`/api/dealers/${id}/reviews/`);
      if (reviewsRes.ok) {
        const reviewsData = await reviewsRes.json();
        setReviews(reviewsData);
      }
    } catch (error) {
      console.error('Error fetching dealer detail:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '3rem' }}>Loading dealership details...</div>;
  }

  if (!dealer) {
    return (
      <div style={{ textAlign: 'center', padding: '3rem', background: 'white', borderRadius: '10px' }}>
        <h2>Dealership Not Found</h2>
        <Link to="/" className="btn-view" style={{ marginTop: '1rem' }}>Return to Dealerships</Link>
      </div>
    );
  }

  return (
    <div>
      <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', border: '1px solid var(--border)', marginBottom: '2rem' }}>
        <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap', alignItems: 'center' }}>
          <img
            src={dealer.image || 'https://images.unsplash.com/photo-1563720223185-11003d516935?w=800'}
            alt={dealer.name}
            style={{ width: '350px', height: '230px', objectFit: 'cover', borderRadius: '10px' }}
          />
          <div style={{ flex: 1, minWidth: '280px' }}>
            <span className="state-tag">{dealer.state}</span>
            <h1 style={{ color: 'var(--primary)', margin: '0.5rem 0' }}>{dealer.name}</h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '1rem', marginBottom: '0.75rem' }}>
              📍 {dealer.address}, {dealer.city}, {dealer.state} {dealer.zip}
            </p>
            <p style={{ color: 'var(--text-muted)', fontSize: '1rem', marginBottom: '0.75rem' }}>
              📞 <strong>Phone:</strong> {dealer.phone || 'N/A'}
            </p>
            {dealer.website && (
              <p style={{ color: 'var(--accent)', fontSize: '1rem', marginBottom: '1rem' }}>
                🌐 <strong>Website:</strong> <a href={dealer.website} target="_blank" rel="noreferrer" style={{ color: 'var(--accent)' }}>{dealer.website}</a>
              </p>
            )}
            <p style={{ color: '#334155', lineHeight: '1.6', marginBottom: '1.5rem' }}>{dealer.description}</p>
            
            {isLoggedIn ? (
              <Link to={`/postreview/${dealer.dealer_id || dealer.id}`} className="btn-view" style={{ background: '#10b981', padding: '0.75rem 1.5rem' }}>
                ✍️ Review Dealer
              </Link>
            ) : (
              <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
                <em>Log in to submit a review for this dealership.</em>
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="reviews-section">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
          <h2>Customer Reviews ({reviews.length})</h2>
          {isLoggedIn && (
            <Link to={`/postreview/${dealer.dealer_id || dealer.id}`} className="btn-view" style={{ background: '#10b981' }}>
              Add Review
            </Link>
          )}
        </div>

        {reviews.length === 0 ? (
          <div style={{ background: 'white', padding: '2rem', borderRadius: '10px', textAlign: 'center', color: 'var(--text-muted)' }}>
            No reviews yet for this dealership. Be the first to add one!
          </div>
        ) : (
          reviews.map((r, idx) => (
            <div key={r.id || idx} className="review-card">
              <div className="review-header">
                <div>
                  <strong style={{ fontSize: '1.1rem', color: 'var(--primary)' }}>{r.name || 'Anonymous Customer'}</strong>
                  {r.purchase_date && (
                    <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginLeft: '1rem' }}>
                      Purchased: {r.purchase_date}
                    </span>
                  )}
                </div>
                <span className={`badge-sentiment badge-${(r.sentiment || 'neutral').toLowerCase()}`}>
                  {r.sentiment || 'neutral'}
                </span>
              </div>
              <p style={{ color: '#334155', margin: '0.75rem 0', fontSize: '1rem', fontStyle: 'italic' }}>
                "{r.review}"
              </p>
              {(r.car_make || r.car_model) && (
                <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', background: '#f1f5f9', padding: '0.4rem 0.8rem', borderRadius: '6px', width: 'fit-content' }}>
                  🚘 Car: {r.car_year || ''} {r.car_make} {r.car_model}
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default DealerDetail;
