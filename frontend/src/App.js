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
import ToDoForm from './components/todo_form';

import { HashRouter, Route, BrowserRouter, Redirect, Switch, Link } from 'react-router-dom';


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
        this.setState({ 'token': token, 'username': username }, () => this.load_data())
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
        this.setState({ 'token': token, 'username': username }, () => this.load_data())
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

    deleteProject(id) {
        const headers = this.get_headers()
        const url = 'http://127.0.0.1:8000/api/projects/' + id + '/'
        const ret = axios.delete(url, { headers }).then(() => { this.load_data() })

    }

    deleteToDo(id) {
        const headers = this.get_headers()
        const url = 'http://127.0.0.1:8000/api/todos/' + id + '/'
        const ret = axios.delete(url, { headers }).then(() => { this.load_data() })

    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users', { headers })
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => { this.setState({ 'users': [] }); console.log(error) })
        axios.get('http://127.0.0.1:8000/api/projects', { headers })
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => { this.setState({ 'projects': [] }); console.log(error) })
        axios.get('http://127.0.0.1:8000/api/todos', { headers })
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => { this.setState({ 'todos': [] }); console.log(error) })
    }

    componentDidMount() {
        this.load_data()

    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', { username: username, password: password })
            .then(response => {
                this.set_token(response.data['token'], username);
            }).catch(error => alert('???????????????? ?????????? ?????? ????????????'))
    }

    createToDo(project, user, text) {
        const headers = this.get_headers()
        const data = { project: project, author: user, text: text }
//        axios.post('http://127.0.0.1:8000/api/todos/', data, { headers })
//            .then(response => {
//                this.load_data()
//            }).catch(error => {
//                console.log(error)
//                this.setState({ todo: [] })
//            })
        const ret = axios.post('http://127.0.0.1:8000/api/todos/', data, { headers })
        this.load_data()
    }

    render() {
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
                    {/*<Menu >*/}
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>????????????????????????</Link>
                            </li>
                            <li>
                                <Link to='/projects'>??????????????</Link>
                            </li>
                            <li>
                                <Link to='/todos'>??????????????</Link>
                            </li>
                            <li>{this.is_auth() ?
                                <button onClick={() => this.logout()}> ?????????? </button> :
                                <Link to='/login/'>??????????</Link>}</li>
                            <p> ????????????????????????: {this.is_auth() ? this.state.username : '??????????????????????????'} </p>
                        </ul>
                    </nav>
                    {/*</Menu>*/}

                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}
                            deleteProject={(id) => this.deleteProject(id)} />} />
                        <Route exact path='/todos' component={() => <TodoList todos={this.state.todos}
                            deleteToDo={(id) => this.deleteToDo(id)} />} />
                        <Route exact path="/todos/create"
                           component={() => <ToDoForm authors={this.state.users} projects={this.state.projects}
                                                      createToDo={(project, user, text) => this.createToDo(project, user, text)}/>}/>
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Redirect from='/users' to='/' />
                        <Route component={Page404} />
                    </Switch>
                </BrowserRouter>
                <Footer />
            </>
        )
    }
}

export default App;


