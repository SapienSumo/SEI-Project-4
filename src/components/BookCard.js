import React from 'react'

const BookCard = ({ name, image }) => {
  return (
    <div className="card bookcover">
      <div className="card-header">
      </div>
      <div className="card-image">
        <figure className="image">
          <div
            className="archive-images"
            alt={name}
            style={{backgroundImage: `url(${image})`}}
          >
          </div>
        </figure>
      </div>
      <div className="card-content">
        <div className="content is-dark">
          <p>{name}</p>
        </div>
      </div>
    </div>
  )
}

export default BookCard
