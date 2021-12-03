import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import UserList from './components/user.js'
import ProjectList from './components/project.js'
import TodoList from './components/todo.js'
import Menu from './components/menu.js'
import Footer from './components/footer.js'
import Page404 from './components/page404.js'
import {HashRouter, Route, BrowserRouter, Redirect, Switch } from 'react-router-dom'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': [],

       }
   }

   componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))
   axios.get('http://127.0.0.1:8000/api/projects')
       .then(response => {
           const projects = response.data
               console.log(projects)
               this.setState(
               {
                   'projects': projects
               }
           )
       }).catch(error => console.log(error))
   axios.get('http://127.0.0.1:8000/api/todos')
       .then(response => {
           const todos = response.data
               console.log(todos)
               this.setState(
               {
                   'todos': todos
               }
           )
       }).catch(error => console.log(error))
   }

   render () {
       return (
       <>
{/*            <div>
                <HashRouter>
                  <Route exact path='/' component = {() => <UserList users={this.state.users} />} />
                   <Route exact path='/projects' component = {() => <ProjectList projects={this.state.projects} />} />
                    <Route exact path='/todos' component = {() =><TodoList todos={this.state.todos} />} />
                </HashRouter>

           </div>*/}
                <BrowserRouter>
                <Menu />
                <Switch>
                    <Route exact path='/' component = {() => <UserList users={this.state.users} />} />
                    <Route exact path='/projects' component = {() => <ProjectList projects={this.state.projects} />} />
                    <Route exact path='/todos' component = {() =><TodoList todos={this.state.todos} />} />
                    <Redirect from='/users' to='/'/>
                    <Route component = {Page404}/>
                </Switch>
                </BrowserRouter>
            <Footer />
        </>
       )
   }
}

export default App;


