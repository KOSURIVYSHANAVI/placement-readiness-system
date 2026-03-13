import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function AdminAuth() {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const res = await fetch('http://localhost:5004/api/admin/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await res.json();
      
      if (res.ok) {
        localStorage.setItem('admin_id', data.admin_id);
        localStorage.setItem('admin_name', data.name);
        localStorage.setItem('role', 'admin');
        alert(data.message);
        navigate('/admin-management');
      } else {
        alert(data.error);
      }
    } catch (error) {
      alert('Connection error');
    }
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)' }}>
      <div style={{ backgroundColor: 'white', padding: '40px', borderRadius: '15px', boxShadow: '0 10px 40px rgba(0,0,0,0.2)', width: '400px' }}>
        <h2 style={{ textAlign: 'center', color: '#f5576c', marginBottom: '30px' }}>Admin Login</h2>
        
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            required
            style={{ width: '100%', padding: '12px', marginBottom: '15px', border: '1px solid #ddd', borderRadius: '8px', fontSize: '14px' }}
          />
          
          <input
            type="password"
            placeholder="Password"
            value={formData.password}
            onChange={(e) => setFormData({ ...formData, password: e.target.value })}
            required
            style={{ width: '100%', padding: '12px', marginBottom: '20px', border: '1px solid #ddd', borderRadius: '8px', fontSize: '14px' }}
          />
          
          <button type="submit" style={{ width: '100%', padding: '12px', backgroundColor: '#f5576c', color: 'white', border: 'none', borderRadius: '8px', fontSize: '16px', fontWeight: 'bold', cursor: 'pointer' }}>
            Login
          </button>
        </form>
        
        <button onClick={() => navigate('/')} style={{ width: '100%', marginTop: '15px', padding: '10px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer' }}>
          Back to Home
        </button>
      </div>
    </div>
  );
}

export default AdminAuth;
