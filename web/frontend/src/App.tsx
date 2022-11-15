import React from "react"
import ResultPage from "./components/ResultPage/ResultPage"
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
import "./App.css"
import AllFilePage from "./components/AllFilePage/AllFilePage"

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/allfile/" element={<AllFilePage />} />
          <Route path="/result/" element={<ResultPage />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
