import React from 'react'

const Table = ({ products }) => {
  return (
    <div className="relative ml-[18rem] overflow-x-auto shadow-md sm:rounded-lg bg-gray-200 h-screen">
      <table className="w-full text-sm text-left rtl:text-right text-black dark:text-gray-800">
        <thead className="text-xs text-black uppercase bg-gray-50 dark:bg-gray-200 dark:text-black ">
          <tr>
            <th scope="col" className="px-6 py-3">Bot Response</th>
            <th scope="col" className="px-6 py-3">Human Response</th>
            <th scope="col" className="px-6 py-3">Predictions</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product, index) => (
            <tr key={index} className="odd:bg-white odd:dark:bg-gray-300 even:bg-gray-50 even:dark:bg-gray-200 border-b dark:border-gray-700">
              <td className="px-6 py-4">{product.botResponse}</td>
              <td className="px-6 py-4">{product.humanResponse}</td>
              <td className="px-6 py-4">{product.prediction}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Table