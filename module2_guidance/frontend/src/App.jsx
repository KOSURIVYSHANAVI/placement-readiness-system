import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CareerGuidance from './pages/CareerGuidance';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CareerGuidance />} />
      </Routes>
    </Router>
  );
}

export default App;
