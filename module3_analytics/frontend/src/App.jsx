import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AnalyticsDashboard from './pages/AnalyticsDashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AnalyticsDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
