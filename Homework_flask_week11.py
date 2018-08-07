from flask import Flask, jsonify, render_template
import json
import requests
from flask import request
from Weather_db import Session, Measurement, Station, engine
import numpy as np



app = Flask(__name__)

@app.route('/api/v1.0/precipitation')
def home_route():
    return "Flask Homework Week 11"

@app.route('/api/v1.0/precipitation')
def precipv1():
    weather_rows = engine.execute(""" 
            SELECT m.date, round(avg(m.tobs),2) as temperature
            FROM measurement m
            WHERE strftime('%Y', m.date)= '2017' 
            GROUP BY 1
    """).fetchall()

    vals = {k:v for k,v in weather_rows}
    return jsonify(vals)


app.run(debug=True)
