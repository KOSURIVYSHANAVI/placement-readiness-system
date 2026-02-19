import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AdminAuth from './pages/AdminAuth';
import AdminManagement from './pages/AdminManagement';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AdminAuth />} />
        <Route path="/admin-management" element={<AdminManagement />} />
      </Routes>
    </Router>
  );
}

export default App;
