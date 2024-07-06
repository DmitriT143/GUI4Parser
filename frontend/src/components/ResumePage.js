import React, {useState, useEffect} from 'react'
import ResumeItem from './ResumeItem'
import axios from 'axios';
import { Container, TextField, Grid, Paper, Typography, Button } from '@mui/material';
import useStyles from './styles'
import Analytics from './RAnalytics'

const ResumePage = () =>{
  const classes = useStyles();
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
    <Container className={classes.Container}>
      <Analytics />
      <Typography variant="h4" className={classes.heading} >Resumes</Typography>
      <Grid container spacing={2} className={classes.filterContainer}>
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
          <Button fullWidth variant='contained' name="Click Me" label="Click Me" className={classes.tryButton} onClick={() => {alert("Wait for more resumes, don't click again"); axios.get('http://localhost:8000/refresh/resume',{params:filter})}}>
            Search for More
          </Button>
        </Grid>
      </Grid>
      <Grid container spacing={3} className={classes.listContainer}>
        {resume.map(resume => (
          <Grid item xs={12} sm={6} md={4} kay={resume.link}>
            <Paper className={classes.paper}>
              <ResumeItem resume={resume} />
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Container>
  )
}

export default ResumePage;
