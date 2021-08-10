# Degree To DMS

This program receives degrees and converts it to degrees, minutes, and seconds or an API that receives degrees, minutes, and seconds and converts them into degree and responds to the results.

## Example

### Degree to DMS
```
GET /api/degreetodms?lat=37.55369139&long=128.2131775 HTTP/2
Host: coordtrans.appspot.com
```

### DMS to Degree
```
GET /api/dmstodegree?lat_degree=37&lat_arcminute=33&lat_arcsecond=13.289&long_degree=128&long_arcminute=12&long_arcsecond=47.439 HTTP/2
Host: coordtrans.appspot.com
```

## License
BSD
