import { Link } from 'react-router-dom'
import { FileText, Upload, Sparkles } from 'lucide-react'
import { Button } from '@/components/ui/button'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 flex flex-col items-center justify-center p-4 text-neutral-100">
      <div className="text-center space-y-6 max-w-2xl">
        {/* Icon */}
        <div className="mx-auto w-20 h-20 bg-indigo-500/10 rounded-2xl flex items-center justify-center border border-indigo-500/20">
          <Sparkles className="w-10 h-10 text-indigo-400" />
        </div>

        {/* Heading */}
        <div className="space-y-3">
          <h1 className="text-5xl font-bold tracking-tight bg-gradient-to-r from-white to-neutral-400 bg-clip-text text-transparent">
            AI Resume Builder
          </h1>
          <p className="text-lg text-neutral-400 max-w-md mx-auto leading-relaxed">
            Upload your resume and let AI analyze, optimize, and enhance it for the job market.
          </p>
        </div>

        {/* Features */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-8 text-left">
          <div className="p-4 rounded-xl bg-neutral-900/50 border border-neutral-800">
            <Upload className="w-5 h-5 text-indigo-400 mb-2" />
            <h3 className="font-semibold text-white text-sm">Upload PDF / DOCX</h3>
            <p className="text-xs text-neutral-500 mt-1">Supports all major resume formats up to 5MB</p>
          </div>
          <div className="p-4 rounded-xl bg-neutral-900/50 border border-neutral-800">
            <FileText className="w-5 h-5 text-indigo-400 mb-2" />
            <h3 className="font-semibold text-white text-sm">AI-Powered Analysis</h3>
            <p className="text-xs text-neutral-500 mt-1">Get intelligent feedback and suggestions instantly</p>
          </div>
        </div>

        {/* CTA */}
        <div className="flex flex-col sm:flex-row gap-3 justify-center pt-4">
          <Link to="/upload">
            <Button className="bg-indigo-600 hover:bg-indigo-500 text-white border-0 h-11 px-8 text-base font-medium transition-all">
              Get Started
            </Button>
          </Link>
        </div>
      </div>
    </div>
  )
}
