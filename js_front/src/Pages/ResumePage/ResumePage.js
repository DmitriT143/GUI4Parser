import React, {useState, useEffect} from 'react'
import ResumeItem from './ResumeItem'
import './ResumePage.css';
import axios from 'axios';
import { Container, TextField, Grid, Paper, Typography, Button } from '@mui/material';
import { blue } from '@mui/material/colors';

const ResumePage = () =>{
    const [resume, setResume] = useState([]);
    const [filter, setFilter] = useState({
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
    <Container>
      <Typography variant="h4" color='green'>Resumes</Typography>
      <Grid container spacing={1}>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Name" name="name" onChange={handleFilterChange} required={true} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Requested Salary" name="salary" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="specialty" name="specialty" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Employment type" name="part_time" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Workday Type" name="workday" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Button fullWidth variant="contained" disableRipple sx={{ bgcolor:blue[800]}}>
            Button to start search
          </Button>
        </Grid>
      </Grid>
      <Grid container spacing={3}>
        {resume.map(resume => (
          <Grid>
            <Paper>
              <ResumeItem resume={resume} />
            </Paper>
          </Grid>)
        )}
      </Grid>
    </Container>
  )
}

export default ResumePage;
