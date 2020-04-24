import React, { Component } from 'react'

class App extends Component {
  state = {
    data: [],
  }

  // Code is invoked after the component is mounted/inserted into the DOM tree.
  componentDidMount() {
    const url =
      'http://pokemon_nginx/trainers/'

    fetch(url,{
      // method:"POST"
      })
      .then(result => result.json())
      .then((result) => {      
        console.log(result);
      })
      .then(result => {
        this.setState({
          data: result,
        })
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    // const result = fetch(url);
    // console.log("result of fetch");
    // console.log(result);
  }


  render() {
    const { data } = this.state
    
    console.log(data);
    console.log(this.state)

    const result = data.map((entry, index) => {
      return <li key={index}>{entry}</li>
    })

    return <ul>{result}</ul>
  }
}

export default App