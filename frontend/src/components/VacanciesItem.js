import React from 'react'
import { Card, Typography, CardContent, CardActions } from '@mui/material'
import useStyles from './styles'
import { Button } from '@mui/base'

const VacanciePage = ({ Vacancy }) =>{
  const classes = useStyles()
  const link = "hh.ru/vacancy/"+Vacancy.link

  return(
    <Card className={classes.card}>
      <CardContent>
        <Typography color="blue" variant="h6" component="div">hh.ru/vacancy/{Vacancy.link}</Typography>
        <Typography color="textSecondary">{Vacancy.name}</Typography>
        <Typography variant="body1" color = "textSecondary">{Vacancy.salary_min}</Typography>
        <Typography variant="body1" color = "textSecondary">{Vacancy.salary_max}</Typography>
        <Typography variant="body1" color = "textSecondary">{Vacancy.region}</Typography>
        <Typography variant="body1" color = "textSecondary">{Vacancy.workday}</Typography>
        <Typography variant="body1" color = "textSecondary">{Vacancy.requirements}</Typography>
      </CardContent>
      <CardActions>
        <Button size="small" color="primary" href={link}>Learn more</Button>
      </CardActions>
    </Card>
  )    
}

export default VacanciePage;
