# MetaMind

MetaMind é um projeto open source focado em **desenvolvimento pessoal e finanças**, com a proposta de ser extremamente simples: inserir dados rápido, acompanhar progresso e visualizar resumos claros.

---

## 🎯 Objetivo

Ajudar pessoas a organizarem:

* Metas pessoais
* Hábitos
* Progresso diário
* Ganhos e gastos

Tudo em um só lugar, de forma simples e gratuita.

---

## 🧱 Stack

### Frontend

* React + Vite

### Backend

* Python + FastAPI

### Banco de Dados

* PostgreSQL

### Infra

* Docker + Docker Compose
* CI/CD com GitHub Actions

### Deploy (Free Tier)

* Front: Vercel
* Back: Render
* Banco: Neon ou Supabase

---

## 📦 Estrutura do Projeto

```
metamind/
 ├── backend/
 │    ├── app/
 │    │    ├── main.py
 │    │    ├── routes/
 │    │    ├── services/
 │    │    ├── models/
 │    │    └── db.py
 │    ├── requirements.txt
 │    └── Dockerfile
 ├── frontend/
 │    ├── src/
 │    ├── index.html
 │    ├── vite.config.js
 │    └── Dockerfile
 ├── docker-compose.yml
 └── .github/workflows/ci.yml
```

---

## 🚀 Funcionalidades (MVP)

### Usuário

* Cadastro
* Login

### Desenvolvimento Pessoal

* Criar metas
* Criar hábitos
* Marcar progresso diário

### Finanças

* Registrar ganhos
* Registrar gastos
* Categorias simples
* Resumo mensal

---

## 🛠️ Como rodar localmente

### Pré-requisitos

* Git
* Docker
* Docker Compose
* Node.js
* Python 3.11+

### Passos

```bash
git clone https://github.com/seu-usuario/metamind.git
cd metamind
docker-compose up --build
```

* Front: [http://localhost:5173](http://localhost:5173)
* Back: [http://localhost:8000](http://localhost:8000)
* Docs API: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🤝 Contribuindo

1. Faça um fork
2. Crie uma branch: `feature/minha-feature`
3. Commit suas mudanças
4. Abra um Pull Request

---

## 📄 Licença

MIT License. Projeto livre para uso, estudo e modificação.

---

## 🌱 Visão de Futuro

* Relatórios visuais
* Gráficos de evolução
* Exportação de dados
* Modo offline (PWA)
* Templates de metas e hábitos
