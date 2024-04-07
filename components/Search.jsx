import React, { useState } from 'react';

export default function Search  ({ options,onSearchInput,id }) {
    const [searchText, setSearchText] = useState('');
    const [showSuggestions, setShowSuggestions] = useState(false);
    const [filteredSuggestions, setFilteredSuggestions] = useState([]);
  
    const handleInputChange = (e) => {
        const searchValue = e.target.value;
        setSearchText(searchValue);
        setShowSuggestions(true);

        // Filter suggestions based on the search value
        const filtered = options.filter(suggestion =>
            suggestion.toLowerCase().includes(searchValue.toLowerCase())
        );
        setFilteredSuggestions(filtered);

        // Pass the search input text back to the parent component
        onSearchInput(id, searchValue);
    };

    const handleSuggestionClick = (suggestion) => {
        setSearchText(suggestion);
        setShowSuggestions(false);
        onSearchInput(id, suggestion); // Call the callback function with the selected suggestion
    };
  
    return (
      <div className="search-container">
        <input
          type="text"
          value={searchText}
          onChange={handleInputChange}
          className='border-2 border-gray-500 py-2 px-4 rounded-lg '
          placeholder="Search..."
        />
        {showSuggestions && (
          <ul className="suggestions">
            {filteredSuggestions.map((suggestion, index) => (
              <li key={index} onClick={() => handleSuggestionClick(suggestion)}>
                {suggestion}
              </li>
            ))}
          </ul>
        )}
      </div>
    );
  };