import React, {useState, useEffect} from 'react'
import './ResumePage.css';
import axios from 'axios';
import { Container, TextField, Grid, Paper, Typography } from '@mui/material';

const ResumePage = () =>{
    const [resume, setResume] = useState([]);
    const [filter, setFilter] = useState({
      link: '',
      name: '',
      salary: '',
      specialty: '',
      part_time: '',
      workday: '',
    });
  useEffect(() => {
    axios.get('http://localhost:8000/resume/', {params: filter})
    .then(response => setResume(response.data))
    .catch(error => console.error('Error fetching data:', error));
  }, [filter],)
  const handleFilterChange = (e) => {
    setFilter({
      ...filter,
      [e.target.name]: e.target.value
    });
  };
  return(
    <button>This it output )</button>
  )
}

export default ResumePage;
