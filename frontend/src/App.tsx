import './App.scss'
import { useState } from 'react'
import TabButton from "../components/TabButton/TabButton"
import Right from '../components/Right/Right'

function App() {

  let [dynamicState, setDynamicState] = useState<string>("Set dynamic state")

  const onSelected = (value: string) => {
    alert(value)
    setDynamicState(value)
  }

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
          <menu>
            <TabButton onSelected={() => onSelected('element one')}>
              <p>Nested Component</p>
            </TabButton>
            <TabButton onSelected={() => onSelected('element two')}>
              <p>Nested Component</p>
            </TabButton>
          </menu>
        </div>
      </section>
      <section className="row bg-primary">
        dynamic content: {dynamicState}
      </section>
    </>
  )
}

export default App
