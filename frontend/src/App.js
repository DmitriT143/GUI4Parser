import React from 'react'
import ResumePage from './components/ResumePage'
import VacanciesPage from './components/VacanciesPage'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Container } from '@mui/material';

const App = () => {
  return (
    <Router>
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h5" style={{ flexGrow: 1 }}>
          Simple site, Don't think too much
        </Typography>
        <Button color="inherit" component={Link} to="/vacancies">Vacancies</Button>
        <Button color="inherit" component={Link} to="/resume">Resumes</Button>
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

export default App;
