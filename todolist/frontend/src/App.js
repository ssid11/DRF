import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Cookies from 'universal-cookie';

import UserList from './components/user.js';
import ProjectList from './components/project.js';
import TodoList from './components/todo.js';
import Menu from './components/menu.js';
import Footer from './components/footer.js';
import Page404 from './components/page404.js';
import LoginForm from './components/login_form.js';

import {HashRouter, Route, BrowserRouter, Redirect, Switch } from 'react-router-dom';


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': [],
           'token': '',
           'username': '',

       }
   }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('username', username)
        this.setState({'token': token}, () => this.load_data())
    }

    is_auth() {
        return !!this.state.token
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        this.setState({'token': token, 'username': username}, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
        }

   load_data() {
       const headers = this.get_headers()
       axios.get('http://127.0.0.1:8000/api/users', {headers})
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => {this.setState({'users':[]}); console.log(error)})
       axios.get('http://127.0.0.1:8000/api/projects', {headers})
           .then(response => {
               const projects = response.data
                   console.log(projects)
                   this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => {this.setState({'projects':[]}); console.log(error)})
       axios.get('http://127.0.0.1:8000/api/todos', {headers})
           .then(response => {
               const todos = response.data
                   console.log(todos)
                   this.setState(
                   {
                       'todos': todos
                   }
               )
           }).catch(error => {this.setState({'todos':[]}); console.log(error)})
   }

   load_data(){}

   componentDidMount() {
    load_data()

   }

   get_token(username, password) {
    console.log('call g_t')
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
        this.set_token(response.data['token'], username);
        console.log(response.data)
    }).catch(error => alert('Неверный логин или пароль'))
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
                    <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
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


