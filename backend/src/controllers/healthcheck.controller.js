import ApiResponse from "../utils/ApiResponse.js";

export const checkHealth = async (req,res) => {
    res.status(200).json(new ApiResponse(200, null, "HealthCheck Successfull"));
}

