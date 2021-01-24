import React, {Component, useEffect, useState} from 'react';
import "../../sass/searchbar/searchbar.scss";
import { useDispatch} from 'react-redux';
import searchIcon from "../../assets/homeFeed/svgs/search_icon.svg"
import {searchPost} from "../../actions/postAction";
import {Search_Post} from "../../constants";


export const Searchbar = (props) => {

    const dispatch = useDispatch();
    const [searchContent, setsearchContent] = useState("")

    const searchHandler = (event) => {
        setsearchContent(event.currentTarget.value)
        const param = searchContent
        dispatch(searchPost(param, Search_Post))
    }




        return (

            
                
                <div className="search">

                    <div className="left">
                        
                        <img src={searchIcon} />
                        <input type="text" id="search" placeholder="Search posts..." onChange={searchHandler}/>

                    </div>

                    <div className="right">


                            <div className="liked">                     

                                <p>Liked</p>

                            </div>

                            <div className="friends">

                                <p>Friends</p>

                            </div>

                            <div className="follow">

                                <p>Follow</p>

                            </div>

                    </div>

                </div>

            
        );

}
