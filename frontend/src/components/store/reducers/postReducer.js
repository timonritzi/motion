import { useState } from 'react'
import { connect } from 'react-redux'
import { List_all_Posts, Search_Post } from '../../../constants'
import { Create_new_Post } from "../../../constants/index"
// import { GET_SPECIFIC_POST } from '../../constants'
import {like_post} from "../../../constants/index"

const initialState = { 
    postsAllChron: [],
    newPost: "tomin",
    specificPost: "",
    
}


export default function postReducer (state = initialState, action) {
    
    switch (action.type) {
        case List_all_Posts: {
            return {
                ...state,
                postsAllChron: action.payload
            }


        }
        case Create_new_Post: {
            const newState = {...state}
            newState.newPost = action.payload
            return newState
        }
        case Search_Post: {
            const newState = {...state}
            newState.postsAllChron = action.payload
            return newState
        }
        // case like_post: {
        //     const old_index = action.payload
        //     return {
        //         ...state, 
        //         postsAllChron: [...state.postsAllChron.old_index] = action.payload
                
                
        //     }
        // }
        default: {
            return state
        }
    }

   
}

