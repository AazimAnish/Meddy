"use client"
import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function ViewPatients() {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        // Fetch data from the API
        axios.get('/viewpatients')
            .then(response => {
                // Assuming response.data contains an array of patient objects with firstname, lastname, and uhid properties
                setPatients(response.data);
            })
            .catch(error => {
                console.error('Error fetching patients:', error);
            });
    }, []);

    return (
        <div className="bg-white p-10">
            <h2 className="font-bold text-2xl">Today's Appointments</h2>
            <div className="p-20">
                <ul role="list" className="divide-y divide-gray-100 bg-white">
                    {patients.map((patient, index) => (
                        <li key={index} className="flex justify-between gap-x-6 py-5">
                            <div className="flex min-w-0 gap-x-4">
                                <div className="min-w-0 flex-auto">
                                    <p className="text-sm font-semibold leading-6 text-gray-900">{`${patient.firstname} ${patient.lastname}`}</p>
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
