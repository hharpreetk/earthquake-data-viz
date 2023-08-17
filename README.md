# Earthquake Visualization with Plotly

This Python script uses Plotly Express to create a global earthquake visualization based on earthquake data from a GeoJSON file. The script reads earthquake data, extracts relevant information, and creates an interactive scatter plot on a map.

## Prerequisites

- Python 3.x
- Required Python packages: `plotly`, `numpy`

## Installation

#### 1. Clone or download this repository.
   ```
   git clone https://github.com/hharpreetk/earthquake-data-viz.git
   ```
#### 2. Install the required packages.
    pip install plotly numpy
    
## Usage

1. Place your GeoJSON earthquake data file in the `eq_data` directory (create if not exists).

2. Run the script `eq_explore_data.py`.


3. The script will generate an interactive scatter plot using Plotly Express. The plot displays earthquake magnitudes, locations, and titles. Hover over the markers for detailed information.

## Customization

- You can customize the marker scaling, color scale, and other visual properties by modifying the script.
- Adjust the `marker_scaling_factor` and `size_max` variables to control the size of markers.
- Modify the `color_continuous_scale` parameter to change the color gradient.
- Update the `title` variable to set the title of the plot.

## Credits

- Earthquake data: [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/)
- Plotly Express: [Plotly](https://plotly.com/python/plotly-express/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

