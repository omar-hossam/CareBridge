import express from "express";
import { getNavbar } from "../controllers/auth.controller.js";

const router = express.Router();


router.get("/navbar", getNavbar);

router.get("/login-test", (req, res) => {
  req.session.user = { name: "Yamin" };
  res.send("Logged in ");
});

router.get("/logout-test", (req, res) => {
  req.session.destroy();
  res.send("Logged out ");
});

export default router;