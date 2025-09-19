# House Price Prediction

A web-based application to predict house prices using a **Linear Regression** model trained on historical housing data. Users can input key features of a house to estimate its market price.

---

## Features

- Predict house prices based on numeric features like lot area, living area, bathrooms, garage, and pool area.
- Modern, responsive frontend with floating labels and professional styling.
- Backend implemented with **Flask**, using a pre-trained Linear Regression model.
- Handles missing values using **SimpleImputer**.
- Cross-origin requests supported for seamless frontend-backend communication.

---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn (LinearRegression, SimpleImputer)
- **Data Handling:** pandas
- **Model Persistence:** joblib
- **Version Control:** Git

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Raghava-2812/House_Price_Prediction.git
cd House_Price_Prediction
```
2. **Install dependencies:**
```bah
pip install flask pandas scikit-learn joblib flask-cors
```
3. **Run the Flask backend:**
```bash
python app.py
```
4. You should see: Running on http://127.0.0.1:5000
5. **Open frontend:**
- Open index.html in your browser.
