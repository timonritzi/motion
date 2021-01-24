import { USER_LOGIN, USER_TOKEN } from "../../src/constants/index";
import { authentication } from "../constants/index";


export const userLoginAction = user => ({
    type: USER_LOGIN,
    payload: user,
});


export const userLogin = data => async (dispatch, getState) => {
    console.log("data", data);

    const headers = new Headers({
        'Content-Type': 'application/json'
    });

    const body = JSON.stringify(data)

    const config = {
        headers,
        body,
        method: 'POST',
    }

    const response = await fetch(`${ authentication }`, config);
    const user = await response.json();
    const { access } = user;

    console.log("User", user.user);
    console.log("token", access);

    if (access) {
        localStorage.setItem("token", access)
        dispatch(userLoginAction({ user: user, authenticated: true}));
    } else {
        dispatch(userLoginAction({ user: "", authenticated: false}));
    }
    return user;


}

export const saveToken = token => ({
    type: USER_TOKEN,
    payload: token,
}) // We should fetch /ME for the user Data, like "Whats on your mind, USER" and for the avatar

