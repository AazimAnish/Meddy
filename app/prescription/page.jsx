"use client"
import React from 'react'
import Sidebar from '../../components/Sidebar'
import { usePathname } from 'next/navigation'

const page = () => {
    const pathname = usePathname()
    console.log(pathname)
  return (
    <div>
      <Sidebar path={pathname}/>
      <div>

      </div>
    </div>
  )
}

export default page