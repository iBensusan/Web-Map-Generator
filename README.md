# Interactive Map Generator

This project is a Python-based application that uses the `Folium` library to generate interactive maps. It visualizes the locations of volcanoes and provides a dynamic population layer using GeoJSON data. The map is generated and saved as an HTML file, which can be opened in any web browser.

## Features

- **Volcanoes Layer**: Shows the locations of volcanoes with colored markers based on their elevation. 
    - Green: Elevation < 1000 meters
    - Orange: 1000 meters <= Elevation < 3000 meters
    - Red: Elevation >= 3000 meters
- **Population Layer**: Visualizes world population data using GeoJSON. Countries are colored based on their population size in 2005.
    - Green: Population < 10 million
    - Orange: 10 million <= Population < 20 million
    - Red: Population >= 20 million
- **Layer Control**: Users can toggle between the volcano and population data layers.

## Requirements

- Python 3.x
- Folium: `pip install folium`
- Pandas: `pip install pandas`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MapProject.git
    cd MapProject
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that `Volcanoes.txt` and `world.json` files are available in the project directory.

## Usage

To generate the map, simply run the following command in your terminal:

```bash
python map_generator.py
