"use client"
import React, { useState,useEffect } from 'react';
import Sidebar from '../../../components/Sidebar';
import axios from 'axios';
import { IoPersonCircleOutline } from 'react-icons/io5';
import { usePathname } from 'next/navigation';

function Page() {
  const [userData, setUserData] = useState({
    firstName: 'John',
    lastName: 'Doe',
    email: 'johndoe@example.com',
    country: 'United States',
    streetAddress: '123 Main Street',
    city: 'New York',
    region: 'NY',
    postalCode: '10001',
    phone: '123-456-7890',
    dob: '01/01/1990',
    maritalStatus: 'Single',
    uhid: '1234567890'
  });

  const path = usePathname();
  const base = `/${path.split('/')[1]}`
  const uhidVar = `${path.split('/')[2]}`

  useEffect(() => {
    // Fetch user data based on the uhid
    axios.get(`/api/view-patients/${uhidVar}`)
      .then(response => {
        // Set the user data from the response
        setUserData(response.data);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }, [uhidVar]);

  return (
    <div className="">
      <Sidebar path={base} />
      <div className="bg-white  z-30 w-auto  text-black h-screen">
        <div className="flex max-w-full ml-[19rem] rounded-xl flex-col bg-white mr-5">
          <div className="bg-[rgb(48,57,114)] h-[6rem] w-full rounded-t-xl justify-start flex flex-row gap-x-[35rem] max-w-content">
            <div className="h-[8rem] w-[8rem] rounded-full bg-white m-5 items-center justify-center flex z-0">
              <label htmlFor="profile-picture-input">
                <IoPersonCircleOutline className="m-auto object-fit h-[9rem] w-[9rem] rounded-full bg-white cursor-pointer" fill="#303972" alt="Profile" />
              </label>
              <input
                type="file"
                accept="image/*"
                id="profile-picture-input"
                className="hidden"
              />
            </div>
            <div className="mb-0 flex relative ">
              <div className="w-[10rem] h-[5rem] rounded-b-full bg-[#FCC43E] transform rotate-180 !top-4 left-10 absolute z-25"></div>
              <div className="w-[8rem] h-[4rem] rounded-b-full bg-[#FB7D5B] transform rotate-180 !top-8 absolute z-0"></div>
            </div>
          </div>
          <div className="mt-[4rem] relative h-auto">
            <div className="flex flex-row justify-between max-h-6 items-start">
              <h2 className="font-bold text-dark-blue ml-5 text-2xl flex-initial">{userData.firstName} {userData.lastName}</h2>
            </div>
            <h4 className="text-gray-500 ml-5 mt-2">Patient {userData.uhid}</h4>
            <div className="grid grid-cols-3 grid-rows-2 gap-4 ml-5 mt-2 gap-y-10">
              <div className="flex flex-col">
                <label className="text-[#A098AE]">Location</label>
                <div className="flex flex-row gap-4 mt-3">
                  <p className="- text-dark-blue">{userData.city}, {userData.region}</p>
                </div>
              </div>
              <div className="flex flex-col">
                <label className="text-[#A098AE]">Phone number</label>
                <div className="flex flex-row gap-4 mt-3">
                  <p className="font-semibold text-dark-blue">{userData.phone}</p>
                </div>
              </div>
              <div className="flex flex-col">
                <label className="text-[#A098AE]">Email id</label>
                <div className="flex flex-row gap-4 mt-3">
                  <p className="font-semibold text-dark-blue">{userData.email}</p>
                </div>
              </div>
              <div className="flex flex-col">
                <label className="text-[#A098AE]">Date of birth</label>
                <div className="flex flex-row gap-4 mt-3">
                  <p className="font-semibold text-dark-blue">{userData.dob}</p>
                </div>
              </div>
              <div className="flex flex-col">
                <label className="text-[#A098AE]">Address</label>
                <div className="flex flex-row gap-4 mt-3">
                  <p className="font-semibold text-dark-blue">{userData.streetAddress}</p>
                </div>
              </div>
              <div className="flex flex-col">
                <label className="text-[#A098AE]">Maritial status</label>
                <div className="flex flex-row gap-4 mt-3">
                  <p className="font-semibold text-dark-blue">{userData.maritalStatus}</p>
                </div>
              </div>
            </div>
            <hr className="bg-black w-full mt-5"></hr>
            <div className="flex flex-col ml-5 gap-y-10 mt-5 ">
              <div className="flex flex-row gap-[30rem] mb-5">
                <div className="flex flex-col">
                  <label className="text-[#A098AE]">Interest</label>
                  <div className="flex flex-row gap-2 mt-3">
                    <p className="font-semibold text-dark-blue">Programming, Design, Music</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Page;
