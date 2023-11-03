/* Import Dependencies */
import ReactDOM from 'react-dom/client';
import axios from 'axios';

/* Import Styles */
import 'bootstrap/dist/css/bootstrap.min.css';

/* Import Components */
import App from './App';


axios.defaults.baseURL = 'https://elixir-biohackathon-2023.rahtiapp.fi';


const RenderRoot = () => {
  const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
  );

  root.render(
    <App />
  );
}

RenderRoot();