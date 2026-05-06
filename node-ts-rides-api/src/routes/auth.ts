import { Router } from "express";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { pgPool } from "../db/postgres";
import { env } from "../config/env";

export const authRouter = Router();

authRouter.post("/register", async (req, res) => {
  const { email, password } = req.body as { email?: string; password?: string };
  if (!email || !password) {
    return res.status(400).json({ error: "email and password are required" });
  }

  const passwordHash = await bcrypt.hash(password, 10);

  try {
    const result = await pgPool.query(
      "INSERT INTO users (email, password_hash) VALUES ($1, $2) RETURNING id, email",
      [email, passwordHash]
    );
    return res.status(201).json(result.rows[0]);
  } catch (error) {
    return res.status(409).json({ error: "User already exists or DB error" });
  }
});

authRouter.post("/login", async (req, res) => {
  const { email, password } = req.body as { email?: string; password?: string };
  if (!email || !password) {
    return res.status(400).json({ error: "email and password are required" });
  }

  const result = await pgPool.query(
    "SELECT id, email, password_hash FROM users WHERE email = $1",
    [email]
  );
  const user = result.rows[0];
  if (!user) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  const ok = await bcrypt.compare(password, user.password_hash);
  if (!ok) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  const token = jwt.sign({ sub: String(user.id), email: user.email }, env.jwtSecret, {
    expiresIn: "7d",
  });

  return res.json({ token });
});
