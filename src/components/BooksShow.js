import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Auth from '../lib/Auth'

class BooksShow extends React.Component {

  constructor(props) {
    super(props) // because this component needs `this.props`

    this.state = {
      book: null
    }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {

    axios.get(`/api/books/${this.props.match.params.id}`)
      .then(res => this.setState({ book: res.data }))
  }

  handleDelete() {
    const token = Auth.getToken()
    axios.delete(`/api/books/${this.props.match.params.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
  }

  canModify() {
    return Auth.isAuthenticated() && Auth.getPayload().sub === this.state.book.user.id
  }

  render() {
    if(!this.state.book) return null
    return (
      <section className="section">
        <div className="container showpage">
          <div className="level">
            <div className="level-left">
              <h1 className="title is-1 has-text-white">{this.state.book.name}</h1>
            </div>
            {this.canModify() &&
              <div className="level-right">
                <Link to={`/books/${this.state.book.id}/edit`} className="button is-light">Edit</Link>
                <button className="button is-dark" onClick={this.handleDelete}>Delete</button>
              </div>
            }
          </div>
          <hr />

          <div
            className="art-image"
            style={{backgroundImage: `url(${this.state.book.image})` }} >

          </div>

          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">
              <figure className="image is-2by3">
                <img src={this.state.book.image} className="img-showpage" alt={this.state.book.name} />
              </figure>
            </div>

            <div className="column is-half-desktop is-full-tablet">
              <h2 className="title is-2 has-text-white">{this.state.book.author.name}</h2>
              <hr />
              <p className="has-text-white">100,000 years ago, at least six human species inhabited the earth. Today there is just one. Us. Homo sapiens. How did our species succeed in the battle for dominance? Why did our foraging ancestors come together to create cities and kingdoms? How did we come to believe in gods, nations and human rights; to trust money, books and laws; and to be enslaved by bureaucracy, timetables and consumerism? And what will our world be like in the millennia to come?

              In Sapiens, Dr Yuval Noah Harari spans the whole of human history, from the very first humans to walk the earth to the radical – and sometimes devastating – breakthroughs of the Cognitive, Agricultural and Scientific Revolutions. Drawing on insights from biology, anthropology, palaeontology and economics, he explores how the currents of history have shaped our human societies, the animals and plants around us, and even our personalities. Have we become happier as history has unfolded? Can we ever free our behaviour from the heritage of our ancestors? And what, if anything, can we do to influence the course of the centuries to come? </p>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default BooksShow
