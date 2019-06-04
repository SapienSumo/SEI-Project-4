import React from 'react'
import Auth from '../lib/Auth'
import axios from 'axios'

class BookNew extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      author: [],
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {

    axios(`/api/books/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))

    axios('/api/authors')
      .then(res => this.setState({ author: res.data }))

  }

  handleChange(e) {
    const data = {...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken('token')

    axios.post('/api/books', this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  render() {
    if(!this.state) return null
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">
              <form onSubmit={this.handleSubmit}>
                <div className="field">
                  <label className="label has-text-white">Title</label>
                  <div className="control">
                    <input
                      className="input"
                      name="name"
                      placeholder="eg: Brie"
                      onChange={this.handleChange}
                    />
                  </div>

                  {this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}

                </div>

                <div className="control">
                  <p className="has-text-white">Select an Author</p>
                  <div className="select is-loading">
                    <select name="author_id" onChange={this.handleChange}>
                      {this.state.author.map(author =>
                        <option value={author._id} key={author._id}>{author.name}</option>
                      )}
                    </select>
                  </div>
                </div>

                <div className="field">
                  <label className="label has-text-white">Image</label>
                  <div className="control">
                    <input
                      className="input"
                      name="image"
                      placeholder=""
                      onChange={this.handleChange}
                    />
                  </div>

                  {this.state.errors.Image && <div className="help is-danger">{this.state.errors.Image}</div>}

                </div>

                <button className="button is-primary">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default BookNew
