import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function AdminManagement() {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('overview');
  const [analytics, setAnalytics] = useState({});
  const [students, setStudents] = useState([]);
  const [questionForm, setQuestionForm] = useState({
    category: 'quantitative',
    question_text: '',
    option_a: '',
    option_b: '',
    option_c: '',
    option_d: '',
    correct_answer: 'A'
  });
  const [subjectForm, setSubjectForm] = useState({
    key: '',
    name: '',
    icon: '📚'
  });
  const [questionCounts, setQuestionCounts] = useState([]);
  const [careerPathForm, setCareerPathForm] = useState({
    category: 'quantitative',
    title: '',
    description: '',
    resources: '',
    duration: ''
  });
  const [roadmaps, setRoadmaps] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5004/api/admin/analytics')
      .then(res => res.json())
      .then(data => setAnalytics(data));

    fetch('http://localhost:5004/api/admin/students')
      .then(res => res.json())
      .then(data => setStudents(data.students || []));

    fetch('http://localhost:5004/api/admin/questions/count')
      .then(res => res.json())
      .then(data => setQuestionCounts(data));

    fetch('http://localhost:5004/api/admin/roadmaps')
      .then(res => res.json())
      .then(data => setRoadmaps(data));
  }, []);

  const handleAddQuestion = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:5004/api/admin/questions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(questionForm)
      });
      if (res.ok) {
        alert('Question added successfully!');
        setQuestionForm({ category: 'quantitative', question_text: '', option_a: '', option_b: '', option_c: '', option_d: '', correct_answer: 'A' });
        // Refresh question counts
        fetch('http://localhost:5004/api/admin/questions/count')
          .then(res => res.json())
          .then(data => setQuestionCounts(data));
      }
    } catch (error) {
      alert('Error adding question');
    }
  };

  const handleAddSubject = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:5004/api/admin/subjects', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(subjectForm)
      });
      if (res.ok) {
        alert('Subject added successfully!');
        setSubjectForm({ key: '', name: '', icon: '📚' });
      }
    } catch (error) {
      alert('Error adding subject');
    }
  };

  const handleAddCareerPath = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:5004/api/admin/roadmaps', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(careerPathForm)
      });
      if (res.ok) {
        alert('Career path added successfully!');
        setCareerPathForm({ category: 'quantitative', title: '', description: '', resources: '', duration: '' });
        // Refresh roadmaps
        fetch('http://localhost:5004/api/admin/roadmaps')
          .then(res => res.json())
          .then(data => setRoadmaps(data));
      }
    } catch (error) {
      alert('Error adding career path');
    }
  };

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

      <div style={{ marginBottom: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
        <button onClick={() => setActiveTab('overview')} style={{ padding: '10px 20px', backgroundColor: activeTab === 'overview' ? '#6c757d' : 'white', color: activeTab === 'overview' ? 'white' : 'black', border: '1px solid #ddd', borderRadius: '5px', cursor: 'pointer' }}>Overview</button>
        <button onClick={() => setActiveTab('add-question')} style={{ padding: '10px 20px', backgroundColor: activeTab === 'add-question' ? '#6c757d' : 'white', color: activeTab === 'add-question' ? 'white' : 'black', border: '1px solid #ddd', borderRadius: '5px', cursor: 'pointer' }}>Add Question</button>
        <button onClick={() => setActiveTab('add-subject')} style={{ padding: '10px 20px', backgroundColor: activeTab === 'add-subject' ? '#6c757d' : 'white', color: activeTab === 'add-subject' ? 'white' : 'black', border: '1px solid #ddd', borderRadius: '5px', cursor: 'pointer' }}>Add Subject</button>
        <button onClick={() => setActiveTab('add-career-path')} style={{ padding: '10px 20px', backgroundColor: activeTab === 'add-career-path' ? '#6c757d' : 'white', color: activeTab === 'add-career-path' ? 'white' : 'black', border: '1px solid #ddd', borderRadius: '5px', cursor: 'pointer' }}>Add Career Path</button>
        <button onClick={() => setActiveTab('students')} style={{ padding: '10px 20px', backgroundColor: activeTab === 'students' ? '#6c757d' : 'white', color: activeTab === 'students' ? 'white' : 'black', border: '1px solid #ddd', borderRadius: '5px', cursor: 'pointer' }}>Students</button>
      </div>

      {activeTab === 'overview' && (
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
      )}

      {activeTab === 'add-question' && (
      <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', marginBottom: '30px' }}>
        <h2>Add New Question</h2>
        <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#f0f0f0', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 10px 0' }}>Question Count by Subject:</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '10px' }}>
            {questionCounts.map(item => (
              <div key={item.category} style={{ padding: '10px', backgroundColor: item.count >= 30 ? '#d4edda' : '#fff3cd', borderRadius: '5px', textAlign: 'center' }}>
                <strong>{item.category}</strong>: {item.count} questions
              </div>
            ))}
          </div>
        </div>
        <form onSubmit={handleAddQuestion}>
          <select value={questionForm.category} onChange={(e) => setQuestionForm({ ...questionForm, category: e.target.value })} style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }}>
            <option value="quantitative">Quantitative Aptitude</option>
            <option value="reasoning">Logical Reasoning</option>
            <option value="verbal">Verbal Ability</option>
            <option value="dbms">DBMS</option>
            <option value="cn">Computer Networks</option>
            <option value="os">Operating Systems</option>
            <option value="coding">Coding</option>
          </select>
          <textarea placeholder="Question Text" value={questionForm.question_text} onChange={(e) => setQuestionForm({ ...questionForm, question_text: e.target.value })} required style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd', minHeight: '80px' }} />
          <input type="text" placeholder="Option A" value={questionForm.option_a} onChange={(e) => setQuestionForm({ ...questionForm, option_a: e.target.value })} required style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} />
          <input type="text" placeholder="Option B" value={questionForm.option_b} onChange={(e) => setQuestionForm({ ...questionForm, option_b: e.target.value })} required style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} />
          <input type="text" placeholder="Option C" value={questionForm.option_c} onChange={(e) => setQuestionForm({ ...questionForm, option_c: e.target.value })} required style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} />
          <input type="text" placeholder="Option D" value={questionForm.option_d} onChange={(e) => setQuestionForm({ ...questionForm, option_d: e.target.value })} required style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} />
          <select value={questionForm.correct_answer} onChange={(e) => setQuestionForm({ ...questionForm, correct_answer: e.target.value })} style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }}>
            <option value="A">A</option>
            <option value="B">B</option>
            <option value="C">C</option>
            <option value="D">D</option>
          </select>
          <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>Add Question</button>
        </form>
      </div>
      )}

      {activeTab === 'add-subject' && (
      <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', marginBottom: '30px' }}>
        <h2>Add New Subject</h2>
        <form onSubmit={handleAddSubject}>
          <input 
            type="text" 
            placeholder="Subject Key (e.g., 'java', 'react')" 
            value={subjectForm.key} 
            onChange={(e) => setSubjectForm({ ...subjectForm, key: e.target.value.toLowerCase() })} 
            required 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} 
          />
          <input 
            type="text" 
            placeholder="Subject Name (e.g., 'Java Programming')" 
            value={subjectForm.name} 
            onChange={(e) => setSubjectForm({ ...subjectForm, name: e.target.value })} 
            required 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} 
          />
          <input 
            type="text" 
            placeholder="Icon (emoji, e.g., ☕)" 
            value={subjectForm.icon} 
            onChange={(e) => setSubjectForm({ ...subjectForm, icon: e.target.value })} 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} 
          />
          <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#17a2b8', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>Add Subject</button>
        </form>
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#e7f3ff', borderRadius: '8px' }}>
          <p style={{ margin: 0, fontSize: '14px', color: '#004085' }}>
            <strong>Note:</strong> After adding a new subject, you need to manually update the AssessmentDashboard.jsx to include it in the categories list.
          </p>
        </div>
      </div>
      )}

      {activeTab === 'add-career-path' && (
      <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', marginBottom: '30px' }}>
        <h2>Add New Career Path / Roadmap</h2>
        <form onSubmit={handleAddCareerPath}>
          <select 
            value={careerPathForm.category} 
            onChange={(e) => setCareerPathForm({ ...careerPathForm, category: e.target.value })} 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }}
          >
            <option value="quantitative">Quantitative Aptitude</option>
            <option value="reasoning">Logical Reasoning</option>
            <option value="verbal">Verbal Ability</option>
            <option value="dbms">DBMS</option>
            <option value="cn">Computer Networks</option>
            <option value="os">Operating Systems</option>
            <option value="coding">Coding</option>
            <option value="dsa">Data Structures & Algorithms</option>
            <option value="python">Python Programming</option>
          </select>
          <input 
            type="text" 
            placeholder="Career Path Title (e.g., 'Master Python Programming')" 
            value={careerPathForm.title} 
            onChange={(e) => setCareerPathForm({ ...careerPathForm, title: e.target.value })} 
            required 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} 
          />
          <textarea 
            placeholder="Description" 
            value={careerPathForm.description} 
            onChange={(e) => setCareerPathForm({ ...careerPathForm, description: e.target.value })} 
            required 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd', minHeight: '80px' }} 
          />
          <textarea 
            placeholder="Resources (e.g., 'Udemy Python Course, LeetCode, GeeksforGeeks')" 
            value={careerPathForm.resources} 
            onChange={(e) => setCareerPathForm({ ...careerPathForm, resources: e.target.value })} 
            required 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd', minHeight: '60px' }} 
          />
          <input 
            type="text" 
            placeholder="Duration (e.g., '4 weeks', '2 months')" 
            value={careerPathForm.duration} 
            onChange={(e) => setCareerPathForm({ ...careerPathForm, duration: e.target.value })} 
            required 
            style={{ width: '100%', padding: '10px', margin: '10px 0', borderRadius: '5px', border: '1px solid #ddd' }} 
          />
          <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>Add Career Path</button>
        </form>
        
        <div style={{ marginTop: '30px' }}>
          <h3>Existing Career Paths ({roadmaps.length})</h3>
          {roadmaps.length === 0 ? (
            <p style={{ color: '#666' }}>No career paths added yet</p>
          ) : (
            <div style={{ display: 'grid', gap: '15px', marginTop: '15px' }}>
              {roadmaps.map(roadmap => (
                <div key={roadmap.id} style={{ padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '8px', border: '1px solid #dee2e6' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start' }}>
                    <div style={{ flex: 1 }}>
                      <h4 style={{ margin: '0 0 5px 0', color: '#667eea' }}>{roadmap.title}</h4>
                      <p style={{ margin: '5px 0', fontSize: '14px', color: '#666' }}><strong>Category:</strong> {roadmap.category}</p>
                      <p style={{ margin: '5px 0', fontSize: '14px', color: '#666' }}><strong>Duration:</strong> {roadmap.duration}</p>
                      <p style={{ margin: '5px 0', fontSize: '14px' }}>{roadmap.description}</p>
                      <p style={{ margin: '5px 0', fontSize: '13px', color: '#555' }}><strong>Resources:</strong> {roadmap.resources}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
      )}

      {activeTab === 'students' && (
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
      )}
    </div>
  );
}

export default AdminManagement;
