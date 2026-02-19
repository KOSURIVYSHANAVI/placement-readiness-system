import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' }}>
      <h1 style={{ color: 'white', fontSize: '48px', marginBottom: '20px', textAlign: 'center' }}>Placement Readiness System</h1>
      <p style={{ color: 'white', fontSize: '20px', marginBottom: '50px', textAlign: 'center' }}>4-Module Microservices Architecture</p>
      
      <div style={{ display: 'flex', gap: '30px' }}>
        <div onClick={() => navigate('/student-auth')} style={{ backgroundColor: 'white', padding: '40px 60px', borderRadius: '15px', cursor: 'pointer', textAlign: 'center', boxShadow: '0 10px 40px rgba(0,0,0,0.3)', transition: 'transform 0.2s' }}>
          <h2 style={{ color: '#667eea', marginBottom: '10px' }}>Student Portal</h2>
          <p style={{ color: '#666' }}>Take assessments & get guidance</p>
        </div>
        
        <div onClick={() => navigate('/admin-auth')} style={{ backgroundColor: 'white', padding: '40px 60px', borderRadius: '15px', cursor: 'pointer', textAlign: 'center', boxShadow: '0 10px 40px rgba(0,0,0,0.3)', transition: 'transform 0.2s' }}>
          <h2 style={{ color: '#f5576c', marginBottom: '10px' }}>Admin Portal</h2>
          <p style={{ color: '#666' }}>Manage system & students</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
