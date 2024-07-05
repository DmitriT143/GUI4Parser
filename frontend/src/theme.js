import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#A69080', // Indigo color
    },
    secondary: {
      main: '#f50057',
    },
    background: {
      default: '#A69080', // Indigo background for the entire page
    },
    text: {
      primary: '#ffffff', // White text for primary content
      secondary: '#000000', // Black text for secondary content
    },
  },
  spacing: 8, // Default spacing is 8
});

export default theme;