import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function AssessmentDashboard() {
  const navigate = useNavigate();
  const [results, setResults] = useState([]);
  const studentName = localStorage.getItem('student_name');

  const categories = [
    { name: 'Quantitative Aptitude', key: 'quantitative', icon: '🔢' },
    { name: 'Logical Reasoning', key: 'reasoning', icon: '🧠' },
    { name: 'Verbal Ability', key: 'verbal', icon: '📝' },
    { name: 'DBMS', key: 'dbms', icon: '🗄️' },
    { name: 'Computer Networks', key: 'cn', icon: '🌐' },
    { name: 'Operating Systems', key: 'os', icon: '💻' },
    { name: 'Coding', key: 'coding', icon: '⚡' },
    { name: 'Data Structures & Algorithms', key: 'dsa', icon: '🔗' },
    { name: 'Python Programming', key: 'python', icon: '🐍' }
  ];

  useEffect(() => {
    const studentId = localStorage.getItem('student_id');
    fetch(`http://localhost:5001/api/results/${studentId}`)
      .then(res => res.json())
      .then(data => setResults(data))
      .catch(err => console.error(err));
  }, []);

  const getPerformanceLevel = (percentage) => {
    if (percentage >= 80) return { level: 'Excellent', color: '#28a745' };
    if (percentage >= 60) return { level: 'Good', color: '#17a2b8' };
    if (percentage >= 40) return { level: 'Average', color: '#ffc107' };
    return { level: 'Needs Improvement', color: '#dc3545' };
  };

  const handleLogout = () => {
    localStorage.clear();
    navigate('/');
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial', backgroundColor: '#f5f7fa', minHeight: '100vh' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
          <h1 style={{ color: '#667eea' }}>Assessment Dashboard</h1>
          <div>
            <span style={{ marginRight: '20px', color: '#333', fontWeight: 'bold' }}>Welcome, {studentName}</span>
            <button onClick={handleLogout} style={{ padding: '10px 20px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer' }}>Logout</button>
          </div>
        </div>

        <h2 style={{ color: '#333', marginBottom: '20px' }}>Select Test Category</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginBottom: '40px' }}>
          {categories.map(cat => (
            <div 
              key={cat.key} 
              onClick={() => navigate(`/assessment-test/${cat.key}`)} 
              style={{ 
                padding: '30px', 
                backgroundColor: 'white', 
                borderRadius: '12px', 
                boxShadow: '0 4px 12px rgba(0,0,0,0.1)', 
                cursor: 'pointer', 
                textAlign: 'center', 
                transition: 'all 0.3s ease', 
                border: '2px solid #667eea',
                transform: 'translateY(0)'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-5px)';
                e.currentTarget.style.boxShadow = '0 8px 20px rgba(102,126,234,0.3)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
              }}
            >
              <div style={{ fontSize: '48px', marginBottom: '10px' }}>{cat.icon}</div>
              <h3 style={{ margin: 0, marginBottom: '15px', color: '#667eea' }}>{cat.name}</h3>
              <p style={{ color: '#666', margin: 0, fontSize: '14px' }}>Click to start test</p>
            </div>
          ))}
        </div>

        <h2 style={{ color: '#333', marginBottom: '20px' }}>Your Test Results</h2>
        {results.length === 0 ? (
          <p style={{ color: '#666' }}>No test results yet. Take a test to see your results here.</p>
        ) : (
          <table style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', overflow: 'hidden', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
            <thead>
              <tr style={{ backgroundColor: '#667eea', color: 'white' }}>
                <th style={{ padding: '15px', textAlign: 'left' }}>Category</th>
                <th style={{ padding: '15px', textAlign: 'center' }}>Score</th>
                <th style={{ padding: '15px', textAlign: 'center' }}>Percentage</th>
                <th style={{ padding: '15px', textAlign: 'center' }}>Performance</th>
                <th style={{ padding: '15px', textAlign: 'center' }}>Readiness Score</th>
                <th style={{ padding: '15px', textAlign: 'center' }}>Date</th>
              </tr>
            </thead>
            <tbody>
              {results.map((result, index) => {
                const performance = getPerformanceLevel(result.percentage);
                return (
                  <tr key={index} style={{ borderBottom: '1px solid #eee' }}>
                    <td style={{ padding: '15px' }}>{result.category}</td>
                    <td style={{ padding: '15px', textAlign: 'center' }}>{result.score}/{result.total}</td>
                    <td style={{ padding: '15px', textAlign: 'center' }}>{result.percentage.toFixed(2)}%</td>
                    <td style={{ padding: '15px', textAlign: 'center' }}>
                      <span style={{ 
                        padding: '5px 12px', 
                        borderRadius: '20px', 
                        backgroundColor: performance.color, 
                        color: 'white', 
                        fontSize: '12px',
                        fontWeight: 'bold'
                      }}>
                        {performance.level}
                      </span>
                    </td>
                    <td style={{ padding: '15px', textAlign: 'center' }}>{result.readiness_score.toFixed(2)}</td>
                    <td style={{ padding: '15px', textAlign: 'center' }}>{result.submitted_at}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}

        <div style={{ marginTop: '40px', display: 'flex', gap: '15px' }}>
          <button onClick={() => navigate('/career-guidance')} style={{ padding: '15px 30px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>View Career Guidance</button>
          <button onClick={() => navigate('/analytics-dashboard')} style={{ padding: '15px 30px', backgroundColor: '#17a2b8', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>View Analytics</button>
        </div>
      </div>
    </div>
  );
}

export default AssessmentDashboard;
