import React, { Component } from 'react';
import Header from "../../components/header/header";
import UpdateProfile from "../../components/profile/updateProfile";


const UpdateProfilePage = () => {

    return(
        <div className="main">

            <Header/>
            <UpdateProfile/>

        </div>
    );
};

export default UpdateProfilePage;