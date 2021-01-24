import React, {Component, useEffect, useState} from 'react';
import "../../sass/updateProfile/updateprofile.scss";
import {useDispatch, useSelector} from "react-redux";
import {userAction} from "../../actions/userAction";
import {ABOUT_USER, update_profile_url,} from "../../constants";
import axios from "axios";



export const UpdateProfile = ({data},props) => {

        const token = localStorage.getItem("token")
        console.log(token)
        const dispatch = useDispatch();

        const aboutMe = useSelector((state) => state.userReducer.aboutMe)

        useEffect(() => {
                const userData = async () => {
                        await dispatch(userAction(ABOUT_USER))
                }
                userData();
                console.log("aboutMEEEEEEEEEE", data)
            },[]);

        console.log(aboutMe.email);

        const [email, setEmail] = useState('')
        const [username, setUsername] = useState('')
        const [first_name, setFirstName] = useState('')
        const [last_name, setLastName] = useState('')
        const [phone, setPhone] = useState('')
        const [about, setAbout] = useState('')
        const [location, setLocation] = useState('')

        const handleSubmit = (event) => {
                                let fd = new FormData();

                if (email !== undefined) {

                        fd.append('email', email);
                }

                if (username !== undefined) {

                        fd.append('username', username);
                }

                if (about !== undefined) {

                        fd.append('about', about);
                }

                if (first_name !== undefined) {

                        fd.append('first_name', first_name);
                }

                if (last_name !== undefined) {

                        fd.append('last_name', last_name);
                }

                if (phone !== undefined) {

                        fd.append('phone', phone);
                }

                if (location !== undefined) {

                        fd.append('location', location);
                }

                fd.append('_method', 'PATCH');

                console.log(fd);

                axios.patch(update_profile_url, fd,
                    {
                            headers: {
                                    'Authorization': `Bearer ${token}`
                            }
                    })
                    .then((response) => {
                            console.log(response);

                    })
                    .catch((error) => {
                            if (error.response) {
                              // The request was made and the server responded with a status code
                              // that falls out of the range of 2xx
                              console.log(error.response.data);
                              console.log(error.response.status);
                              console.log(error.response.headers);}
                    });
        }




        return (

            <div className="container-profile profile-update">

                    <div className="profile">

                        <div className="content-left">

                                <div className="avatar-update">
                                        <img alt="" src={aboutMe.avatar} />
                                        <button className="update-image">UPDATE IMAGE</button>
                                </div>

                                <div className="delete-save-acc">
                                        <button className="delete-button">DELETE</button>
                                        <button className="save-button" onClick={handleSubmit} >SAVE</button>
                                </div>

                        </div>

                        <div className="content-right">

                                <div className="top-right">

                                        <div className="content-top-left">

                                                <div className="first-name">
                                                        <div>First Name</div>
                                                        <input name="first_name" onChange={(event) => setFirstName(event.target.value)} defaultValue={aboutMe.first_name} type="text" />
                                                </div>

                                                <div className="email">
                                                        <div>Email</div>
                                                        <input name="email" onChange={(event) => setEmail(event.target.value)} defaultValue={aboutMe.email} type="text"/>
                                                </div>

                                                <div className="location">
                                                        <div>Location</div>
                                                        <input name="first_name" onChange={(event) => setLocation(event.target.value)} defaultValue={aboutMe.location} type="text"/>
                                                </div>

                                                <div className="about">
                                                        <div>About</div>
                                                        <input name="first_name" onChange={(event) => setAbout(event.target.value)} defaultValue={aboutMe.about} type="text"/>
                                                </div>

                                        </div>

                                        <div className="content-top-right">


                                                <div className="last-name">
                                                        <div>Last Name</div>
                                                        <input name="last_name" onChange={(event) => setLastName(event.target.value)} defaultValue={aboutMe.last_name} type="text"/>
                                                </div>

                                                <div className="username">
                                                        <div>Username</div>
                                                        <input name="username" onChange={(event) => setUsername(event.target.value)} defaultValue={aboutMe.username} type="text"/>
                                                </div>

                                                <div className="phone">
                                                        <div>Phone</div>
                                                        <input name="phone" onChange={(event) => setPhone(event.target.value)} defaultValue={aboutMe.phone} type="text"/>
                                                </div>

                                                <div className="password">
                                                        <div>Password</div>
                                                        <input name="password" defaultValue={"adminadmin"} type="text"/>
                                                </div>

                                                </div>

                                </div>

                                <div className="bottom-right">
                                        <p>Interests</p>
                                        <form>
                                                <input placeholder="Type something..." name="things-user-likes"/>
                                                <button className="interests-button">ADD</button>
                                        </form>
                                </div>

                        </div>

              </div>

            </div>
        );

        }

export default UpdateProfile;