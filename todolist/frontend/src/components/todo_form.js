import React from "react";

class ToDoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { project: '', author: '', text: "", }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.project, this.state.author, this.state.text)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form
                    onSubmit={(event) => this.handleSubmit(event)}>
                    <label>
                        Создать заметку
                    </label>
                    <div className="form-group">
                        <label for="text">Текст заметки</label>
                        <input type="text" name="text" value={this.state.text}
                            onChange={(event) => this.handleChange(event)} />
                    </div>
                    <div className="form-group">
                        <label for="author">Укажите автора</label>
                        <select name="author"
                            onChange={(event) => this.handleChange(event)}>
                            {this.props.authors.map((item) =>
                                <option value={item.id}>
                                    {item.username}
                                </option>)}
                        </select>
                    </div>
                    <div className="form-group">
                        <label for='project'> Проект</label>
                        <select className="form-control" name="project"
                            onChange={(event) => this.handleChange(event)}>
                            {this.props.projects.map((item) =>
                                <option value={item.id}>
                                    {item.name}
                                </option>)}
                        </select>
                    </div>
                    <div>
                        <input className="btn-success" type="submit" value="Сохранить" />
                    </div>
                </form>
            </div>
        )
    }
}
export default ToDoForm