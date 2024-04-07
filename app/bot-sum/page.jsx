"use client"
import React from 'react'
import Sidebar from '../../components/Sidebar'
import { usePathname } from 'next/navigation'
import path from 'path'

const page = () => {
  const pathname = usePathname()
  return (
    <div>
      <Sidebar path={pathname}/>
      <div>
        
      </div>
    </div>
  )
}

export default page