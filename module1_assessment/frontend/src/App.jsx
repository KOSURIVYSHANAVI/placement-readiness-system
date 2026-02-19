import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StudentAuth from './pages/StudentAuth';
import AssessmentDashboard from './pages/AssessmentDashboard';
import AssessmentTest from './pages/AssessmentTest';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<StudentAuth />} />
        <Route path="/assessment-dashboard" element={<AssessmentDashboard />} />
        <Route path="/assessment-test/:category" element={<AssessmentTest />} />
      </Routes>
    </Router>
  );
}

export default App;
