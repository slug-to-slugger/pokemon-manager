import React, { Component } from 'react'

class App extends Component {
  state = {
    data: [],
    token: [],
  }

  // Code is invoked after the component is mounted/inserted into the DOM tree.
  componentDidMount() {
    // トレーナー登録
    // const url = 'http://localhost/trainers/';
    // const method = "POST";
    // const headers = {
    //   'Accept': 'application/json',
    //   'Content-Type': 'application/json'
    // };
    // const obj = {"username": "test2@example.com", "password": "test", "nickname": "Jiro"};
    // const body = JSON.stringify(obj);
    // fetch(url,{method, headers, body})
    // .then((result) => {
    //   return result.json()
    // }).then((result) => {      
    //   console.log(result);
    // })
    // .catch((error) => {
    //   console.error('Error:', error);
    // });

    // 全トレーナーデータ取得
    // fetch(url)
    // .then((result) => {
    //   return result.json()
    // }).then((result) => {
    //   console.log(result);
    //     this.setState({
    //       data: result,
    //     })
    // })
    // .catch((error) => {
    //   console.error('Error:', error);
    // });

    // トークン情報取得
    // curl -H "Content-Type: application/json" http://localhost/api-token-auth/ -d '{"username": "test@example.com", "password": "test"}'
    const url = 'http://localhost/api-token-auth/';
    const method = "POST";
    const headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    };
    const obj = {"username": "test@example.com", "password": "test"};
    const body = JSON.stringify(obj);
    fetch(url,{method, headers, body})
    .then((result) => {
      return result.json()
    })
    .then((result) => {      
      console.log(result);
      this.setState({
        token: result,
      })
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }

  // render() {
  //   const { data } = this.state
    
  //   const result = data.map((d) => {
  //     return Object.keys(d).map((key) => {
  //       return <li key={key}>{d[key]}</li>
  //     })
  //   })

  //   return <ul>{result}</ul>
  // }

  // トークン取得
  render() {
    // console.log(this.state);
    const { token } = this.state
  return <div>{token.token}</div>

  }
}

export default App