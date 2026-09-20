import { BrowserRouter, Routes, Route } from 'react-router-dom'
import UploadPage from '@/pages/UploadPage'
import NotFoundPage from '@/pages/NotFoundPage'
import RegisterPage from '@/pages/RegisterPage'
import LoginPage from '@/pages/LoginPage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<RegisterPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
