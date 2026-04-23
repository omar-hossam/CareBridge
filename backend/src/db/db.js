import mongoose from "mongoose";
import env from "../config.js";


const connectDB = async () => {
    try {
        console.log(env)
        const connectionInstance = await mongoose.connect(`${env.db_uri}${env.db_name}`)
        
        console.log(`\n MongoDB connected !! DB HOST: ${connectionInstance.connection.host}`);
    } catch (error) {
        console.log("MONGODB connection FAILED ", error);
        process.exit(1)
    }
}

export default connectDB;