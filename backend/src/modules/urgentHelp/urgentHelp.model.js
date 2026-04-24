import mongoose from "mongoose";

const urgentHelpSchema = new mongoose.Schema({
    name: String,
    phone: String,
    problem: String,
    location: String
}, { timestamps: true });

export default mongoose.model("UrgentHelp", urgentHelpSchema);