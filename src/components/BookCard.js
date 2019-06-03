import React from 'react'

const BookCard = ({ name, image }) => {
  return (
    <div className="card bookcover">
      <div className="card-header">
      </div>
      <div className="card-image">
        <figure className="image">
          <img src={image} className="archive-images" alt={name}/>
        </figure>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{name}</p>
        </div>
      </div>
    </div>
  )
}

export default BookCard
