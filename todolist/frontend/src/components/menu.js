import React from 'react'
import { Link } from 'react-router-dom'


{/*}
const Menu = () => {
   return (
       <nav> Строка меню</nav>
   )
}
*/}
const Menu = () => {

    return (
        <div>

                <ul>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Пользователи</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Проекты</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Заметки</Link>
                            </li>
                            <li>
                                <Link to='/login'>Вход</Link>
                            </li>
                        </ul>
                    </nav>
                </ul>

        </div>
    )
}

export default Menu
