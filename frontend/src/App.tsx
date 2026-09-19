import { useState } from 'react'
import { UploadCloud, FileText, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react'
import { Button } from './components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './components/ui/card'
import { Input } from './components/ui/input'
import { Label } from './components/ui/label'

function App() {
  const [file, setFile] = useState<File | null>(null)
  const [isUploading, setIsUploading] = useState(false)
  const [status, setStatus] = useState<'idle' | 'success' | 'error'>('idle')
  const [message, setMessage] = useState('')

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0])
      setStatus('idle')
      setMessage('')
    }
  }

  const handleUpload = async () => {
    if (!file) return

    setIsUploading(true)
    setStatus('idle')
    setMessage('')

    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch('http://localhost:8000/api/v1/resume/upload', {
        method: 'POST',
        body: formData,
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || 'Upload failed')
      }

      setStatus('success')
      setMessage('Resume uploaded successfully!')
      setFile(null)
      // Clear the input
      const fileInput = document.getElementById('resume-upload') as HTMLInputElement
      if (fileInput) fileInput.value = ''
    } catch (error: any) {
      setStatus('error')
      setMessage(error.message || 'Something went wrong during upload.')
    } finally {
      setIsUploading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 flex items-center justify-center p-4 text-neutral-100">
      <Card className="w-full max-w-md bg-neutral-900/50 border-neutral-800 backdrop-blur-xl shadow-2xl">
        <CardHeader className="text-center space-y-2">
          <div className="mx-auto w-12 h-12 bg-indigo-500/10 rounded-full flex items-center justify-center mb-2">
            <UploadCloud className="w-6 h-6 text-indigo-400" />
          </div>
          <CardTitle className="text-2xl font-bold tracking-tight text-white">Upload Resume</CardTitle>
          <CardDescription className="text-neutral-400">
            Select a PDF or DOCX file to upload your resume (Max 5MB).
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="space-y-2">
            <Label htmlFor="resume-upload" className="sr-only">Resume File</Label>
            <div className="relative group">
              <Input
                id="resume-upload"
                type="file"
                accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                onChange={handleFileChange}
                disabled={isUploading}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
              />
              <div className="border-2 border-dashed border-neutral-700 rounded-xl p-8 flex flex-col items-center justify-center space-y-3 bg-neutral-950/50 group-hover:border-indigo-500/50 group-hover:bg-indigo-500/5 transition-all">
                {file ? (
                  <>
                    <FileText className="w-8 h-8 text-indigo-400" />
                    <span className="text-sm font-medium text-neutral-200 truncate max-w-full px-4">{file.name}</span>
                    <span className="text-xs text-neutral-500">{(file.size / 1024 / 1024).toFixed(2)} MB</span>
                  </>
                ) : (
                  <>
                    <UploadCloud className="w-8 h-8 text-neutral-500 group-hover:text-indigo-400 transition-colors" />
                    <span className="text-sm font-medium text-neutral-300">Click to browse or drag and drop</span>
                    <span className="text-xs text-neutral-500">PDF, DOCX up to 5MB</span>
                  </>
                )}
              </div>
            </div>
          </div>

          {status !== 'idle' && (
            <div className={`p-4 rounded-lg flex items-start space-x-3 text-sm ${status === 'success' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-red-500/10 text-red-400 border border-red-500/20'}`}>
              {status === 'success' ? <CheckCircle2 className="w-5 h-5 shrink-0" /> : <AlertCircle className="w-5 h-5 shrink-0" />}
              <p className="leading-tight pt-0.5">{message}</p>
            </div>
          )}

          <Button 
            onClick={handleUpload} 
            disabled={!file || isUploading}
            className="w-full bg-indigo-600 hover:bg-indigo-500 text-white border-0 h-11 text-base font-medium transition-all"
          >
            {isUploading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Uploading...
              </>
            ) : (
              'Upload Resume'
            )}
          </Button>
        </CardContent>
      </Card>
    </div>
  )
}

export default App
