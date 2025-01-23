import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
car_prices = pd.read_csv("CarPrice_Assignment.csv")
print(car_prices.info())
print(car_prices.describe())

# Visualizing the data
car_prices.hist(bins=30, figsize=(20, 15))

# Encoding categorical columns
def encode_columns_label(car_prices, columns):
    le = LabelEncoder()
    for col in columns:
        car_prices[col] = le.fit_transform(car_prices[col])
    return car_prices

columns_to_encode = ['fueltype', 'aspiration', 'brand', 'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'fuelsystem', 'enginetype', 'cylindernumber']
car_prices = encode_columns_label(car_prices, columns_to_encode)

# Drop unnecessary columns
car_prices = car_prices.drop(['CarName', 'car_ID'], axis=1)

# Correlation matrix visualization
correlation_matrix = car_prices.corr().abs()
plt.figure(figsize=(20, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Target correlation
Correlation_with_target = correlation_matrix['price'].sort_values(ascending=False)
print(Correlation_with_target)

# Drop low correlation features
threshold = 0.1
low_correlation_features = Correlation_with_target[abs(Correlation_with_target) < threshold].index
df_dropped = car_prices.drop(columns=low_correlation_features)

# Prepare target and features
target_column = 'price'
x = df_dropped.drop(columns=[target_column])
y = df_dropped[target_column]

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model fitting
model = LinearRegression()
model.fit(x_train, y_train)

# Predictions and evaluation
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error: {rmse}')
r_squared = model.score(x_test, y_test)
print(f'R-squared: {r_squared}')

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='blue', label='Predicted vs Actual')
plt.plot(y_test, y_test, color='red', linestyle='--', label='Perfect Fit (y = x)') 

# Add labels, title, and legend
plt.xlabel('Actual Values (y_test)', fontsize=12)
plt.ylabel('Predicted Values (y_pred)', fontsize=12)
plt.title('Model Fit: Actual vs Predicted Values', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
