import React from 'react'
import { Link } from 'react-router-dom'

const ProjectItem = ({project, deleteProject}) => {
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
            <td>
              <button onClick={()=>deleteProject(project.id)}
              type="button">Удалить</button>
           </td>
       </tr>
   )
}

const ProjectList = ({projects, deleteProject}) => {
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
          <th>
          </th>
          {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
       </table>
   )
}


export default ProjectList
