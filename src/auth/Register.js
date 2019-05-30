import React from 'react'
import axios from 'axios'
// import { ToastContainer, toast } from 'react-toastify'

class Register extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {},
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    //this.ageValidator = this.ageValidator.bind(this)
  }

  //function for converting the date of birth to an age in years

  handleChange(e) {
    console.log(e.target.value)
    const data =  {...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data: data })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login'))
      .catch((err) => this.setState({errors: err.response.data.errors }))
  }

  render() {
    console.log(this.state)
    return (
      <section>
        <section className="section">
          <div className="container">
            <div className="columns is-centered">
              <div className="column is-half-desktop is-two-thirds-tablet">
                <form onSubmit={this.handleSubmit}>

                  <div className="field">
                    <label className="label">Username</label>
                    <div className="control">
                      <input className="input"
                        name="username"
                        placeholder="eg: leela3000"
                        onChange={this.handleChange} />
                    </div>
                    {this.state.errors.username && <div className="help is-danger">{this.state.errors.username}</div>}
                  </div>

                  <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                      <input className="input"
                        name="email"
                        placeholder="eg: leela@planetexpress.nnyc" onChange={this.handleChange} />
                    </div>
                    {this.state.errors.email && <div className="help is-danger">{this.state.errors.email}</div>}
                  </div>

                  <div className="field">
                    <label className="label">Password</label>
                    <div className="control">
                      <input className="input"
                        name="password"
                        type="password"
                        placeholder="eg: ••••••••"
                        onChange={this.handleChange} />
                    </div>
                    {this.state.errors.password && <div className="help is-danger">{this.state.errors.password}</div>}
                  </div>

                  <div className="field">
                    <label className="label">Password Confirmation</label>
                    <div className="control">
                      <input className="input"
                        name="password_confirmation"
                        type="password"
                        placeholder="eg: ••••••••"
                        onChange={this.handleChange} />
                    </div>
                    {this.state.errors.password_confirmation && <div className="help is-danger">{this.state.errors.password_confirmation}</div>}
                  </div>
                  <button className="button is-info submit-edit-button">Submit</button>
                </form>
              </div>
            </div>
          </div>
        </section>
      </section>
    )
  }
}


export default Register
