import React from 'react'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          This is a Redirect page
        </h1>
      </header>
      <body>
        <hug>
        <button className="Resume-Link" onClick={RedirectResumes}>
          <p>This is <code className="App-link">link</code> to Resumes</p>
        </button>
        <button className="Vacancie-Link" onClick={RedirectVacancies}>
          <p>This is <code className="App-link"> link </code> to Vacancies </p>
        </button>
        </hug>
      </body>
      <back className="App-bottom"><p>^_^</p></back>
    </div>
  );
}

function RedirectVacancies(){
  alert("Placeholder, get to Vacancies")
}
function RedirectResumes() {
  alert("Placeholder, get to Resumes")
}

export default App;
