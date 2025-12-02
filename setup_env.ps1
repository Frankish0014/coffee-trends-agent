
# PowerShell script to set up environment for Coffee Trends Agent
# Run this before starting the server or demos

$env:GOOGLE_API_KEY = "AIzaSyDyk8e7iGvc1nAa_kSXyGPzEieth8LRxLs"

Write-Host "✅ GOOGLE_API_KEY environment variable set!" -ForegroundColor Green
Write-Host "   You can now run:" -ForegroundColor Cyan
Write-Host "   - python run_server.py" -ForegroundColor Yellow
Write-Host "   - python run_demo.py" -ForegroundColor Yellow
Write-Host "   - python run_interactive.py" -ForegroundColor Yellow