##This is your app.py!!!
#*********************
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
        f"/api/v1.0/temp/yyyy-mm-dd/yyyy-mm-dd"
    )


if __name__ == "__main__":
    app.run(debug=True)
