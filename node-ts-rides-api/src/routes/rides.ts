import { Router } from "express";
import { pgPool } from "../db/postgres";
import { redis } from "../db/redis";
import { requireAuth } from "../middleware/auth";

export const ridesRouter = Router();

ridesRouter.get("/", requireAuth, async (req, res) => {
  const userId = req.user!.sub;
  const cacheKey = `rides:user:${userId}`;
  const cached = await redis.get(cacheKey);
  if (cached) {
    return res.json(JSON.parse(cached));
  }

  const result = await pgPool.query(
    "SELECT id, origin, destination, status, created_at FROM rides WHERE user_id = $1 ORDER BY created_at DESC",
    [userId]
  );

  await redis.set(cacheKey, JSON.stringify(result.rows), "EX", 30);
  return res.json(result.rows);
});

ridesRouter.post("/", requireAuth, async (req, res) => {
  const userId = req.user!.sub;
  const { origin, destination } = req.body as {
    origin?: string;
    destination?: string;
  };

  if (!origin || !destination) {
    return res.status(400).json({ error: "origin and destination are required" });
  }

  const result = await pgPool.query(
    "INSERT INTO rides (user_id, origin, destination, status) VALUES ($1, $2, $3, 'requested') RETURNING id, user_id, origin, destination, status, created_at",
    [userId, origin, destination]
  );

  await redis.del(`rides:user:${userId}`);
  return res.status(201).json(result.rows[0]);
});
