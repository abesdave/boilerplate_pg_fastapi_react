import { createBrowserRouter, Navigate, RouterProvider } from 'react-router-dom';
import './App.scss'
import DataContainer from './features/data/Data.container';

const router = createBrowserRouter([
  {
    path: '/data',
    element: <DataContainer />
  },
  {
    path: '*',
    element: <Navigate to='/data' />
  },
]);

function App() {

  return (
    <>
      <RouterProvider router={router} />   
    </>
  )
}

export default App
