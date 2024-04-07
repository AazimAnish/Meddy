"use client"
import React, { useState } from 'react';
import Sidebar from '../../../components/Sidebar';
import { usePathname } from 'next/navigation';
import Search from '../../../components/Search';
import axios from 'axios'; // Import Axios library

const Page = () => {
    const pathname = usePathname();
    const [medInputs, setMedInputs] = useState([{ id:1 , medicine: '', timings: ['Morning', 'Lunch', 'Night'] }]);
    const uhidVar = `${pathname.split('/')[2]}`
    const [patientData, setPatientData] = useState();
    const [appointmentData, setAppointmentData] = useState();


    const options = [
        "Aspirin",
        "Paracetamol",
        "Ibuprofen",
        "Amoxicillin",
        "Penicillin",
        "Ciprofloxacin",
        "Prednisone",
        "Lisinopril",
        "Atorvastatin",
        "Metformin"
    ];

    const handleSearchInputChange = (id, medicine) => {
        setMedInputs(prevMedInputs => {
            const updatedInputs = prevMedInputs.map(input => input.id === id ? { ...input, medicine } : input);
            return updatedInputs;
        });
    };
    

    // Callback function to add a new search input
    const handleAddMore = (e) => {
        e.preventDefault();
        const newId = medInputs.length + 1;
        setMedInputs([...medInputs, { id: newId, medicine: '', timings: []}]);
    };

    const handleCheckboxChange = (index, timing) => {
        setMedInputs(prevMedInputs => {
            const newMedInputs = [...prevMedInputs]; // Create a copy of the medInputs array
            console.log("newMedInputs:", newMedInputs);
            console.log("index:", index);
            // Ensure that newMedInputs[index] is not undefined
            if (newMedInputs[index]) {
                // Toggle the presence of timing in the timings array of the specific medicine object
                if (newMedInputs[index].timings?.includes(timing)) {
                    newMedInputs[index].timings = newMedInputs[index].timings.filter(t => t !== timing);
                } else {
                    newMedInputs[index].timings?.push(timing);
                }
            }
            console.log("Updated timings:", newMedInputs[index]?.timings);
            return newMedInputs; // Return the updated medInputs array
        });
    };

    const fetchPatientData = async() => {
        // Fetch user data based on the uhid
        await axios.get(`/api/view-patients/${uhidVar}`)
            .then(response => {
                // Set the user data from the response
                console.log(response.data,"response.data view patients ")
                setPatientData(response.data);
               // return response.data;
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }
    
    const fetchAppoinment = async() => {
        // Fetch user data based on the uhid
        await axios.get(`/api/get-appointments/${uhidVar}`)
            .then(response => {
                console.log(response.data,"response.data get appointments")
                // Set the user data from the response
                setAppointmentData(response.data);
               // return response.data;
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }
    

    const handleSubmit = async(e) => {
        e.preventDefault();
        // Make Axios POST request to submit form data
        const patient = await fetchPatientData();
        const appointment = await fetchAppoinment();
        console.log(patientData,appointmentData,"patient",patient,appointment)

        const newMedInputs = {
            DoctorName :  appointmentData.doctor,
            HospitalName : "Rajagiri hospital",
            Doctor_specialization : appointmentData.speciality,
            uhid : uhidVar,
            Medicines : medInputs,
            patient : patientData,
        }

        console.log(newMedInputs,"newmedinputs")
       
    };

    return (
        <div>
            <Sidebar path={pathname} />
            <div className='bg-white ml-[18rem] h-screen w-full overflow-hidden'>
                <h1 className='pt-10 pl-20 font-bold text-2xl'>Add prescription</h1>
                <form className="w-full pt-10 ml-20 space-y-8">
                    <div className='flex  justify-start items-end space-x-4'>
                        <div className='space-y-10'>
                            {medInputs.map((medInput, index) => (
                                <div key={index} className='flex justify-center items-center'>
                                    <Search
                                        options={options}
                                        key={medInput.id}
                                        value={medInput.medicine}
                                        id={medInput.id}
                                        onSearchInput={handleSearchInputChange}
                                        name="medicine"
                                    />
                                    <div className='flex ml-10'>
                                        <input
                                            type='checkbox'
                                            value="Morning"
                                            checked={medInput.timings && medInput.timings.includes('Morning')}
                                            onChange={(e) => handleCheckboxChange(index, 'Morning')}
                                        />
                                        <label htmlFor="">Morning</label>
                                    </div>
                                    <div className='ml-10'>
                                        <input
                                            type='checkbox'
                                            value="Lunch"
                                            checked={medInput.timings && medInput.timings.includes('Lunch')}
                                            onChange={(e) => handleCheckboxChange(index, 'Lunch')}
                                        />
                                        <label htmlFor="">Lunch</label>
                                    </div>
                                    <div className='ml-10'>
                                        <input
                                            type='checkbox'
                                            value="Night"
                                            checked={medInput.timings && medInput.timings.includes('Night')}
                                            onChange={(e) => handleCheckboxChange(index, 'Night')}
                                        />
                                        <label htmlFor="">Night</label>
                                    </div>
                                    </div>
                            ))}
                        </div>
                    </div>
                    <div className='flex space-x-5 w-1/2 justify-end items-end -ml-40'>
                        <button className='px-5 bg-indigo-600 py-2 text-white rounded-xl' onClick={handleAddMore}>+ Add more</button>
                        <button  className='px-5 text-indigo-600 py-2 bg-white border-2 border-gray-500 rounded-xl' onClick={handleSubmit}>Submit</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default Page;
