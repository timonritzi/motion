import React from 'react';
import ReactDOM from 'react-dom';
import { store } from "./components/store/index";
import { Provider } from 'react-redux';
import Routes from './routes/routes';
import {saveToken} from "./actions/userLoginAction";


const token = localStorage.getItem("token");

if (token) {
  store.dispatch(saveToken(token));
}

ReactDOM.render(
  <Provider store = {store}>
    <Routes />
  </Provider>,
  document.getElementById('root')
);



