import React from 'react'
import Auth from '../lib/Auth'
import axios from 'axios'

class BookNew extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {
        author_id: 0
      },
      authors: [],
      errors: null
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {

    axios('/api/authors')
      .then(res => this.setState({ authors: res.data }))

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
      .then(() => this.props.history.push('/api/books'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  render() {
    console.log(this.state.data)
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">
              <form onSubmit={this.handleSubmit}>
                <div className="field">
                  <label className="label has-text-white">Book Title</label>
                  <div className="control">
                    <input
                      className="input"
                      name="name"
                      placeholder=""
                      onChange={this.handleChange}
                    />
                  </div>

                  {this.state.errors && this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}

                </div>

                <div className="control">
                  <label className="label has-text-white">Select An Author</label>
                  <div className="select ">
                    <select name="author_id" onChange={this.handleChange}>
                      <option value={0}>Please select an author...</option>
                      {this.state.authors.map(author =>
                        <option value={author.id} key={author.id}>{author.name}</option>
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

                  {this.state.errors && this.state.errors.Image && <div className="help is-danger">{this.state.errors.Image}</div>}

                </div>

                <div className="field">
                  <label className="label has-text-white">Blurb</label>
                  <div className="control">
                    <textarea className="textarea"
                      name="blurb"
                      placeholder=""
                      onChange={this.handleChange}
                    />
                  </div>

                  {this.state.errors && this.state.errors.blurb && <div className="help is-danger">{this.state.errors.blurb}</div>}

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

export default BookNew
