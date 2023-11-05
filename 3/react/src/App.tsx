/* Import Dependencies */
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';

/* Import Styles */
import './App.css';

/* Import Components */
import Demo from 'components/demo/Demo';


const App = () => {
  return (
    <div className="h-100 w-100 position-relative">
      <Router>
        <Routes>
          {/* Demo Page */}
          <Route path="/" element={<Demo />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
