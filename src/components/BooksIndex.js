import React from 'react'
import { Link } from 'react-router-dom'

import Books from './Books'

class BooksIndex extends React.Component {

  constructor(){
    super()

    this.state = {
      name: []
    }
  }

  componentDidMount() {
    fetch('/api/books')
      .then(res => res.json())
      .then(data => this.setState({ cheeses: data }))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-multiline">
            {this.state.name.map(name =>
              <div key={name._id} className="column is-one-quarter-desktop is-one-third-tablet">
                <Link to={`/books/${name._id}`}>
                  <Books {...name} />
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
