from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask('degreetodms')


def calc_dms(degree):
    degree_ = int(degree)
    arcminute = int((degree - degree_) * 60)
    arcsecond = (((degree - degree_) * 60) - int((degree - degree_) * 60)) * 60

    return dict(degree=degree_, arcminute=arcminute, arcsecond=round(arcsecond, 3))
    

@app.route('/api/degreetodms')
def main():
    if 'lat' not in request.args:
        raise BadRequest('', jsonify(code=400, message='Latitude가 전달되지 않았습니다'))
    
    if 'long' not in request.args:
        raise BadRequest('', jsonify(code=400, message='Longitude가 전달되지 않았습니다'))

    latitude = float(request.args['lat'])
    longitude = float(request.args['long'])

    return jsonify(lat=calc_dms(latitude), long=calc_dms(longitude))
