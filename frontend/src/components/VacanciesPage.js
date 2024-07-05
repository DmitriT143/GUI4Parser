import React, {useState, useEffect} from 'react'
import VacanciesItem from './VacanciesItem'
import axios from 'axios';
import { Container, TextField, Grid, Paper, Typography, Button } from '@mui/material';
import useStyles from './styles'
import Analytics from './VAnalytics'

const VacanciesPage = () =>{
  const classes = useStyles();
  const [Vacancy, setVacancy] = useState([]);
  const [filter, setFilter] = useState({
    name: '',
    salary_min: '',
    salary_max: '',
    region: '',
    workday: '',
  })
  useEffect(() =>{
    axios.get('http://localhost:8000/Vacancy/', {params:filter})
    .then(response => setVacancy(response.data))
    .catch(error => console.error('Error fetching data:', error))
  }, [filter],)

  const handleFilterChange = (e) => {
    setFilter({
      ...filter,
      [e.target.name]: e.target.value
    })
  }
  return(
    <Container className={classes.Container}>
      <Analytics />
      <Typography variant="h4" className={classes.heading} >Vacancies</Typography>
      <Grid container spacing={2} className={classes.filterContainer}>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Name" name="name" onChange={handleFilterChange} required={true} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Min Salary" name="salary_min" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Max salary" name="salary_max" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Vacancy Region" name="region" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <TextField fullWidth label="Workday Type" name="workday" onChange={handleFilterChange} />
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Button fullWidth variant='contained' name="Click Me" label="Click Me" className={classes.tryButton}>
            Search for More
          </Button>
        </Grid>
      </Grid>
      <Grid container spacing={3} className={classes.listContainer}>
        {Vacancy.map(Vacancy => (
          <Grid item xs={12} sm={6} md={4} kay={Vacancy.link}>
            <Paper className={classes.paper}>
              <VacanciesItem Vacancy={Vacancy} />
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Container>
  )
}

export default VacanciesPage;
