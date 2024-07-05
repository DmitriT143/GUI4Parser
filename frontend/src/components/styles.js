import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  container: {
    marginTop: theme.spacing(4),
    backgroundColor: theme.palette.background.default,
    color: theme.palette.text.primary,
  },
  heading: {
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    color: theme.palette.primary.contrastText,
    backgroundColor: theme.palette.primary.main,
    padding: theme.spacing(2),
    borderRadius: theme.shape.borderRadius,
    borderBottom: `2px solid ${theme.palette.common.white}`,
  },
  filterContainer: {
    marginBottom: theme.spacing(4),
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.contrastText,
    padding: theme.spacing(2),
    borderRadius: theme.shape.borderRadius,
  },
  listContainer: {
    marginTop: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.primary,
    backgroundColor: '#600C5C',
  },
  card: {
    minHeight: '200px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'space-between',
    backgroundColor: '#780f74',
    color: theme.palette.text.secondary,
  },

  title: {
    flexGrow: 1,
  },
  
  analyticsContainer: {
    display: 'flex',
    justifyContent: 'space-around',
    alignItems: 'center',
    marginTop: theme.spacing(4),
  },
  analyticsItem: {
    textAlign: 'center',
  },
  analyticsSvg: {
    marginBottom: theme.spacing(2),
  },
}));


export default useStyles;