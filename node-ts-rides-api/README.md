# Node + TypeScript Rides API

## Stack
- Node.js + TypeScript
- Express + JWT
- PostgreSQL (pg)
- Redis (ioredis)

## Setup
1. Copy `.env.example` to `.env`
2. Install deps:
   - `npm install`
3. Init DB schema:
   - run `sql/init.sql` on your PostgreSQL database
4. Start dev server:
   - `npm run dev`

## First routes
- `POST /auth/register` body: `{ "email": "...", "password": "..." }`
- `POST /auth/login` body: `{ "email": "...", "password": "..." }`
- `GET /rides` header: `Authorization: Bearer <token>`
- `POST /rides` header: `Authorization: Bearer <token>` body: `{ "origin": "...", "destination": "..." }`

