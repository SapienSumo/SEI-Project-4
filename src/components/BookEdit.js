import React from 'react'
import Auth from '../lib/Auth'
import axios from 'axios'

class BookEdit extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      errors: {},
      author: []
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
    console.log(this.state.data)
  }

  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken('token')

    const data = {...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })

    axios.put(`/api/books/${this.state.data.id}`, this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  render() {
    console.log(this.state.data)
    if(!this.state) return null
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">
              <form onSubmit={this.handleSubmit}>
                <div className="field">
                  <label className="label has-text-white">Name</label>
                  <div className="control">
                    <input
                      className="input"
                      name="name"
                      placeholder=""
                      onChange={this.handleChange}
                      value={this.state.data.name || ''}
                    />
                  </div>
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
                      placeholder="https://bulma.io/images/placeholders/128x128.png"
                      onChange={this.handleChange}
                      value={this.state.data.image || ''}
                    />
                  </div>

                </div>

                <button className="button is-warning">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default BookEdit

// {this.state.errors.image && <div className="help is-danger">{this.state.errors.image}</div>}
// {this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}
