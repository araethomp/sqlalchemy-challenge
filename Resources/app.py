import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#Engine

engine = create_engine("sqlite:///hawaii.sqlite",
                       connect_args={'check_same_thread': False})

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#session.close()

#Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"<h1>Welcome to the SQLAlchemy Challenge API</h1>"
        f"<h3>Available Routes:</h3>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    new_precipitation = {date: prcp for date, prcp in precipitation}

    return jsonify(new_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def tobs():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    primary_station = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    results = list(np.ravel(primary_station))
    return jsonify(results=results)


if __name__ == "__main__":
    app.run(debug=True)
