# Car Price Prediction using Machine Learning

This project predicts car prices based on various features using a machine learning model. The dataset contains information about car characteristics like fuel type, body style, engine location, etc. A linear regression model is used to predict the price of the car.


## Project Overview

The goal of this project is to predict the prices of cars using the `CarPrice_Assignment.csv` dataset. A linear regression model is trained on the data, and the performance is evaluated using metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared. The project also includes a correlation heatmap to visualize the relationships between features.

## Dataset

The dataset used for this project is `CarPrice_Assignment.csv`. It contains information about cars, including features like:
- `fueltype`: The type of fuel used by the car (e.g., petrol, diesel)
- `carbody`: The body type of the car (e.g., sedan, hatchback)
- `drivewheel`: The type of drive (e.g., front-wheel drive, rear-wheel drive)
- And more…

The dataset is available in this repository and should be placed in the same directory as `app.py` for easy access.

## Features

The model uses the following features to predict the price of a car:
- `brand`: The brand of the car.
- `fueltype`: The type of fuel used by the car.
- `aspiration`: The aspiration type of the car (e.g., turbo, standard).
- `doornumber`: The number of doors.
- `carbody`: The car body style (e.g., sedan, hatchback).
- `drivewheel`: Type of drive (e.g., front-wheel drive, rear-wheel drive).
- `enginelocation`: Location of the engine (e.g., front, rear).
- `fuelsystem`: Type of fuel system used.
- `enginetype`: Type of engine (e.g., overhead valves, push rod).
- `cylindernumber`: Number of cylinders.

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your system. You will also need to install the dependencies listed in the `requirements.txt` file.

### Steps to Set Up:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/car-price-prediction.git
   cd car-price-prediction
   ```

2. **Set up a virtual environment (recommended):**

   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - For Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**: Ensure that the `CarPrice_Assignment.csv` dataset is in the same directory as `app.py`.

## Usage

### Running the Application

Once the dependencies are installed and the dataset is in place, you can run the project by following these steps:

1. **Activate the virtual environment** (if not already active):
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Run the Python script:**
   ```bash
   python app.py
   ```

3. The script will generate:
   - A **correlation matrix heatmap** showing the relationships between different features.
   - **Model performance metrics** like Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared score.
   - A **scatter plot** comparing the actual vs. predicted car prices.

## Results

The project evaluates the performance of the linear regression model using the following metrics:
- **Mean Squared Error (MSE)**: Measures the average squared difference between predicted and actual values.
- **Root Mean Squared Error (RMSE)**: The square root of MSE, providing a more interpretable error value.
- **R-squared**: Indicates how well the model explains the variance in the target variable (price).

### Example Output:
- **Mean Squared Error (MSE)**: 11623237.545
- **Root Mean Squared Error (RMSE)**: 3409.2869
- **R-squared**: 0.85

Additionally, the scatter plot compares actual values against predicted values, with a red line indicating perfect predictions.

## Contributing

Contributions are welcome! If you want to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Open a pull request describing your changes.


