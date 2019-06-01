import React from 'react'

const BookCard = ({ name, genres, author, image }) => {
  return (
    <div className="card bookcover">
      <div className="card-header">
        <h3 className="card-header-tilte">{name}</h3>
      </div>
      <div className="card-image">
        <figure className="image">
          <img src={image} alt={name}/>
        </figure>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{author.name}</p>
          <p>{genres.name}</p>
        </div>
      </div>
    </div>
  )
}

export default BookCard
