from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


def calc_dms(degree):
    degree_ = int(degree)
    arcminute = int((degree - degree_) * 60)
    arcsecond = (((degree - degree_) * 60) - int((degree - degree_) * 60)) * 60

    return dict(degree=degree_, arcminute=arcminute, arcsecond=round(arcsecond, 3))


def calc_degree(degree, arcminute, arcsecond):
    return degree + (arcminute / 60) + (arcsecond / 3600)


@app.route('/api/degreetodms')
def degreetodms():
    if 'lat' not in request.args:
        raise BadRequest('', jsonify(code=400, message='Latitude가 전달되지 않았습니다'))
    
    if 'long' not in request.args:
        raise BadRequest('', jsonify(code=400, message='Longitude가 전달되지 않았습니다'))

    latitude = float(request.args['lat'])
    longitude = float(request.args['long'])

    return jsonify(lat=calc_dms(latitude), long=calc_dms(longitude))


@app.route('/api/dmstodegree')
def dmstodegree():
    valdate_fields = ('lat_degree', 'lat_arcminute', 'lat_arcsecond', 'long_degree', 'long_arcminute', 'long_arcsecond')
    for field in valdate_fields:
        if field not in request.args:
            raise BadRequest('', jsonify(code=400, message=f'{field}가 전달되지 않았습니다'))

    lat_degree = float(request.args['lat_degree'])
    lat_arcminute = float(request.args['lat_arcminute'])
    lat_arcsecond = float(request.args['lat_arcsecond'])

    long_degree = float(request.args['long_degree'])
    long_arcminute = float(request.args['long_arcminute'])
    long_arcsecond = float(request.args['long_arcsecond'])

    return jsonify(lat=calc_degree(lat_degree, lat_arcminute, lat_arcsecond),
                   long=calc_degree(long_degree, long_arcminute, long_arcsecond))
