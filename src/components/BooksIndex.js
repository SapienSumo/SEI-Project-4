import React from 'react'
import { Link } from 'react-router-dom'

import BookCard from './Bookcard'

class BooksIndex extends React.Component {

  constructor(){
    super()

    this.state = {
      books: []
    }

    this.handleSearch = this.handleSearch.bind(this)
  }

  componentDidMount() {
    fetch('/api/books')
      .then(res => res.json())
      .then(data => this.setState({ books: data }))
  }

  handleSearch(e) {
    this.setState({ term: e.target.value })
  }

  filteredBooks() {
    const re = new RegExp(this.state.term, 'i')
    return this.state.books.filter(book => re.test(book.name))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="control">
            <input className="input searchbar" type="text" name="name" placeholder="Search..." onChange={this.handleSearch}></input>
          </div>
          <div className="columns is-multiline">
            {this.filteredBooks().map(book =>
              <div key={book.id} className="column is-3-desktop is-one-third-tablet">
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
