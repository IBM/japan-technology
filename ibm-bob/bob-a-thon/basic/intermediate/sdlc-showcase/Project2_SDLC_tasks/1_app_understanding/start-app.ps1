# Windows 向けデュアルバンクアプリ起動スクリプト
# このスクリプトは、Bank2、Bank1 バックエンド、Bank1 フロントエンドを
# それぞれ別の PowerShell ウィンドウで起動します。

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  デュアルバンクアプリ起動スクリプト" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# スクリプトの配置ディレクトリを取得
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "アプリケーションサービスを起動しています..." -ForegroundColor Cyan
Write-Host ""

# Bank2 (Investment Bank) を新しい PowerShell ウィンドウで起動
Write-Host "Bank2 (Investment Bank) をポート 5000 で起動しています..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$scriptDir\bank2-investment'; Write-Host 'Bank2 - Investment Bank' -ForegroundColor Blue; Write-Host 'http://localhost:5000 で起動しています' -ForegroundColor Yellow; python app.py"
Start-Sleep -Seconds 3

# Bank1 Backend (Savings Bank) を新しい PowerShell ウィンドウで起動
Write-Host "Bank1 Backend (Savings Bank) をポート 5001 で起動しています..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$scriptDir\bank1-savings'; Write-Host 'Bank1 - Savings Bank Backend' -ForegroundColor Green; Write-Host 'http://localhost:5001 で起動しています' -ForegroundColor Yellow; python app.py"
Start-Sleep -Seconds 3

# Bank1 Frontend を新しい PowerShell ウィンドウで起動
Write-Host "Bank1 Frontend をポート 5173 で起動しています..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$scriptDir\bank1-savings\frontend'; Write-Host 'Bank1 - Frontend (React + Vite)' -ForegroundColor Magenta; Write-Host 'http://localhost:5173 で起動しています' -ForegroundColor Yellow; npm run dev"
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  アプリケーションの起動が完了しました" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "アクセス先:" -ForegroundColor Yellow
Write-Host "  • Frontend:        http://localhost:5173" -ForegroundColor White
Write-Host "  • Bank1 API:       http://localhost:5001" -ForegroundColor White
Write-Host "  • Bank2 API:       http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "ヘルスチェック:" -ForegroundColor Yellow
Write-Host "  • Bank1:           http://localhost:5001/health" -ForegroundColor White
Write-Host "  • Bank2:           http://localhost:5000/health" -ForegroundColor White
Write-Host ""
Write-Host "デモユーザー:" -ForegroundColor Yellow
Write-Host "  1. Alice Johnson (ID: 1)" -ForegroundColor White
Write-Host "  2. Bob Smith (ID: 2)" -ForegroundColor White
Write-Host "  3. Charlie Brown (ID: 3)" -ForegroundColor White
Write-Host "  4. David Wilson (ID: 4)" -ForegroundColor White
Write-Host "  5. Emma Brown (ID: 5)" -ForegroundColor White
Write-Host ""
Write-Host "各サービス用に 3 つの PowerShell ウィンドウを開きました。" -ForegroundColor Cyan
Write-Host "サービスを停止するには、それぞれのウィンドウを閉じるか、各ウィンドウで Ctrl+C を押してください。" -ForegroundColor Cyan
Write-Host ""
Write-Host "3 秒後にブラウザを開きます..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

# 既定のブラウザでフロントエンドを開く
Start-Process "http://localhost:5173"

Write-Host ""
Write-Host "何かキーを押すとこのウィンドウを閉じます..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Made with Bob
