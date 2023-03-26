import express from "express";
import { router } from "./routes/routes.js";
const app = express();

app.use(router);
app.use(express.json());

app.listen(8080, () => console.log("Server is running on port", 8080));
