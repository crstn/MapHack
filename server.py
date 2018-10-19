from flask import Flask
from flask import request
import psycopg2
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/findmachine")
def findmachine():

    lat = request.args.get('lat')
    lng = request.args.get('lng')


    conn = psycopg2.connect("dbname='parking' \
                             host='localhost' \
                             user='postgres' \
                             password='postgres'")

    cur = conn.cursor()

    cur.execute("""SELECT ST_AsGeoJSON(geom)
    FROM parkomat
    WHERE ST_DWITHIN(
    	ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography, geom::geography, 1000)
    ORDER BY ST_DISTANCE(ST_SetSRID(
    	ST_MakePoint(%s, %s), 4326)::geography, geom::geography)
    LIMIT 1;""", (lng, lat, lng, lat ))


    closest_machine = json.dumps(cur.fetchone())
    closest_coords = closest_machine.split("[[")[1]

    coords = closest_coords.split("]]")[0]

    response = '{"type": "Feature","geometry": {"type": "Point","coordinates": ['+coords+']}}'




    cur.close()
    conn.close()


    return response





    #return "Find a machine at " + lat + ", " +lng
