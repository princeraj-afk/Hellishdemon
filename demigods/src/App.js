import React from "react";


function App() {
  const helloInSpanish = () => {
    console.log("musto gucho")
  };

  return (<div>
    <h1>Hello!</h1>
    <button onClick={helloInSpanish}>Hola!</button>
  </div>)
}

export default App;