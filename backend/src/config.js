import dotenv from "dotenv";

dotenv.config();

const env = {
    port: process.env.PORT || 5000,
    db_uri: process.env.DB_URI,
    db_name: process.env.DB_NAME
};

export default env;