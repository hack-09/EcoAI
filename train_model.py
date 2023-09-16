import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample training data (replace with your actual data)
X_train = np.array(["Air Quality","Water Pollution"])  # Replace with your data
y_train = np.array(["Air Quality","Water Pollution"])  # Replace with your labels

# Reshape X_train to make it a 2D array
X_train = X_train.reshape(0, 1)

# Split the data into training and testing sets (optional but recommended)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to 'model.pkl' file
joblib.dump(model, 'model.pkl')

print('Model training and saving completed.')
