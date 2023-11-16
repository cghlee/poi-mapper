# PoI Mapper

A project created to enable mapping of a large number of points of interest
(PoIs) for a given location to enable easier visualisation of routing between
PoIs, and easier identification of PoIs on the fly (e.g. for nearby spots to
sightsee, have lunch or dinner, or grab a drink).

The PoI Mapper outputs an interactive map in HTML format to either locally
store or host online as a web page.

## Dependencies

PoI Mapper requires the `Folium` module, which can be installed via `venv` and
the `requirements.txt` file provided. Relevant documentation is linked below:

- [Folium](https://pypi.org/project/folium/)
- [venv](https://docs.python.org/3/library/venv.html)

## How to Use

Run `poi_mapper.py`, which will operate according to functions defined
within `functions_folium.py`, `functions_json.py`, and `functions_pois.py`.

If locally-stored `location.json` or `pois.json` files do not exist, these will
be generated based on location and PoI data inputted by the user on the first
run of the program. Else, such data will be automatically imported.

Information on map bounding coordinates can be obtained by using the export
functionality on [OpenStreetMap](https://www.openstreetmap.org/).

Latitude and longitude coordinates for a given PoI can be found by right-
clicking on its location in Google Maps, selecting the coordinates option at
the top of the pop-up menu, and pasting into the PoI Mapper when prompted.
