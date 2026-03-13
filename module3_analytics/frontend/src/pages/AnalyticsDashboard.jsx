import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function AnalyticsDashboard() {
  const navigate = useNavigate();
  const [dashboardData, setDashboardData] = useState({});
  const [chartData, setChartData] = useState({ categories: [], scores: [] });
  const [timeline, setTimeline] = useState([]);
  const [comparison, setComparison] = useState({});
  const [activeView, setActiveView] = useState('overview');
  const studentName = localStorage.getItem('student_name');

  useEffect(() => {
    const studentId = localStorage.getItem('student_id');
    
    if (!studentId) {
      navigate('/');
      return;
    }

    fetch(`http://localhost:5003/api/analytics/dashboard/${studentId}`)
      .then(res => res.json())
      .then(data => setDashboardData(data));

    fetch(`http://localhost:5003/api/analytics/chart/${studentId}`)
      .then(res => res.json())
      .then(data => setChartData(data));

    fetch(`http://localhost:5003/api/analytics/timeline/${studentId}`)
      .then(res => res.json())
      .then(data => setTimeline(data.timeline || []));

    fetch(`http://localhost:5003/api/analytics/comparison/${studentId}`)
      .then(res => res.json())
      .then(data => setComparison(data.comparisons || {}));
  }, [navigate]);

  const getPerformanceLevel = (score) => {
    if (score >= 80) return { level: 'Excellent', color: '#28a745', emoji: '🌟' };
    if (score >= 60) return { level: 'Good', color: '#17a2b8', emoji: '👍' };
    if (score >= 40) return { level: 'Average', color: '#ffc107', emoji: '⚠️' };
    return { level: 'Needs Improvement', color: '#dc3545', emoji: '📚' };
  };

  const getStrengthsAndWeaknesses = () => {
    if (!chartData.categories.length) return { strengths: [], weaknesses: [] };
    const subjects = chartData.categories.map((cat, i) => ({ name: cat, score: chartData.scores[i] }));
    const strengths = subjects.filter(s => s.score >= 70).sort((a, b) => b.score - a.score);
    const weaknesses = subjects.filter(s => s.score < 60).sort((a, b) => a.score - b.score);
    return { strengths, weaknesses };
  };

  const getRecommendations = () => {
    const avgScore = dashboardData.average_score || 0;
    const { weaknesses } = getStrengthsAndWeaknesses();
    const recommendations = [];

    if (avgScore >= 80) {
      recommendations.push('🎉 Excellent performance! You\'re placement ready!');
      recommendations.push('💼 Start applying to top companies');
      recommendations.push('🎯 Focus on interview preparation and soft skills');
    } else if (avgScore >= 60) {
      recommendations.push('👍 Good progress! Keep improving');
      recommendations.push('📈 Focus on weak areas to boost your score');
      if (weaknesses.length > 0) {
        recommendations.push(`🎯 Priority: Improve ${weaknesses[0].name}`);
      }
    } else {
      recommendations.push('📚 More practice needed');
      recommendations.push('⏰ Dedicate 2-3 hours daily for preparation');
      if (weaknesses.length > 0) {
        recommendations.push(`🔴 Critical: Focus on ${weaknesses.slice(0, 2).map(w => w.name).join(', ')}`);
      }
    }

    return recommendations;
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial', backgroundColor: '#f5f7fa', minHeight: '100vh' }}>
      <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
          <div>
            <h1 style={{ color: '#667eea', margin: 0 }}>Analytics Dashboard</h1>
            <p style={{ color: '#666', margin: '5px 0' }}>Welcome back, {studentName}! Track your progress</p>
          </div>
          <button onClick={() => navigate('/assessment-dashboard')} style={{ padding: '10px 20px', backgroundColor: '#667eea', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer' }}>← Back to Dashboard</button>
        </div>

        {/* View Tabs */}
        <div style={{ marginBottom: '30px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <button onClick={() => setActiveView('overview')} style={{ padding: '10px 20px', backgroundColor: activeView === 'overview' ? '#667eea' : 'white', color: activeView === 'overview' ? 'white' : 'black', border: '1px solid #667eea', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}>📊 Overview</button>
          <button onClick={() => setActiveView('performance')} style={{ padding: '10px 20px', backgroundColor: activeView === 'performance' ? '#667eea' : 'white', color: activeView === 'performance' ? 'white' : 'black', border: '1px solid #667eea', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}>📈 Performance</button>
          <button onClick={() => setActiveView('comparison')} style={{ padding: '10px 20px', backgroundColor: activeView === 'comparison' ? '#667eea' : 'white', color: activeView === 'comparison' ? 'white' : 'black', border: '1px solid #667eea', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}>🔄 Comparison</button>
          <button onClick={() => setActiveView('timeline')} style={{ padding: '10px 20px', backgroundColor: activeView === 'timeline' ? '#667eea' : 'white', color: activeView === 'timeline' ? 'white' : 'black', border: '1px solid #667eea', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}>⏱️ Timeline</button>
          <button onClick={() => setActiveView('recommendations')} style={{ padding: '10px 20px', backgroundColor: activeView === 'recommendations' ? '#667eea' : 'white', color: activeView === 'recommendations' ? 'white' : 'black', border: '1px solid #667eea', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}>💡 Recommendations</button>
        </div>

        {/* Overview Tab */}
        {activeView === 'overview' && (
        <div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', marginBottom: '30px' }}>
            <div style={{ backgroundColor: '#667eea', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center', boxShadow: '0 4px 12px rgba(102,126,234,0.3)' }}>
              <h2 style={{ margin: 0, fontSize: '36px' }}>{dashboardData.total_tests || 0}</h2>
              <p style={{ margin: '10px 0 0 0' }}>Total Tests</p>
            </div>
            <div style={{ backgroundColor: '#28a745', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center', boxShadow: '0 4px 12px rgba(40,167,69,0.3)' }}>
              <h2 style={{ margin: 0, fontSize: '36px' }}>{dashboardData.average_score?.toFixed(1) || 0}%</h2>
              <p style={{ margin: '10px 0 0 0' }}>Average Score</p>
            </div>
            <div style={{ backgroundColor: '#ffa500', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center', boxShadow: '0 4px 12px rgba(255,165,0,0.3)' }}>
              <h2 style={{ margin: 0, fontSize: '36px' }}>{dashboardData.highest_score?.toFixed(1) || 0}%</h2>
              <p style={{ margin: '10px 0 0 0' }}>Highest Score</p>
            </div>
            <div style={{ backgroundColor: '#dc3545', color: 'white', padding: '25px', borderRadius: '12px', textAlign: 'center', boxShadow: '0 4px 12px rgba(220,53,69,0.3)' }}>
              <h2 style={{ margin: 0, fontSize: '36px' }}>{dashboardData.lowest_score?.toFixed(1) || 0}%</h2>
              <p style={{ margin: '10px 0 0 0' }}>Lowest Score</p>
            </div>
          </div>

          {/* Overall Performance Level */}
          <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', marginBottom: '30px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
            <h2 style={{ color: '#667eea', marginBottom: '20px' }}>Overall Performance Level</h2>
            {dashboardData.average_score ? (
              <div style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '64px', marginBottom: '10px' }}>{getPerformanceLevel(dashboardData.average_score).emoji}</div>
                <h3 style={{ color: getPerformanceLevel(dashboardData.average_score).color, margin: '10px 0', fontSize: '28px' }}>{getPerformanceLevel(dashboardData.average_score).level}</h3>
                <p style={{ color: '#666', fontSize: '18px' }}>You scored {dashboardData.average_score.toFixed(1)}% on average</p>
              </div>
            ) : (
              <p style={{ color: '#666', textAlign: 'center' }}>Take tests to see your performance level</p>
            )}
          </div>
        </div>
        )}

        {/* Performance Tab */}
        {activeView === 'performance' && (
        <div>
          <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', marginBottom: '30px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
            <h2 style={{ color: '#667eea', marginBottom: '20px' }}>Subject-wise Performance</h2>
            {chartData.categories.length === 0 ? (
              <p style={{ color: '#666' }}>No data available. Take some tests first!</p>
            ) : (
              <div style={{ marginTop: '20px' }}>
                {chartData.categories.map((cat, i) => {
                  const performance = getPerformanceLevel(chartData.scores[i]);
                  return (
                    <div key={i} style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '8px' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                        <span style={{ fontWeight: 'bold', textTransform: 'uppercase', fontSize: '16px' }}>{cat}</span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                          <span style={{ padding: '4px 12px', borderRadius: '12px', backgroundColor: performance.color, color: 'white', fontSize: '12px', fontWeight: 'bold' }}>{performance.level}</span>
                          <span style={{ fontWeight: 'bold', fontSize: '18px', color: performance.color }}>{chartData.scores[i].toFixed(1)}%</span>
                        </div>
                      </div>
                      <div style={{ width: '100%', height: '35px', backgroundColor: '#e0e0e0', borderRadius: '17px', overflow: 'hidden' }}>
                        <div style={{ width: `${chartData.scores[i]}%`, height: '100%', backgroundColor: performance.color, transition: 'width 0.5s ease' }}></div>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>

          {/* Strengths and Weaknesses */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px' }}>
            <div style={{ backgroundColor: 'white', padding: '25px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
              <h3 style={{ color: '#28a745', marginBottom: '15px' }}>💪 Your Strengths</h3>
              {getStrengthsAndWeaknesses().strengths.length === 0 ? (
                <p style={{ color: '#666' }}>Score 70%+ in subjects to see strengths</p>
              ) : (
                <ul style={{ listStyle: 'none', padding: 0 }}>
                  {getStrengthsAndWeaknesses().strengths.map((s, i) => (
                    <li key={i} style={{ padding: '10px', marginBottom: '8px', backgroundColor: '#d4edda', borderRadius: '8px', color: '#155724' }}>
                      <strong>{s.name}</strong>: {s.score.toFixed(1)}%
                    </li>
                  ))}
                </ul>
              )}
            </div>

            <div style={{ backgroundColor: 'white', padding: '25px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
              <h3 style={{ color: '#dc3545', marginBottom: '15px' }}>📚 Areas to Improve</h3>
              {getStrengthsAndWeaknesses().weaknesses.length === 0 ? (
                <p style={{ color: '#666' }}>Great! No weak areas found</p>
              ) : (
                <ul style={{ listStyle: 'none', padding: 0 }}>
                  {getStrengthsAndWeaknesses().weaknesses.map((w, i) => (
                    <li key={i} style={{ padding: '10px', marginBottom: '8px', backgroundColor: '#f8d7da', borderRadius: '8px', color: '#721c24' }}>
                      <strong>{w.name}</strong>: {w.score.toFixed(1)}%
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>
        )}

        {/* Comparison Tab */}
        {activeView === 'comparison' && (
        <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
          <h2 style={{ color: '#667eea', marginBottom: '20px' }}>📊 Current vs Previous Performance</h2>
          {Object.keys(comparison).length === 0 ? (
            <p style={{ color: '#666' }}>Take multiple tests in same subjects to see comparison</p>
          ) : (
            <div style={{ marginTop: '20px' }}>
              {Object.entries(comparison).map(([category, data]) => (
                <div key={category} style={{ marginBottom: '20px', padding: '20px', backgroundColor: '#f8f9fa', borderRadius: '8px' }}>
                  <h3 style={{ textTransform: 'uppercase', marginBottom: '15px' }}>{category}</h3>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '15px' }}>
                    <div>
                      <p style={{ margin: '5px 0', color: '#666' }}>Current Score</p>
                      <p style={{ margin: '5px 0', fontSize: '24px', fontWeight: 'bold', color: '#667eea' }}>{data.current?.toFixed(1)}%</p>
                    </div>
                    {data.previous && (
                      <>
                        <div>
                          <p style={{ margin: '5px 0', color: '#666' }}>Previous Score</p>
                          <p style={{ margin: '5px 0', fontSize: '24px', fontWeight: 'bold', color: '#999' }}>{data.previous.toFixed(1)}%</p>
                        </div>
                        <div>
                          <p style={{ margin: '5px 0', color: '#666' }}>Improvement</p>
                          <p style={{ margin: '5px 0', fontSize: '24px', fontWeight: 'bold', color: data.improvement >= 0 ? '#28a745' : '#dc3545' }}>
                            {data.improvement >= 0 ? '+' : ''}{data.improvement.toFixed(1)}%
                          </p>
                        </div>
                      </>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
        )}

        {/* Timeline Tab */}
        {activeView === 'timeline' && (
        <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
          <h2 style={{ color: '#667eea', marginBottom: '20px' }}>⏱️ Progress Timeline</h2>
          {timeline.length === 0 ? (
            <p style={{ color: '#666' }}>No timeline data available yet</p>
          ) : (
            <div style={{ marginTop: '20px' }}>
              {timeline.map((item, i) => (
                <div key={i} style={{ display: 'flex', gap: '20px', marginBottom: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '8px', borderLeft: '4px solid #667eea' }}>
                  <div style={{ minWidth: '150px' }}>
                    <p style={{ margin: 0, fontSize: '12px', color: '#666' }}>{item.date}</p>
                  </div>
                  <div style={{ flex: 1 }}>
                    <p style={{ margin: '0 0 5px 0', fontWeight: 'bold', textTransform: 'uppercase' }}>{item.category}</p>
                    <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
                      <span style={{ fontSize: '18px', fontWeight: 'bold', color: getPerformanceLevel(item.percentage).color }}>{item.percentage.toFixed(1)}%</span>
                      <span style={{ padding: '3px 10px', borderRadius: '10px', backgroundColor: getPerformanceLevel(item.percentage).color, color: 'white', fontSize: '11px' }}>{getPerformanceLevel(item.percentage).level}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
        )}

        {/* Recommendations Tab */}
        {activeView === 'recommendations' && (
        <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
          <h2 style={{ color: '#667eea', marginBottom: '20px' }}>💡 Personalized Recommendations</h2>
          {dashboardData.total_tests === 0 ? (
            <p style={{ color: '#666' }}>Take tests to get personalized recommendations</p>
          ) : (
            <div>
              <div style={{ marginBottom: '30px' }}>
                <h3 style={{ color: '#333', marginBottom: '15px' }}>Based on your performance:</h3>
                <ul style={{ listStyle: 'none', padding: 0 }}>
                  {getRecommendations().map((rec, i) => (
                    <li key={i} style={{ padding: '15px', marginBottom: '10px', backgroundColor: '#e7f3ff', borderRadius: '8px', borderLeft: '4px solid #667eea', fontSize: '16px' }}>
                      {rec}
                    </li>
                  ))}
                </ul>
              </div>

              <div style={{ padding: '20px', backgroundColor: '#fff3cd', borderRadius: '8px', borderLeft: '4px solid #ffc107' }}>
                <h3 style={{ color: '#856404', marginBottom: '10px' }}>📅 Study Plan Suggestion</h3>
                <p style={{ margin: '5px 0', color: '#856404' }}>• Practice weak subjects for 1 hour daily</p>
                <p style={{ margin: '5px 0', color: '#856404' }}>• Take 1 test every 2 days to track progress</p>
                <p style={{ margin: '5px 0', color: '#856404' }}>• Review mistakes after each test</p>
                <p style={{ margin: '5px 0', color: '#856404' }}>• Check career guidance for learning resources</p>
              </div>

              <div style={{ marginTop: '20px', textAlign: 'center' }}>
                <button onClick={() => navigate('/career-guidance')} style={{ padding: '12px 30px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold', marginRight: '10px' }}>View Career Guidance</button>
                <button onClick={() => navigate('/assessment-dashboard')} style={{ padding: '12px 30px', backgroundColor: '#667eea', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>Take More Tests</button>
              </div>
            </div>
          )}
        </div>
        )}
      </div>
    </div>
  );
}

export default AnalyticsDashboard;
