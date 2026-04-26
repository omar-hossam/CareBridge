import express from "express";
import cors from "cors";
import authRoutes from "./routes/auth.route.js";


import urgentHelpRoutes from "./modules/urgentHelp/urgentHelp.route.js";
import healthCheckRouter from "./routes/healthcheck.route.js";


const app = express();

app.use(express.json());
app.use(cors());

// routes
app.use("/api/urgent-help", urgentHelpRoutes);
app.use("/health", healthCheckRouter);
app.use("/auth", authRoutes);

export default app;