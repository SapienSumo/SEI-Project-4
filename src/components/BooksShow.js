import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Auth from '../lib/Auth'

class BooksShow extends React.Component {

  constructor(props) {
    super(props) // because this component needs `this.props`

    this.state = {
      cheese: null
    }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {

    axios.get(`/api/books/${this.props.match.params.id}`)
      .then(res => this.setState({ name: res.data }))
  }

  handleDelete() {
    const token = Auth.getToken()
    axios.delete(`/api/books/${this.props.match.params.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
  }

  canModify() {
    return Auth.isAuthenticated() && Auth.getPayload().sub === this.state.name.user._id
  }

  render() {
    if(!this.state.name) return null
    return (
      <section className="section">
        <div className="container">
          <div className="level">
            <div className="level-left">
              <h1 className="title is-1">{this.state.name.author}</h1>
            </div>
            {this.canModify() &&
              <div className="level-right">
                <Link to={`/books/${this.state.name._id}/edit`} className="button is-primary">Edit</Link>
                <button className="button is-danger" onClick={this.handleDelete}>Delete</button>
              </div>
            }
          </div>
          <hr />

          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">
              <figure className="image">
                <img src={this.state.name} alt={this.state.name.author} />
              </figure>
            </div>

            <div className="column is-half-desktop is-full-tablet">
              <h2 className="title is-2">{this.state.name.genres}</h2>
              <hr />
              <h2 className="title is-2">Tasting Notes</h2>
              <p className="is-size-4">{this.state.name.genres}</p>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default BooksShow
