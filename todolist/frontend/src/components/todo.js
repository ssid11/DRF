import React from 'react'


const TodoItem = ({todo}) => {
   return (
       <tr>
           <td>
               {todo.active==true ? 'Да' : 'Нет'}
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
       </tr>
   )
}

const TodoList = ({todos}) => {
   return (
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
          {todos.map((todo) => <TodoItem todo={todo}/>)}
       </table>
   )
}


export default TodoList
