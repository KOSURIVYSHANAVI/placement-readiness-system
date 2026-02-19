import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function AdminManagement() {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('overview');
  const [analytics, setAnalytics] = useState({});
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5004/api/admin/analytics')
      .then(res => res.json())
      .then(data => setAnalytics(data));

    fetch('http://localhost:5004/api/admin/students')
      .then(res => res.json())
      .then(data => setStudents(data.students || []));
  }, []);

  const handleLogout = () => {
    localStorage.clear();
    navigate('/');
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial', backgroundColor: '#f5f5f5', minHeight: '100vh' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
        <div>
          <h1 style={{ color: '#6c757d', margin: 0 }}>Admin Management Dashboard</h1>
          <p style={{ color: '#666', margin: '5px 0' }}>Module 4 - System Administration</p>
        </div>
        <button onClick={handleLogout} style={{ padding: '10px 20px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>Logout</button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', marginBottom: '30px' }}>
        <div style={{ backgroundColor: '#1e90ff', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center' }}>
          <h2 style={{ margin: 0, fontSize: '36px' }}>{analytics.total_students || 0}</h2>
          <p style={{ margin: '10px 0 0 0' }}>Total Students</p>
        </div>
        <div style={{ backgroundColor: '#28a745', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center' }}>
          <h2 style={{ margin: 0, fontSize: '36px' }}>{analytics.total_tests || 0}</h2>
          <p style={{ margin: '10px 0 0 0' }}>Total Tests</p>
        </div>
        <div style={{ backgroundColor: '#ffa500', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center' }}>
          <h2 style={{ margin: 0, fontSize: '36px' }}>{analytics.total_questions || 0}</h2>
          <p style={{ margin: '10px 0 0 0' }}>Questions</p>
        </div>
        <div style={{ backgroundColor: '#ff6347', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center' }}>
          <h2 style={{ margin: 0, fontSize: '36px' }}>{analytics.avg_performance || 0}%</h2>
          <p style={{ margin: '10px 0 0 0' }}>Avg Performance</p>
        </div>
      </div>

      <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px' }}>
        <h2>Student Monitoring</h2>
        {students.length === 0 ? (
          <p>No students registered yet</p>
        ) : (
          <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px' }}>
            <thead>
              <tr style={{ backgroundColor: '#6c757d', color: 'white' }}>
                <th style={{ padding: '10px', textAlign: 'left' }}>Name</th>
                <th style={{ padding: '10px', textAlign: 'left' }}>Email</th>
                <th style={{ padding: '10px', textAlign: 'center' }}>Tests</th>
                <th style={{ padding: '10px', textAlign: 'center' }}>Avg Score</th>
              </tr>
            </thead>
            <tbody>
              {students.map(student => (
                <tr key={student.id} style={{ borderBottom: '1px solid #ddd' }}>
                  <td style={{ padding: '10px' }}>{student.name}</td>
                  <td style={{ padding: '10px' }}>{student.email}</td>
                  <td style={{ padding: '10px', textAlign: 'center' }}>{student.tests_taken}</td>
                  <td style={{ padding: '10px', textAlign: 'center', fontWeight: 'bold', color: student.average_score >= 70 ? 'green' : 'red' }}>{student.average_score}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}

export default AdminManagement;
