"use client"
import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function ViewPatients() {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        // Fetch data from the API
        axios.get('/api/get-appointments')
            .then(response => {
                console.log(response.data)
                // Assuming response.data contains an array of patient objects with firstname, lastname, and uhid properties
                setPatients(response.data);
            })
            .catch(error => {
                console.error('Error fetching patients:', error);
            });
    }, []);

    return (
        <div className="bg-white h-screen p-10">
            <h2 className="font-bold text-2xl">Today's Appointments</h2>
            <div className="p-20">
                <ul role="list" className="divide-y divide-gray-500 bg-white">
                    {patients.length>0 && patients.map((patient, index) => (
                        <li key={index} className="flex justify-between gap-x-6 py-5 cursor-pointer border-b-2 border-t-2 border-gray-400 hover:bg-gray-200 px-3">
                            <div className="flex min-w-0 gap-x-4">
                                <div className="min-w-0 flex-auto">
                                    <p className="text-sm font-semibold leading-6 text-gray-900">{`${patient.firstName} ${patient.lastName}`}</p>
                                    <p className="mt-1 truncate text-xs leading-5 text-gray-500">UHID: {patient.uhid}</p>
                                </div>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
