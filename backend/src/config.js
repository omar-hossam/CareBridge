import {configDotenv} from "dotenv"
configDotenv({
    path: "./.env"
})


const env = {
    db_uri : process.env.DB_URI,
    db_name : process.env.DB_NAME,
    port : process.env.PORT,
}

export default env ; 

