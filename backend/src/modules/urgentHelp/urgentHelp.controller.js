import UrgentHelp from "./urgentHelp.model.js";

export const createRequest = async (req, res) => {
    try {
        const data = await UrgentHelp.create(req.body);
        res.status(201).json(data);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

export const getRequests = async (req, res) => {
    try {
        const data = await UrgentHelp.find();
        res.json(data);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

