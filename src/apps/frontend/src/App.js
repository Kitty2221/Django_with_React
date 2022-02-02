import React, { Component, Fragment } from "react";
import Home2 from "./users/Home2";
import Home3 from "./usersgroup/Home3";


import './App.css';


const BaseLayout = () => (
  <div className="container-fluid">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand" href="#">Django React Demo</a>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
  </button>
  <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div className="navbar-nav">
      <a className="nav-item nav-link" href="/">USERS</a>
      <a className="nav-item nav-link" href="/groups_user">GROUPS OF USER</a>

    </div>
  </div>
</nav>




  </div>
)

class App extends Component {
  render() {
    return (
      <Fragment>
            <BaseLayout/>
        <Home2 />
        <Home3 />
        {/*<Header2 />*/}
        {/*<Header3 />*/}
      </Fragment>
    );
  }
}

export default App;

