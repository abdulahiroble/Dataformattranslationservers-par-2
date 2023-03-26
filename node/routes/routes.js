import { Router } from "express";
import fs from 'fs';
import yaml from 'js-yaml';
const router = Router();

router.get("/", (req, res) => {
    res.send("Node.js server is running");
});

// Get YAML file and return it as txt
router.get("/yaml", (req, res) => {
    // Read yaml file
    const file = fs.readFileSync('./files/me.yaml', 'utf8');
    const doc = yaml.load(file);
    res.send(doc);
});

// Read txt file and return it as csv
router.get("/csv", (req, res) => {
    // Read txt file
    const file = fs.readFileSync('./files/me.txt', 'utf8');
    const lines = file.split('  ');
    const csv = lines.join(' , ');
    res.send(csv);
});

// Read csv file and return it as xml
router.get("/xml", (req, res) => {
    // Read csv file
    const file = fs.readFileSync('./files/me.csv', 'utf8');
    const lines = file.split(' , ');
    const xml = lines.join(' <br> ');
    res.send(xml);
});

export { router };