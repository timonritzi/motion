import { USER_LOGIN, USER_LOGOUT, USER_TOKEN } from '../../../constants/index';




export const initalState = {

    user: null,
    token: null,
    authenticated: false,
};

 const userLoginReducer = (state = initalState, action) => {

    switch (action.type) {

        case USER_LOGIN: {
            return {
                user: action.payload.user.user,
                token: action.payload.user.access,
                authenticated: action.payload.authenticated,
            };
        }
        case USER_LOGOUT: {
            console.log(action)
            return {
                user: null,
                token: null,
                authenticated: null,
                
            };
            
        }
        case USER_TOKEN:
            return {
                token: action.payload,
                authenticated: true,
            }
        default:
            return state;
    }

}
export default userLoginReducer;
