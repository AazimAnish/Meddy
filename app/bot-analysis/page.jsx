import React from 'react'
import Sidebar from '../../components/Sidebar'
import Table from '../../components/Table.jsx'

const page = () => {

  const products = [
    { 
      botResponse: 'Hi, how are you?', 
      humanResponse: 'I am not so fine, having a temperature rise.', 
      prediction: 'Fever symptoms detected. More info required to confirm what type of fever.' 
    },
    { 
      botResponse: 'Fever is not a good symptom. Do you have any other illness like headache or other?', 
      humanResponse: 'Yeah, small headache and skin rashes.', 
      prediction: 'There is a possibility of dengue or malaria. Still not confirmed.' 
    },
    { 
      botResponse: 'Have you been in contact with anyone who is sick?', 
      humanResponse: 'No, I have not been in contact with anyone sick.', 
      prediction: 'Possible viral infection. Recommend further tests.' 
    },
    { 
      botResponse: 'How long have you been feeling these symptoms?', 
      humanResponse: 'I have been feeling these symptoms for the past 3 days.', 
      prediction: 'Early stage of illness detected. Immediate medical attention required.' 
    },
    { 
      botResponse: 'Do you have any allergies?', 
      humanResponse: 'No, I do not have any known allergies.', 
      prediction: 'No allergies detected. Suitable for most treatments.' 
    },
  ]

  return (
    <div>
      <Sidebar/>
      <Table products={products} />
    </div>
  )
}

export default page