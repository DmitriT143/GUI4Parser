import React from 'react'
import { Card, Typography, CardContent, CardActions } from '@mui/material'
import useStyles from './styles'
import { Button } from '@mui/base'

const ResumePage = ({ resume }) =>{
  const classes = useStyles()
  const link = "hh.ru/resume/"+resume.link

  return(
    <Card className={classes.card}>
      <CardContent>
        <Typography color="blue" variant="h6" component="div">hh.ru/resume/{resume.link}</Typography>
        <Typography color="textSecondary">{resume.name}</Typography>
        <Typography variant="body1" color = "textSecondary">{resume.salary}</Typography>
        <Typography variant="body1" color = "textSecondary">{resume.specialty}</Typography>
        <Typography variant="body1" color = "textSecondary">{resume.part_time}</Typography>
        <Typography variant="body1" color = "textSecondary">{resume.workday}</Typography>
      </CardContent>
      <CardActions>
        <Button size="small" color="primary" href={link}>Learn more</Button>
      </CardActions>
    </Card>
  )    
}

export default ResumePage;
