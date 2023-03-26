import os
import csv
import json
import xml.etree.ElementTree as ET
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

routes = APIRouter()

routes.get("/")

def _():
    return {"message": "First FastAPI route"}


# From JSON to CSV
@routes.get("/csv", status_code=200)
async def read_csv(response: Response):
    # Read JSON file
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../files/me.json"))
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = []
        for row in csvreader:
            data.append(row)
    return JSONResponse(content=data, status_code=200)


# From CSV to JSON
@routes.get('/json', status_code=200)
async def read_csv():
    # Read CSV
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../files/me.csv"))
    with open(file_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        rows = [row for row in csvreader]
    return rows

# From XML to JSON
@routes.get('/xml', status_code=200)
async def read_xml():
    # Read XML
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../files/me.xml"))
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Parse XML to dictionary
    data = {}
    hobbies = []
    for child in root:
        if child.tag == 'hobbies':
            for hobby in child:
                hobbies.append(hobby.text)
        else:
            data[child.tag] = child.text
    data['hobbies'] = hobbies

    return data
        
        
    