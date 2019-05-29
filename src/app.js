import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

class App extends React.Component {

  componentDidMount() {
    axios.get('/books')
      .then(res => this.setState({ books: res.data }))
  }

  render() {
    if(!this.state) return <p>Loading...</p>
    return (
      <div>
        <div>
          <h1>APOCRYPHA</h1>
        </div>)
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
