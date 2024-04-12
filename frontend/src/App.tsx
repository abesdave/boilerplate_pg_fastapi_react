import './App.scss'
import { decrement, increment } from './store/counterSlice';

import { useAppSelector, useAppDispatch } from './store/hooks';

function App() {

  const dispatch = useAppDispatch()
  const counter = useAppSelector(state => state.counter).value

  return (
    <>
      <h1>Redux Counter</h1>
      <div>
        Counter: {counter}
        <button onClick={() => dispatch(increment())} className='btn btn-success'>Increment</button>
        <button onClick={() => dispatch(decrement())} className='btn btn-warning'>Decrement</button>
      </div>
    </>
  )
}

export default App
