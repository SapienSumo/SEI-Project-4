import React from 'react'
import { Link } from 'react-router-dom'
import Auth from '../lib/Auth'
import images from '../images'

class Home extends React.Component {
  constructor(){
    super()

    this.state = {
      currentImg: 0,
      images: images
    }
  }

  componentDidMount() {
    setInterval(() => {
      let currentImg = this.state.currentImg + 1
      currentImg === this.state.images.length ? currentImg = 0:null
      this.setState({ currentImg })
    }, 4000)
  }

  render() {
    return (
      <section className="section home-container" id="background-change" style={{
        backgroundImage: `url(${images[this.state.currentImg]})`
      }}>
        <div className="container title-container has-text-centered">
          <h1 className="title logohome has-text-light is-1"> APOCHRYPHA </h1>
          <h2 className="subtitle is-2"> FIND YOUR VICE </h2>
          {!Auth.isAuthenticated() && <Link to="/register"><button className="button is-warning">Sign Up</button></Link> || <Link to="/aboutus"><button className="button is-warning">ARCHIVES</button></Link>}
        </div>
      </section>
    )
  }
}

export default Home
