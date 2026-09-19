import { Link } from 'react-router-dom'
import { AlertCircle } from 'lucide-react'
import { Button } from '@/components/ui/button'

export default function NotFoundPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 flex items-center justify-center p-4 text-neutral-100">
      <div className="text-center space-y-6">
        <div className="mx-auto w-16 h-16 bg-red-500/10 rounded-full flex items-center justify-center border border-red-500/20">
          <AlertCircle className="w-8 h-8 text-red-400" />
        </div>
        <div className="space-y-2">
          <h1 className="text-7xl font-bold text-white">404</h1>
          <p className="text-xl text-neutral-400">Page not found</p>
          <p className="text-sm text-neutral-500">The page you're looking for doesn't exist.</p>
        </div>
        <Link to="/">
          <Button className="bg-indigo-600 hover:bg-indigo-500 text-white border-0 h-10 px-6 font-medium transition-all">
            Go Home
          </Button>
        </Link>
      </div>
    </div>
  )
}
