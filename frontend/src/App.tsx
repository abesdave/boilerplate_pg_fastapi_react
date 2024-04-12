import './App.scss'

import Right from '../components/Right/Right'

function App() {
  return (
    <>
      <section>
        <div className="row bg-success">
          <Right val="World." />
        </div>
      </section>
      <section>
        <div className="row bg-warning">
          <h2>Examples:</h2>
        </div>
      </section>
    </>
  )
}

export default App
