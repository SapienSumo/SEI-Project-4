import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../lib/Auth'

class Navbar extends React.Component {

  constructor(props) {
    super(props)

    this.state = { active: false }

    this.logout = this.logout.bind(this)
    this.toggleActive = this.toggleActive.bind(this)
  }

  logout() {
    Auth.removeToken()
    this.props.history.push('/books')
  }

  toggleActive() {
    this.setState({ active: !this.state.active })
  }

  componentDidUpdate(prevProps) {
    if(prevProps.location.pathname !== this.props.location.pathname) {
      this.setState({ active: false })
    }
  }
  //   this.state = {
  //     data: {}
  //   }
  //   this.handleSearch = this.handleSearch.bind(this)
  //   this.handleSubmit = this.handleSubmit.bind(this)
  // }
  //
  // handleSearch(e) {
  //   this.setState({ data: e.target.value })
  // }
  //
  // handleSubmit(e) {
  //   e.preventDefault()
  //
  //   this.props.history.push(`/search/${this.state.data}`)
  //  }

  render() {
    return (
      <nav className="navbar is-dark">
        <div className="container">
          <div className="navbar-brand">

            <Link to="/" className="navbar-item navbar-home">APOCHRYPHA</Link>
            <div className="field has-addons">
              <div className="control">
                <input className="input" type="text" placeholder="Find a repository"></input>
              </div>
              <div className="control">
                <a className="button is-warning">
                  Search
                </a>
              </div>
            </div>
            <a role="button" className={`navbar-burger ${this.state.active ? 'is-active' : ''}`}
              onClick={this.toggleActive}>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>

          <div className={`navbar-menu ${this.state.active ? 'is-active' : ''}`}>

            {/* Everything else*/}

            <div className="navbar-end">

              <Link to="/archive" className="navbar-item">Archives</Link>

              {/* Right-hand links*/}
              {/* Method for Navbar components */}

              <Link to="/books" className="navbar-item">Books</Link>

              {!Auth.isAuthenticated() && <Link to="/login" className="navbar-item">Login</Link>}

              {/* Register and login will now disappear once logged in */}
              {Auth.isAuthenticated() && <a className="navbar-item" onClick={this.logout}>Logout</a>}

            </div>
          </div>
        </div>
      </nav>
    )
  }
}
// `withRouter` gives the Navbar `history` via props
export default withRouter(Navbar)
