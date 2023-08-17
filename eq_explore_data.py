from pathlib import Path
import json

import plotly.express as px
import numpy as np

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examine all the earthquakes in dataset
all_eq_dicts = all_eq_data["features"]

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# Normalize magnitudes
normalized_mags = np.array(mags)
normalized_mags = (normalized_mags - np.min(normalized_mags)) / (
    np.max(normalized_mags) - np.min(normalized_mags)
)

# Adjust marker size scaling
marker_scaling_factor = 10
scaled_marker_sizes = normalized_mags * marker_scaling_factor

title = "Global Magnitude 4.5+ Earthquakes, Past Month"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    title=title,
    size=scaled_marker_sizes,
    size_max=15,
    color=mags,
    color_continuous_scale="dense",
    labels={"color": "Magnitude", 'lon':"Longitude", 'lat':'Latitude'},
    projection="natural earth",
    hover_name=eq_titles,
)

# Customize hover label format
hover_template = (
    "<b>%{hovertext}</b><br>"
    "<b>Magnitude:</b> %{marker.color:.2f}<br>"
    "<b>Longitude:</b> %{lon}<br>"
    "<b>Latitude:</b> %{lat}<extra></extra>"
)
fig.update_traces(hovertemplate=hover_template)

fig.show()
