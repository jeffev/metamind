@echo off
echo Criando estrutura do projeto MetaMind...

mkdir backend
mkdir backend\app
mkdir backend\app\routes
mkdir backend\app\services
mkdir backend\app\models

type nul > backend\app\main.py
type nul > backend\app\db.py
type nul > backend\requirements.txt
type nul > backend\Dockerfile

mkdir frontend
mkdir frontend\src
type nul > frontend\index.html
type nul > frontend\vite.config.js
type nul > frontend\Dockerfile

mkdir .github
mkdir .github\workflows
type nul > .github\workflows\ci.yml

type nul > docker-compose.yml
type nul > README.md
type nul > .gitignore

echo Estrutura criada com sucesso!
pause
