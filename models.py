# models.py

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class RecommendationModel:
    def __init__(self):
        # Load a pre-trained machine learning model
        self.model = self.load_or_train_model()

    def load_or_train_model(self):
        try:
            # Load the pre-trained model
            return joblib.load('model.pkl')
        except FileNotFoundError:
            # If the pre-trained model is not found, train a new model
            return self.train_model()

    def train_model(self):
        # Sample training data (replace with your actual data)
        X_train = np.array(["Air Quality","Water Pollution"])  # Replace with your data
        y_train = np.array(["Air Quality","Water Pollution"])  # Replace with your labels

        # Reshape X_train to make it a 2D array
        X_train = X_train.reshape(0, 1)

        # Split the data into training and testing sets (optional but recommended)
        X_train,y_train= train_test_split(X_train, y_train, test_size=0.2, random_state=42)

        # Train a Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Save the trained model to 'model.pkl' file
        joblib.dump(model, 'model.pkl')

        return model

    def get_air_quality_recommendations(self, air_quality):
        # Use the model to generate recommendations based on air quality
        recommendations = self.model.predict([[air_quality]])
        return recommendations

    def get_water_pollution_recommendations(self, water_pollution):
        # Use the model to generate recommendations based on water pollution
        recommendations = self.model.predict([[water_pollution]])
        return recommendations

    def get_combined_recommendations(self, air_quality, water_pollution):
        air_quality_recommendations = self.get_air_quality_recommendations(air_quality)
        water_pollution_recommendations = self.get_water_pollution_recommendations(water_pollution)

        # Combine or process recommendations as needed
        combined_recommendations = (air_quality_recommendations, water_pollution_recommendations)
        return combined_recommendations
