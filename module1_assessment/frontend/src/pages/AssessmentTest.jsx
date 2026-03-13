import { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function AssessmentTest() {
  const { category } = useParams();
  const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [timeLeft, setTimeLeft] = useState(300);
  const timerRef = useRef(null);

  useEffect(() => {
    fetch(`http://localhost:5001/api/questions/${category}`)
      .then(res => res.json())
      .then(data => {
        const shuffled = data.sort(() => 0.5 - Math.random());
        const selected = shuffled.slice(0, 10);
        setQuestions(selected);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, [category]);

  useEffect(() => {
    if (questions.length > 0 && timeLeft > 0) {
      timerRef.current = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            clearInterval(timerRef.current);
            handleSubmit();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [questions]);

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const handleAnswer = (questionId, answer) => {
    setAnswers({ ...answers, [questionId]: answer });
  };

  const handleSubmit = async () => {
    if (timerRef.current) clearInterval(timerRef.current);
    
    const studentId = localStorage.getItem('student_id');
    const formattedAnswers = Object.keys(answers).map(qId => ({
      question_id: qId,
      selected_answer: answers[qId]
    }));

    try {
      const res = await fetch('http://localhost:5001/api/test/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          student_id: studentId,
          category: category,
          answers: formattedAnswers
        })
      });
      const data = await res.json();
      
      const percentage = data.percentage;
      let performanceLevel = '';
      if (percentage >= 80) performanceLevel = 'Excellent';
      else if (percentage >= 60) performanceLevel = 'Good';
      else if (percentage >= 40) performanceLevel = 'Average';
      else performanceLevel = 'Needs Improvement';
      
      alert(`Test Submitted!\nScore: ${data.score}/${data.total}\nPercentage: ${percentage.toFixed(2)}%\nPerformance: ${performanceLevel}\nReadiness Score: ${data.readiness_score.toFixed(2)}`);
      navigate('/assessment-dashboard');
    } catch (error) {
      alert('Error submitting test');
    }
  };

  if (loading) return <div style={{ padding: '30px' }}>Loading questions...</div>;

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial', maxWidth: '900px', margin: '0 auto' }}>
      <div style={{ 
        position: 'sticky', 
        top: '20px', 
        backgroundColor: timeLeft < 60 ? '#dc3545' : '#667eea', 
        color: 'white', 
        padding: '15px 30px', 
        borderRadius: '10px', 
        textAlign: 'center', 
        marginBottom: '20px',
        fontSize: '24px',
        fontWeight: 'bold',
        boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
        zIndex: 1000
      }}>
        ⏱️ Time Remaining: {formatTime(timeLeft)}
      </div>
      
      <h1 style={{ color: '#667eea', textAlign: 'center' }}>{category.toUpperCase()} Assessment</h1>
      <p style={{ textAlign: 'center', color: '#666', marginBottom: '30px' }}>10 Random Questions | 5 Minutes</p>
      
      {questions.length === 0 ? (
        <p>No questions available for this category.</p>
      ) : (
        <div>
          {questions.map((q, index) => (
            <div key={q.id} style={{ marginBottom: '30px', padding: '20px', border: '2px solid #667eea', borderRadius: '10px', backgroundColor: '#f9f9ff' }}>
              <h3 style={{ color: '#333' }}>Q{index + 1}. {q.question_text}</h3>
              <div style={{ marginTop: '15px' }}>
                {['A', 'B', 'C', 'D'].map(option => (
                  <label key={option} style={{ display: 'block', marginBottom: '10px', cursor: 'pointer', padding: '10px', backgroundColor: answers[q.id] === option ? '#667eea' : 'white', color: answers[q.id] === option ? 'white' : 'black', borderRadius: '5px', border: '1px solid #ddd' }}>
                    <input
                      type="radio"
                      name={`question-${q.id}`}
                      value={option}
                      onChange={() => handleAnswer(q.id, option)}
                      style={{ marginRight: '10px' }}
                    />
                    {option}. {q[`option_${option.toLowerCase()}`]}
                  </label>
                ))}
              </div>
            </div>
          ))}
          
          <div style={{ textAlign: 'center', marginTop: '30px' }}>
            <button onClick={handleSubmit} style={{ padding: '15px 40px', backgroundColor: '#667eea', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', fontSize: '16px', fontWeight: 'bold' }}>Submit Test</button>
            <button onClick={() => navigate('/assessment-dashboard')} style={{ marginLeft: '15px', padding: '15px 40px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', fontSize: '16px' }}>Cancel</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default AssessmentTest;
