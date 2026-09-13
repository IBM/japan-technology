@echo off
REM Windows 向けデュアルバンクアプリ起動スクリプト (CMD)
REM このスクリプトは、Bank2、Bank1 バックエンド、Bank1 フロントエンドを
REM それぞれ別ウィンドウで起動します

echo ========================================
echo   デュアルバンクアプリ起動スクリプト
echo ========================================
echo.

REM スクリプトの配置ディレクトリを取得
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo アプリケーションサービスを起動しています...
echo.

REM Bank2 (Investment Bank) を新しいウィンドウで起動
echo Bank2 (Investment Bank) をポート 5000 で起動しています...
start "Bank2 - Investment Bank" cmd /k "cd /d "%SCRIPT_DIR%bank2-investment" && echo Bank2 - Investment Bank && echo http://localhost:5000 で起動しています && python app.py"
timeout /t 3 /nobreak >nul

REM Bank1 Backend (Savings Bank) を新しいウィンドウで起動
echo Bank1 Backend (Savings Bank) をポート 5001 で起動しています...
start "Bank1 - Savings Bank Backend" cmd /k "cd /d "%SCRIPT_DIR%bank1-savings" && echo Bank1 - Savings Bank Backend && echo http://localhost:5001 で起動しています && python app.py"
timeout /t 3 /nobreak >nul

REM Bank1 Frontend を新しいウィンドウで起動
echo Bank1 Frontend をポート 5173 で起動しています...
start "Bank1 - Frontend" cmd /k "cd /d "%SCRIPT_DIR%bank1-savings\frontend" && echo Bank1 - Frontend (React + Vite) && echo http://localhost:5173 で起動しています && npm run dev"
timeout /t 5 /nobreak >nul

echo.
echo ========================================
echo   アプリケーションの起動が完了しました
echo ========================================
echo.
echo アクセス先:
echo   - Frontend:        http://localhost:5173
echo   - Bank1 API:       http://localhost:5001
echo   - Bank2 API:       http://localhost:5000
echo.
echo ヘルスチェック:
echo   - Bank1:           http://localhost:5001/health
echo   - Bank2:           http://localhost:5000/health
echo.
echo デモユーザー:
echo   1. Alice Johnson (ID: 1)
echo   2. Bob Smith (ID: 2)
echo   3. Charlie Brown (ID: 3)
echo   4. David Wilson (ID: 4)
echo   5. Emma Brown (ID: 5)
echo.
echo 各サービス用に 3 つのコマンドウィンドウを開きました。
echo サービスを停止するには、それぞれのウィンドウを閉じてください。
echo.
echo 3 秒後にブラウザを開きます...
timeout /t 3 /nobreak >nul

REM 既定のブラウザでフロントエンドを開く
start http://localhost:5173

echo.
echo 何かキーを押すとこのウィンドウを閉じます...
pause >nul

@REM Made with Bob
