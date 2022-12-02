import './App.css';
import React from "react";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      list: null,
      searchTerm: ''
    };
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? 
                  target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  onDismiss(id) {
    const updateList = this.state.list.filter(item => item.id !== id);
    this.setState({list: updateList});
  }

  onSearchChange(event) {
    this.setState({searchTerm: event.target.value});
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/api/v1/exercicios/')
      .then((response) => response.json())
      .then((result) => this.setState({list: result}))
      .catch((error) => error);
  }

  render() {
    const {list, searchTerm} = this.state;

    return (
      <div className="App">
        <Search searchTerm={searchTerm} 
                handleInputChange={(e) => this.handleInputChange(e)}
        >
          Pesquisa:
        </Search>
        {
          list ? (
            <ExerciciosTable  list={list}
                              searchTerm={searchTerm}
                              onDismiss={(id) => this.onDismiss(id)}
            />
          ) : null
        }
      </div>
    );
  }
}

function ExerciciosTable(props) {
  const {list, onDismiss, searchTerm} = props;
  return (
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Exercício</th>
          <th>URL da foto</th>
          <th>Máquina</th>
        </tr>
      </thead>
      <tbody>
        {
          list.filter(ex => ex.nome.toLowerCase().includes(searchTerm)).map((ex) => (
            <tr key={ex.id}>
              <td>{ex.id}</td>
              <td>{ex.nome}</td>
              <td>{ex.urlfoto}</td>
              <td>{ex.maquina}</td>
              <td>
                <Button onClick = {() => onDismiss(ex.id)}>
                  Remover
                </Button>
              </td>
            </tr>
          ))
        }
      </tbody>
    </table>
  );
}

function Search(props) {
  const {searchTerm, handleInputChange, children} = props;
  return (
    <form>
      {children} <input type="text" placeholder="Busca nome do exercício"
      name="searchTerm" value={searchTerm}
      onChange={(event) => handleInputChange(event)}/>
    </form>
  );
}

function Button(props) {
  const {
    onClick,
    className='',
    children,
  } = props;
  return (
    <button onClick={onClick}
            className={className}
            type="button"
    >
      {children}
    </button>
  );
}

export default App;
