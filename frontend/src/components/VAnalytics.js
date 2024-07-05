import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Typography, Box } from '@mui/material';
import useStyles from './styles';

const Analytics = ({ type }) => {
  const [count, setCount] = useState(0);
  const classes = useStyles();

  useEffect(() => {
    const fetchCount = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/Vacancy/?format=json`);
        setCount(response.data.length);
      } catch (error) {
        console.error('Error fetching count:', error);
        setCount(error.message);
      }
    };

    fetchCount();
  }, [type]);

  return (
    <Box className={classes.analyticsContainer}>
      <Box className={classes.analyticsItem}>
        <svg height="100" width="100" className={classes.analyticsSvg}>
          <circle cx="50" cy="50" r="40" stroke="black" strokeWidth="3" fill="white" />
          <text x="50%" y="50%" textAnchor="middle" stroke="#51c5cf" strokeWidth="1px" dy=".3em">
            {count}
          </text>
        </svg>
        <Typography variant="h6">
          {`We have ${count} vacancies available`}
        </Typography>
      </Box>
    </Box>
  );
};

export default Analytics;