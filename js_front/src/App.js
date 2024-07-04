import React from 'react'
import './App.css'
import ResumePage from './Pages/ResumePage/ResumePage'
import VacanciesPage from './Pages/VacanciesPage/VacanciesPage'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { AppBar, Toolbar, Container } from '@mui/material';

const App = () => {
  return (
    <Router>
    <AppBar position="static">
      <Toolbar className="App-bottom">
        <hug>
            <button className="Resume-Link"onClick={PlaceholderReaction}>
              This is MY parser site
            </button>
          <Link to="/Resume">
            <button className="Resume-Link">
              This is <code className="App-link">link</code> to Resumes
            </button>
          </Link>
          <Link to="Vacancies">
            <button className="Vacancie-Link">
              <p>This is <code className="App-link"> link </code> to Vacancies </p>
            </button>
          </Link>
        </hug>
      </Toolbar>
    </AppBar>
      <Container>
        <Routes>
          <Route path="/Resume" element={<ResumePage/>} />
          <Route path="/Vacancies" element={<VacanciesPage/>} />
        </Routes>
      </Container>
    </Router>
  );
}
function PlaceholderReaction() {
  alert('Клик!')
}

export default App;
