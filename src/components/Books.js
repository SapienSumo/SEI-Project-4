import React from 'react'

const Books = ({ name, author }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-header-tilte">{name}</h3>
      </div>
      <div className="card-image">
        <figure className="image">
          <img />
        </figure>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{author}</p>
        </div>
      </div>
    </div>
  )
}

export default Books
