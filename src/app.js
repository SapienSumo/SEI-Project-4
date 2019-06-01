import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Route, Switch } from 'react-router-dom'
import axios from 'axios'


import Home from './components/Home'
import Register from './auth/Register'
import Login from './auth/Login'
import Navbar from './components/Navbar'
import BooksIndex from './components/BooksIndex'
import BookEdit from './components/BookEdit'
import BookNew from './components/BookNew'
import BooksShow from './components/BooksShow'
import Archive from './components/Archive'

import 'bulma'
import './style.scss'

class App extends React.Component {

  componentDidMount() {
    axios.get('/api/books')
      .then(res => this.setState({ books: res.data }))
  }

  render() {
    if(!this.state) return <p>Loading...</p>
    return (
      <Router>
        <main>
          <Navbar />
          <Switch>
            <Route path="/search/:query" component={BooksIndex} />
            <Route path="/books/:id/edit" component={BookEdit}/>
            <Route path="/books/new" component={BookNew} />
            <Route path="/books/:id" component={BooksShow}/>
            <Route path="/books" component={BooksIndex}/>
            <Route path="/archive" component={Archive}/>
            <Route path="/register" component={Register}/>
            <Route path="/login" component={Login}/>
            <Route path="/" component={Home}/>
          </Switch>
        </main>
      </Router>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
