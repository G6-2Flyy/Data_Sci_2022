import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Session start
session = Session(engine)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
   
    """List all available api routes."""
    return (
        f"Aloha! Welcome to the Hawaii WX API"
        f"/"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tabs"
        f"/api/v1.0/start"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation_analysis():
    
    query = """
        SELECT 
        date, 
        prcp  
        FROM 
        measurement
        WHERE
        date BETWEEN '2016-08-23' AND '2017-08-23'
        ORDER BY
        date desc;
        """
    results = session.execute(query).all()
    session.close()
    precip = {date: prcp for date, prcp in results}
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
  
    """Return a list of stations"""
    
    results = session.execute("SELECT station From station").all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/tobs")
def temp_observation():
    
    """Return a JSON list of temperature observations for the previous year"""
   
    results = session.execute("Select tobs, date From measurement Where date >= '2016-08-23'").all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/start")
def var_temps():
    start = '2016-08-24'
    """Return a list of min, max, and average temperatures for a specified start date"""

    results = session.execute(f"Select min(tobs), max(tobs), avg(tobs) From measurement Where date >= '{start}';").all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)




@app.route("/api/v1.0/start/end")
def rng_temps():
    start = '2016-08-23'
    end = '2017-08-23'
    """Return a list of min, max, and average temperatures for a range of dates"""
   
    results = session.execute(f"Select min(tobs), max(tobs), avg(tobs) From measurement Where date Between '{start}' and '{end}';").all()

    session.close()

    all_names = list(np.ravel(results))
    return jsonify(all_names)


if __name__ == '__main__':
    app.run(debug=True)

