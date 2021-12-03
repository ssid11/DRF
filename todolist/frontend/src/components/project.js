import React from 'react'
import { Link } from 'react-router-dom'

const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
               {project.name}
           </td>
           <td>
               {project.repo}
           </td>
           <td>
               {project.devops}
           </td>
       </tr>
   )
}

const ProjectList = ({projects}) => {
   return (
       <table>

           <th>
              Название
           </th>
           <th>
               Репозиторий
           </th>
          <th>
            Разработчики
          </th>
          {projects.map((project) => <ProjectItem project={project}/>)}
       </table>
   )
}


export default ProjectList
