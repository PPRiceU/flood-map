#!/usr/bin/env python3
import urllib.request

site_keys = {
    'charleston': 'cj7f7c6sj0rvz32rs91o9ujf2',
    'fortlauderdale': 'cj7f7d7i60uxv34mtr4zux3ua',
    'jacksonville': 'cj7f7cmoi0w752wlxsozcxbcf',
    'miami': 'cj7ctr3ov025f2qnpmgly9829',
    'orlando': 'cj7ctreuo02cx2ppjg9wxcgv6',
    'palmbeach': 'cj7ctrqlx028r2wnpeubytt6m',
    'savannah': 'cj7f7cd9o0vm12wo3mf2v1wdf',
    'tallahassee': 'cj7f7cvbn0vic2wkyhakqcf4x',
    'tampa': 'cj7cts9mp02d32xmtanabe06n'
}

base = 'https://api.mapbox.com/datasets/v1/tailwindlabs/{}/features'
token = 'sk.eyJ1IjoidGFpbHdpbmRsYWJzIiwiYSI6ImNqNnY0cGN2MzEwM3EzMnBkNHM3OWoxaWgifQ.3rwB8LW4khqcDoEekNCbTg'

# Get the archives
for key in site_keys.keys():

    # Get and save the file
    base_this = base.format(site_keys[key])
    try:
        urllib.request.urlretrieve('{}?access_token={}'.format(base_this, token), key + '.geojson')
    except urllib.error.URLError as e:
        print('Error: ' + e.reason)
