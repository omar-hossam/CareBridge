import express from "express"
import cors from "cors"


const app = express();

app.use(express.json());
app.use(cors());

// import routes 
import healthCheckRouter from "./routes/healthcheck.route.js"

// use routes 
app.use("/health", healthCheckRouter);

export default app ; 