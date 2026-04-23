import app from "./app.js";
import connectDB from "./db/db.js";
import env from "./config.js";

connectDB()
.then(() => {
    app.listen(env.port , () => {
        console.log(`⚙️ Server is running at port : ${env.port}`);
    })
})
.catch((err) => {
    console.log("MONGO db connection failed !!! ", err);
})