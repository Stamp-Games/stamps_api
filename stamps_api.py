#!/usr/bin/env python3

"""
Description: This API is part of the Thinkful Stamps project.
The API is to allow for GET requests that will fetch populated data and save that data in a JSON object.

POST, UPDATE & DELETE requests will come as the data categories are flushed out.
authored by Michael Nickey on February 26th 2016
"""
# Todo(mnickey) : create POST request endpoint
# Todo(mnickey) : create UPDATE endpoint
# Todo(mnickey) : create DELETE endpoint
import json
import logging
from flask import Flask, jsonify, abort, make_response, request, render_template
from database import Stamp
from flask.ext.sqlalchemy import SQLAlchemy
import pprint
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object('database')
db = SQLAlchemy(app)
pp = pprint.PrettyPrinter(indent=4)

# Logging Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
WEB PAGES
"""

@app.route('/', methods=['GET'])
@app.route('/stamps/index/', methods=['GET'])
def show_index():
    return render_template('main.html')


"""
DATABASE FUNCTIONS
"""


# Get all the stamps from the database
def query_db():
    logger.info("Logging stamps...")
    stamp_query = Stamp.query.all()
    results = [stamp.to_dict() for stamp in stamp_query]
    return json.dumps(results)


# Write all the stamps from the database into a JSON file
def query_db_to_json():
    f = open('stamps.json', 'w')
    json.dump(query_db(), f, indent=2)
    f.close()
    return f


def load_stamps():
    al_stamp = Stamp(state="Alabama", state_abbr="AL", stamp_url="/images/alabama-stamp.jpg",
                     stamp_name="alabama-stamp", blurb="This is the Alabama state stamp.",
                     date_issued="", country="United States", value="0.35")
    db.session.add(al_stamp)
    ak_stamp = Stamp(state="Alaska", state_abbr="AK", stamp_url="/images/alaska-stamp.jpg",
                     stamp_name="alaska-stamp", blurb="This is the Alaska state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ak_stamp)
    az_stamp = Stamp(state="Arizona", state_abbr="AZ", stamp_url="/images/arizona-stamp.jpg",
                     stamp_name="arizona-stamp", blurb="This is the Arizona state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(az_stamp)
    ar_stamp = Stamp(state="Arkansas", state_abbr="AR", stamp_url="/images/arkansas-stamp.jpg",
                     stamp_name="arkansas-stamp", blurb="This is the Arkansas state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ar_stamp)
    ca_stamp = Stamp(state="California", state_abbr="CA", stamp_url="/images/california-stamp.jpg",
                     stamp_name="california-stamp", blurb="This is the California state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ca_stamp)
    co_stamp = Stamp(state="Colorado", state_abbr="CO", stamp_url="/images/colorado-stamp.jpg",
                     stamp_name="colorado-stamp", blurb="This is the Colorado state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(co_stamp)
    ct_stamp = Stamp(state="Connecticut", state_abbr="CT", stamp_url="/images/connecticut-stamp.jpg",
                     stamp_name="connecticut-stamp", blurb="This is the Connecticut state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ct_stamp)
    de_stamp = Stamp(state="Delaware", state_abbr="DE", stamp_url="/images/delaware-stamp.jpg",
                     stamp_name="delaware-stamp", blurb="This is the Delaware state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(de_stamp)
    fl_stamp = Stamp(state="Florida", state_abbr="FL", stamp_url="/images/Florida-stamp.jpg".lower(),
                     stamp_name="Florida-stamp".lower(), blurb="This is the Florida state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(fl_stamp)
    ga_stamp = Stamp(state="Georgia", state_abbr="GA", stamp_url="/images/Georgia-stamp.jpg".lower(),
                     stamp_name="Georgia-stamp".lower(), blurb="This is the Georgia state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ga_stamp)
    hi_stamp = Stamp(state="Hawaii", state_abbr="HI", stamp_url="/images/Hawaii-stamp.jpg".lower(),
                     stamp_name="Hawaii-stamp".lower(), blurb="This is the Hawaii state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(hi_stamp)
    id_stamp = Stamp(state="Idaho", state_abbr="ID", stamp_url="/images/Idaho-stamp.jpg".lower(),
                     stamp_name="Idaho-stamp".lower(), blurb="This is the Idaho state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(id_stamp)
    il_stamp = Stamp(state="Illinois", state_abbr="IL", stamp_url="/images/Illinois-stamp.jpg".lower(),
                     stamp_name="Illinois-stamp".lower(), blurb="This is the Illinois state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(il_stamp)
    in_stamp = Stamp(state="Indiana", state_abbr="IN", stamp_url="/images/Indiana-stamp.jpg".lower(),
                     stamp_name="Indiana-stamp".lower(), blurb="This is the Indiana state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(in_stamp)
    ia_stamp = Stamp(state="Iowa", state_abbr="IA", stamp_url="/images/Iowa-stamp.jpg".lower(),
                     stamp_name="Iowa-stamp".lower(), blurb="This is the Iowa state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ia_stamp)
    ks_stamp = Stamp(state="Kansas", state_abbr="KS", stamp_url="/images/Kansas-stamp.jpg".lower(),
                     stamp_name="Kansas-stamp".lower(), blurb="This is the Kansas state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ks_stamp)
    ky_stamp = Stamp(state="Kentucky", state_abbr="KY", stamp_url="/images/Kentucky-stamp.jpg".lower(),
                     stamp_name="Kentucky-stamp".lower(), blurb="This is the Kentucky state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ky_stamp)
    la_stamp = Stamp(state="Louisiana", state_abbr="LA", stamp_url="/images/Louisiana-stamp.jpg".lower(),
                     stamp_name="Louisiana-stamp".lower(), blurb="This is the Louisiana state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(la_stamp)
    me_stamp = Stamp(state="Maine", state_abbr="ME", stamp_url="/images/Maine-stamp.jpg".lower(),
                     stamp_name="Maine-stamp".lower(), blurb="This is the Maine state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(me_stamp)
    md_stamp = Stamp(state="Maryland", state_abbr="MD", stamp_url="/images/Maryland-stamp.jpg".lower(),
                     stamp_name="Maryland-stamp".lower(), blurb="This is the Maryland state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(md_stamp)
    ma_stamp = Stamp(state="Massachusetts", state_abbr="MA", stamp_url="/images/Massachusetts-stamp.jpg".lower(),
                     stamp_name="Massachusetts-stamp".lower(), blurb="This is the Massachusetts state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ma_stamp)
    mi_stamp = Stamp(state="Michigan", state_abbr="MI", stamp_url="/images/Michigan-stamp.jpg".lower(),
                     stamp_name="Michigan-stamp".lower(), blurb="This is the Michigan state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(mi_stamp)
    mn_stamp = Stamp(state="Minnesota", state_abbr="MN", stamp_url="/images/Minnesota-stamp.jpg".lower(),
                     stamp_name="Minnesota-stamp".lower(), blurb="This is the Minnesota state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(mn_stamp)
    ms_stamp = Stamp(state="Mississippi", state_abbr="MS", stamp_url="/images/Mississippi-stamp.jpg".lower(),
                     stamp_name="Mississippi-stamp".lower(), blurb="This is the Mississippi state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ms_stamp)
    mo_stamp = Stamp(state="Missouri", state_abbr="MO", stamp_url="/images/Missouri-stamp.jpg".lower(),
                     stamp_name="Missouri-stamp".lower(), blurb="This is the Missouri state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(mo_stamp)
    mt_stamp = Stamp(state="Montana", state_abbr="MT", stamp_url="/images/Montana-stamp.jpg".lower(),
                     stamp_name="Montana-stamp".lower(), blurb="This is the Montana state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(mt_stamp)
    ne_stamp = Stamp(state="Nebraska", state_abbr="NE", stamp_url="/images/Nebraska-stamp.jpg".lower(),
                     stamp_name="Nebraska-stamp".lower(), blurb="This is the Nebraska state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ne_stamp)
    nv_stamp = Stamp(state="Nevada", state_abbr="NV", stamp_url="/images/Nevada-stamp.jpg".lower(),
                     stamp_name="Nevada-stamp".lower(), blurb="This is the Nevada state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(nv_stamp)
    nh_stamp = Stamp(state="New Hampshire", state_abbr="NH", stamp_url="/images/NewHampshire-stamp.jpg".lower(),
                     stamp_name="New Hampshire-stamp".lower(), blurb="This is the New Hampshire state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(nh_stamp)
    nj_stamp = Stamp(state="New Jersey", state_abbr="NJ", stamp_url="/images/NewJersey-stamp.jpg".lower(),
                     stamp_name="New Jersey-stamp".lower(), blurb="This is the New Jersey state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(nj_stamp)
    nm_stamp = Stamp(state="New Mexico", state_abbr="NM", stamp_url="/images/NewMexico-stamp.jpg".lower(),
                     stamp_name="New Mexico-stamp".lower(), blurb="This is the New Mexico state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(nm_stamp)
    ny_stamp = Stamp(state="New York", state_abbr="NY", stamp_url="/images/NewYork-stamp.jpg".lower(),
                     stamp_name="New York-stamp".lower(), blurb="This is the New York state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ny_stamp)
    nc_stamp = Stamp(state="North Carolina", state_abbr="NC", stamp_url="/images/NorthCarolina-stamp.jpg".lower(),
                     stamp_name="North Carolina-stamp".lower(), blurb="This is the North Carolina state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(nc_stamp)
    nd_stamp = Stamp(state="North Dakota", state_abbr="ND", stamp_url="/images/NorthDakota-stamp.jpg".lower(),
                     stamp_name="North Dakota-stamp".lower(), blurb="This is the North Dakota state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(nd_stamp)
    oh_stamp = Stamp(state="Ohio", state_abbr="OH", stamp_url="/images/Ohio-stamp.jpg".lower(),
                     stamp_name="Ohio-stamp".lower(), blurb="This is the Ohio state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(oh_stamp)
    ok_stamp = Stamp(state="Oklahoma", state_abbr="OK", stamp_url="/images/Oklahoma-stamp.jpg".lower(),
                     stamp_name="Oklahoma-stamp".lower(), blurb="This is the Oklahoma state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ok_stamp)
    or_stamp = Stamp(state="Oregon", state_abbr="OR", stamp_url="/images/Oregon-stamp.jpg".lower(),
                     stamp_name="Oregon-stamp".lower(), blurb="This is the Oregon state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(or_stamp)
    pa_stamp = Stamp(state="Pennsylvania", state_abbr="PA", stamp_url="/images/Pennsylvania-stamp.jpg".lower(),
                     stamp_name="Pennsylvania-stamp".lower(), blurb="This is the Pennsylvania state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(pa_stamp)
    ri_stamp = Stamp(state="Rhode Island", state_abbr="RI", stamp_url="/images/RhodeIsland-stamp.jpg".lower(),
                     stamp_name="Rhode Island-stamp".lower(), blurb="This is the Rhode Island state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ri_stamp)
    sc_stamp = Stamp(state="South Carolina", state_abbr="SC", stamp_url="/images/SouthCarolina-stamp.jpg".lower(),
                     stamp_name="South Carolina-stamp".lower(), blurb="This is the South Carolina state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(sc_stamp)
    sd_stamp = Stamp(state="South Dakota", state_abbr="SD", stamp_url="/images/SouthDakota-stamp.jpg".lower(),
                     stamp_name="South Dakota-stamp".lower(), blurb="This is the South Dakota state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(sd_stamp)
    tn_stamp = Stamp(state="Tennessee", state_abbr="TN", stamp_url="/images/Tennessee-stamp.jpg".lower(),
                     stamp_name="Tennessee-stamp".lower(), blurb="This is the Tennessee state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(tn_stamp)
    tx_stamp = Stamp(state="Texas", state_abbr="TX", stamp_url="/images/Texas-stamp.jpg".lower(),
                     stamp_name="Texas-stamp".lower(), blurb="This is the Texas state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(tx_stamp)
    ut_stamp = Stamp(state="Utah", state_abbr="UT", stamp_url="/images/Utah-stamp.jpg".lower(),
                     stamp_name="Utah-stamp".lower(), blurb="This is the Utah state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(ut_stamp)
    vt_stamp = Stamp(state="Vermont", state_abbr="VT", stamp_url="/images/Vermont-stamp.jpg".lower(),
                     stamp_name="Vermont-stamp".lower(), blurb="This is the Vermont state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(vt_stamp)
    va_stamp = Stamp(state="Virginia", state_abbr="VA", stamp_url="/images/Virginia-stamp.jpg".lower(),
                     stamp_name="Virginia-stamp".lower(), blurb="This is the Virginia state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(va_stamp)
    wa_stamp = Stamp(state="Washington", state_abbr="WA", stamp_url="/images/Washington-stamp.jpg".lower(),
                     stamp_name="Washington-stamp".lower(), blurb="This is the Washington state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(wa_stamp)
    wv_stamp = Stamp(state="West Virginia", state_abbr="WV", stamp_url="/images/WestVirginia-stamp.jpg".lower(),
                     stamp_name="West Virginia-stamp".lower(), blurb="This is the West Virginia state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(wv_stamp)
    wi_stamp = Stamp(state="Wisconsin", state_abbr="WI", stamp_url="/images/Wisconsin-stamp.jpg".lower(),
                     stamp_name="Wisconsin-stamp".lower(), blurb="This is the Wisconsin state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(wi_stamp)
    wy_stamp = Stamp(state="Wyoming", state_abbr="WY", stamp_url="/images/Wyoming-stamp.jpg".lower(),
                     stamp_name="Wyoming-stamp".lower(), blurb="This is the Wyoming state stamp.",
                     date_issued="", country="United States", value="0.34")
    db.session.add(wy_stamp)
    db.session.commit()

"""
API CALLS
"""


# Get all the stamps
@app.route('/api/stamps/', methods=['GET'])
def get_stamps():
    all_stamps = json.loads(query_db())
    return json.dumps({'stamps': all_stamps[:]})


# Get the stamp by stamp ID
@app.route('/api/stamps/<int:stamp_id>/', methods=['GET', 'POST']) #Post conditional to be added if needed
def get_stamps_by_id(stamp_id):
        logger.info("in the GET method")
        all_stamps = json.loads(query_db())
        stamp = [stamp for stamp in all_stamps if stamp['id'] == stamp_id]
        if len(stamp) == 0:
            abort(404)
        return json.dumps({'stamps': stamp})


# Error handling for stamps not found by API request
@app.errorhandler(404)
def not_found(error=404):
    return make_response(jsonify({'error': 'Not Found'}), 404)


# Get stamp by state name
@app.route('/api/stamps/state/<state>/', methods=['GET'])
def get_stamps_by_name(state):
    logger.info("Collecting matching stamps with that name...")
    state = state.capitalize()
    stamp = [stamp for stamp in all_stamps if stamp['state'] == state]
    if len(stamp) == 0:
        abort(404)
    return json.dumps({'stamps': stamp})


# Get stamps by value -- greater than or equal to the variable in the url
@app.route('/api/stamps/value/<value>/', methods=['GET'])
def get_stamps_by_value(value):
    logger.info("Collecting stamps by value greater or equal to " + value + ".")
    stamp = [stamp for stamp in all_stamps if str(stamp['value']) >= value]
    if len(stamp) == 0:
        abort(404)
    return json.dumps({'stamp': stamp}, indent=4, separators=(',', ': '))


# Get states that have a common letter or string
@app.route('/api/stamps/letter/<letter>/', methods=['GET'])
def get_stamps_by_common_letter(letter):
    logger.info("Collecting stamps with a common or string of '" + letter + "'")
    letter = letter.lower()
    stamp = [stamp for stamp in all_stamps if letter in stamp['state'][:].lower()]
    if len(stamp) == 0:
        abort(404)
    return json.dumps({'stamps': stamp}, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    load_stamps()   # To be used only if the database needs to be reinitialized as all update info will be lost.
    all_stamps = json.loads(query_db())
    PORT = int(os.environ["PORT"], 5000)
    app.run(debug=True, port=PORT)
