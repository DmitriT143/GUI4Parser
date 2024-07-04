import React from 'react'
import { Card, Typography } from '@mui/material'

const ResumePage = ({resume}) =>{
  return(
    <Card>
      <Typography variant="h2" component="div">{resume.link}</Typography>
      <Typography>{resume.name}</Typography>
      <Typography>{resume.salary}</Typography>
      <Typography>{resume.specialty}</Typography>
      <Typography>{resume.part_time}</Typography>
      <Typography>{resume.workday}</Typography>
    </Card>
  )    
}

export default ResumePage;
