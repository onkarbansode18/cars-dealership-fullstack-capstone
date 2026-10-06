import React, { useState, useEffect } from 'react';
import { Link, useSearchParams } from 'react-router-dom';

const Dealers = ({ isLoggedIn, username }) => {
  const [dealers, setDealers] = useState([]);
  const [states, setStates] = useState([]);
  const [searchParams, setSearchParams] = useSearchParams();
  const selectedState = searchParams.get('state') || 'All';
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDealers(selectedState);
  }, [selectedState]);

  const fetchDealers = async (stateFilter) => {
    setLoading(true);
    try {
      let url = '/api/dealers/';
      if (stateFilter && stateFilter !== 'All') {
        url += `?state=${encodeURIComponent(stateFilter)}`;
      }
      const response = await fetch(url);
      const data = await response.json();
      setDealers(data);

      if (states.length === 0 && (!stateFilter || stateFilter === 'All')) {
        const allRes = await fetch('/api/dealers/');
        const allData = await allRes.json();
        const uniqueStates = Array.from(new Set(allData.map(d => d.state))).sort();
        setStates(uniqueStates);
      }
    } catch (error) {
      console.error('Error fetching dealers:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleStateChange = (e) => {
    const val = e.target.value;
    if (val === 'All') {
      setSearchParams({});
    } else {
      setSearchParams({ state: val });
    }
  };

  return (
    <div>
      <section className="hero">
        <h1>National Cars Dealership Network</h1>
        <p>Explore top rated car dealerships across the United States. Filter by state or view detailed inventory and customer reviews.</p>
      </section>

      <div className="filter-bar">
        <label htmlFor="state-select" style={{ fontWeight: '600' }}>Filter by State:</label>
        <select
          id="state-select"
          className="filter-select"
          value={selectedState}
          onChange={handleStateChange}
        >
          <option value="All">All States</option>
          {states.map(s => (
            <option key={s} value={s}>{s}</option>
          ))}
          {!states.includes('Kansas') && <option value="Kansas">Kansas</option>}
        </select>
        {selectedState !== 'All' && (
          <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
            Showing results for <strong>{selectedState}</strong> ({dealers.length} found)
          </span>
        )}
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '3rem' }}>Loading dealership branches...</div>
      ) : dealers.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '3rem', background: 'white', borderRadius: '10px' }}>
          <h3>No dealerships found for state: {selectedState}</h3>
        </div>
      ) : (
        <div className="dealers-grid">
          {dealers.map(dealer => (
            <div key={dealer.dealer_id || dealer.id} className="dealer-card">
              <img
                src={dealer.image || 'https://images.unsplash.com/photo-1563720223185-11003d516935?w=800'}
                alt={dealer.name}
                className="dealer-img"
              />
              <div className="dealer-body">
                <div className="state-tag">{dealer.state}</div>
                <h3 className="dealer-title">{dealer.name}</h3>
                <div className="dealer-info">
                  <p>📍 {dealer.address}, {dealer.city}, {dealer.state} {dealer.zip}</p>
                  <p>📞 {dealer.phone}</p>
                </div>
                <p style={{ fontSize: '0.9rem', color: '#475569', marginBottom: '1.25rem' }}>
                  {dealer.description}
                </p>
                <div style={{ display: 'flex', gap: '0.5rem', marginTop: 'auto' }}>
                  <Link to={`/dealer/${dealer.dealer_id || dealer.id}`} className="btn-view" style={{ flex: 1 }}>
                    View Dealer Details
                  </Link>
                  {isLoggedIn && (
                    <Link to={`/postreview/${dealer.dealer_id || dealer.id}`} className="btn-view" style={{ background: '#10b981' }}>
                      Review Dealer
                    </Link>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dealers;
