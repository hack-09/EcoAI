import requests
from flask import Flask, jsonify, redirect, render_template, request, session
from models import RecommendationModel
from data_preprocessing import preprocess_data

app = Flask(__name__)


# Load and preprocess environmental data
data = preprocess_data('environmental_data.csv')

# Load pre-trained recommendation model
model = RecommendationModel()

API_KEY = 'c8c56e6a28f9678f8a234d0bcf251745'

def get_current_temperature(city_name):
    # Make a GET request to the OpenWeatherMap API
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Extract the current temperature from the JSON response
        temperature = data['main']['temp']
        return temperature
    else:
        return None

def get_current_climate_pattern(city_name):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            return weather_description
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

@app.route('/get_data')
def get_data():
    city = request.args.get('city')
    
    temperature = get_current_temperature(city)
    climate_pattern = get_current_climate_pattern(city)
    
    data = {
        'temperature': temperature if temperature is not None else 'N/A',
        'climate_pattern': climate_pattern if climate_pattern is not None else 'N/A'
    }
    
    return jsonify(data)


@app.route('/')
def index():
    air_quality = data['Air Quality'].iloc[1]
    water_pollution = data['Water Pollution'].iloc[1]
    combined_recommendations = model.get_combined_recommendations(air_quality, water_pollution)
    air_quality_health = 'Good' if air_quality > 0 else 'Poor'
    water_pollution_health = 'Low' if water_pollution > 0 else 'High'
    

    return render_template('index.html',
                           air_quality_recommendations=combined_recommendations[0],
                           water_pollution_recommendations=combined_recommendations[1],
                           air_quality_health=air_quality_health,
                           water_pollution_health=water_pollution_health)

@app.route('/favicon.ico')
def favicon():
    # Return a default favicon.ico file or a 404 response
    # You can replace 'favicon.ico' with the actual path to your favicon file
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
