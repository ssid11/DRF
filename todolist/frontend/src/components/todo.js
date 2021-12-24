import React from 'react'
import { Link } from 'react-router-dom';


const TodoItem = ({ todo, deleteToDo }) => {
    return (
        <tr>
            <td>
                {todo.active == true ? 'Да' : 'Нет'}
            </td>
            <td>
                {todo.author}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.on_created}
            </td>
            <td>
                <button type="button" onClick={() => deleteToDo(todo.id)}>Удалить</button>
            </td>
        </tr>
    )
}

const TodoList = ({ todos, deleteToDo }) => {
    return (
        <div>
        <p>Таблица заметок</p>
            <table>
                <th>
                    Активна?
                </th>
                <th>
                    Автор
                </th>
                <th>
                    Текст
                </th>
                <th>
                    Дата создания
                </th>
                <th>
                </th>
                {todos.map((todo) => <TodoItem todo={todo} deleteToDo={deleteToDo} />)}
            </table>
            <div ><Link to="/todos/create">Создать</Link></div>
        </div>
    )
}


export default TodoList
