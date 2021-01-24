import {postCreate, listPosts, search_Post } from "../constants/index"
import {like} from "../constants/index"


// action creator
export const setPostData = (type, data) => {
    return {
        type: type,
        payload: data,
    }
} 

export const postAction = (body, type) => async (dispatch, getState) => {   
    const { userLoginReducer:{ token } } = getState();    
    const config = {
        method: "POST",
        headers: new Headers({
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        }),
        body: body
    };

    const response = await fetch(postCreate, config)
    const data = await response.json();
    dispatch(setPostData(type, data));
};

export const listPost = (type) => async (dispatch, getState) => {
    const { userLoginReducer:{ token } } = getState();
    const config = {
        method: "GET",
        headers: new Headers({
            "Authorization": `Bearer ${token}`,
            "Content-Type" : "application/json"
        }),
        
    }

    const response = await fetch(listPosts, config)
    const data = await response.json();
    dispatch(setPostData(type, data))
    
    console.log(data);
}


export const likePost = (type, postId, body) => async (dispatch, getState) => {
    const { userLoginReducer:{ token } } = getState();
    const config = {
        method: "POST",
        headers: new Headers({
            "Authorization": `Bearer ${token}`,
            "Content-Type" : "application/json"
        }),
        body: body
        
    }

    const response = await fetch(like + postId +"/", config)
    const data = await response.json();
    dispatch(setPostData(type, data.id))
    console.log("post",data);
}

export  const searchPost = (param, type) => async (dispatch, getState) => {
    const { userLoginReducer:{ token } } = getState()
    const config = {
        method: "GET",
        headers: new Headers({
            "Authorization": `Bearer ${token}`,
            "Content-Type" : "application/json"
        }),
        param: param
    }

    const response = await fetch(`https://motion-timon.propulsion-learn.ch/backend/api/social/posts/search/?search=${param}`, config)
    const data = await response.json();
    dispatch(setPostData(type, data))
    console.log("get", data);
}
