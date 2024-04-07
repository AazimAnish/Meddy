"use client"
import React from 'react'
import Sidebar from '../../../components/Sidebar'
import {IoPersonCircleOutline} from 'react-icons/io5'
// import {path} from 'react-icons/gr'
import { usePathname } from 'next/navigation'
import { pathToFileURL } from 'url'

function page() {
  const path = usePathname()
  const base = `/${path.split('/')[1]}`;

  return (
    <div className=''>
        <Sidebar path={base}/>
        <div className='bg-white  z-30 w-auto h-full text-black'>
        <div class='flex max-w-full ml-[19rem] rounded-xl flex-col bg-white mr-5'>
        <div class='bg-[rgb(48,57,114)] h-[6rem] w-full rounded-t-xl justify-start flex flex-row gap-x-[35rem] max-w-content'>
            <div class='h-[8rem] w-[8rem] rounded-full bg-white m-5 items-center justify-center flex z-0'>
            <label for='profile-picture-input'>
                <img src='../images/profile.jpg' class='m-auto object-fit h-[7rem] w-[7rem] rounded-full bg-white cursor-pointer' fill='#303972'/>
            </label>
            <input
                type='file'
                accept='image/*'
                id='profile-picture-input'
                class='hidden'
            />
            </div>
            <div class='mb-0 flex relative '>
            <div class='w-[10rem] h-[5rem] rounded-b-full bg-[#FCC43E] transform rotate-180 !top-4 left-10 absolute z-25'></div>
            <div class='w-[8rem] h-[4rem] rounded-b-full bg-[#FB7D5B] transform rotate-180 !top-8 absolute z-0'></div>
            </div>
        </div>
  <div class='mt-[4rem] relative h-auto'>
    <div class='flex flex-row justify-between max-h-6 items-start'>
      <h2 class='font-bold text-dark-blue ml-5 text-2xl flex-initial'>John Doe</h2>
      {/* <Link to='/dashboard/innovator/profile/edit'>
        <img src='edit.svg' alt='edit' class='h-20 w-20 cursor-pointer mr-4' />
      </Link> */}
    </div>
    <h4 class='text-gray-500 ml-5 mt-2'>Patient</h4>
    <div class='grid grid-cols-3 grid-rows-2 gap-4 ml-5 mt-2 gap-y-10'>
      <div class='flex flex-col'>
        <label class='text-[#A098AE]'>Location</label>
        <div class='flex flex-row gap-4 mt-3'>
          {/* <GrLocation class='mt-1' fill='#FB7D5B' /> */}
          <p class='- text-dark-blue'>New York</p>
        </div>
      </div>
      <div class='flex flex-col'>
        <label class='text-[#A098AE]'>Phone number</label>
        <div class='flex flex-row gap-4 mt-3'>
          {/* <BsFillTelephoneFill class='mt-1' fill='#FB7D5B' /> */}
          <p class='font-semibold text-dark-blue'>123-456-7890</p>
        </div>
      </div>
      <div class='flex flex-col'>
        <label class='text-[#A098AE]'>Email id</label>
        <div class='flex flex-row gap-4 mt-3'>
          {/* <MdEmail class='mt-1' fill='#FB7D5B ' size='20' /> */}
          <p class='font-semibold text-dark-blue'>johndoe@example.com</p>
        </div>
      </div>
      <div class='flex flex-col'>
        <label class='text-[#A098AE]'>Date of birth</label>
        <div class='flex flex-row gap-4 mt-3'>
          <p class='font-semibold text-dark-blue'>01/01/1990</p>
        </div>
      </div>
      <div class='flex flex-col'>
        <label class='text-[#A098AE]'>Address</label>
        <div class='flex flex-row gap-4 mt-3'>
          <p class='font-semibold text-dark-blue'>123 Main Street</p>
        </div>
      </div>
    </div>
    <hr class='bg-black w-full mt-5'></hr>
    <div class='flex flex-col ml-5 gap-y-10 mt-5 '>
      <div>
        <label class='text-[#A098AE]'>Bio</label>
        <div class='flex flex-row gap-4 mt-3'>
          <p class='font-semibold text-dark-blue'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget justo eu sem vehicula rutrum.</p>
        </div>
        <hr class='bg-black w-full mt-5'></hr>
      </div>
      <div class='flex flex-row gap-[30rem] mb-5'>
        <div class='flex flex-col'>
          <label class='text-[#A098AE]'>Interest</label>
          <div class='flex flex-row gap-2 mt-3'>
            <p class='font-semibold text-dark-blue'>Programming , Design , Music</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

        </div>
    </div>
  )
}

export default page
