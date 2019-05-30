import React from 'react'
import { Link } from 'react-router-dom'

import BookCard from './BookCard'

class BooksIndex extends React.Component {

  constructor(){
    super()

    this.state = {
      books: []
    }
  }

  componentDidMount() {
    fetch('/api/books')
      .then(res => res.json())
      .then(data => this.setState({ books: data }))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-multiline">
            {this.state.books.map(book =>
              <div key={book.id} className="column is-one-quarter-desktop is-one-third-tablet">
                <Link to={`/books/${book.id}`}>
                  <BookCard {...book} />
                </Link>
              </div>
            )}

          </div>
        </div>
      </section>
    )
  }
}

export default BooksIndex
