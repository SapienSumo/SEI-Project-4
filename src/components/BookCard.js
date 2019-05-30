import React from 'react'

const BookCard = ({ name, author, genre }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-header-tilte">{name}</h3>
        <p>{author}</p>
        <p>{genre}</p>
      </div>
      <div className="card-content">
        <div className="content">
        </div>
      </div>
    </div>
  )
}

export default BookCard
