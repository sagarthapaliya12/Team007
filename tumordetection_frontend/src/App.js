
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera'
import './App.css';
import { Header, MainWrapper } from './header';

function App() {
  return (

    <MainWrapper>
      <div className='test'>
        <Header className='header'>TUMO</Header>
      </div>
      <div className='mid-bar'></div>
      <div className='area'>
      <div className='button-container'>
        <Button classname="but" style={{
          maxWidth: "8rem",
          maxHeight: "2rem",
          minWidth: "10rem",
          minHeight: "3rem"
        }} variant="contained" component="label">
          Upload
          <input hidden accept="image/*" multiple type="file" />
        </Button>

        <IconButton color="primary" aria-label="upload picture" component="label">
          <input hidden accept="image/*" type="file" />
          <PhotoCameraIcon style={{
            zIndex: 111,
            maxWidth: "1rem",
            maxHeight: "2rem",
            minWidth: "6rem",
            minHeight: "3rem"
          }} />
        </IconButton>
      </div>


        <ul class="circles">
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
    </MainWrapper>
  );
}

export default App;
