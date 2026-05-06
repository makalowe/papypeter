import express from "express";
import { authRouter } from "./routes/auth";
import { ridesRouter } from "./routes/rides";

export const app = express();

app.use(express.json());

app.get("/health", (_req, res) => {
  res.json({ ok: true });
});

app.use("/auth", authRouter);
app.use("/rides", ridesRouter);
