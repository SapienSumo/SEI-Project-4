import React from 'react'
import Auth from '../lib/Auth'
import axios from 'axios'

class BookEdit extends React.Component {

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
      .then(res => {
        res.data.author_id = res.data.author.id
        this.setState({ data: res.data })
      })

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

    const data = this.state.data
    delete data['user']
    delete data['id']
    delete data['author']

    axios.put(`/api/books/${this.props.match.params.id}`, this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/api/books'))
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
                  <label className="label has-text-white">Select An Author</label>
                  <div className="select ">
                    <select name="author_id" onChange={this.handleChange} value={this.state.data.author_id}>
                      <option value={0}>Please select an author...</option>
                      {this.state.author.map(author =>
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
                      value={this.state.data.image || ''}
                    />
                  </div>

                  <div className="field">
                    <label className="label has-text-white">Blurb</label>
                    <div className="control">
                      <textarea className="textarea"
                        name="blurb"
                        placeholder=""
                        onChange={this.handleChange}
                        value={this.state.data.blurb}
                      />
                    </div>
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
