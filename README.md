# House Price Prediction Web App

## Overview
This is a simple and professional web application that predicts house prices based on key features of a property. The frontend uses HTML, CSS, and JavaScript, and the backend is powered by **Python Flask** with a **Linear Regression model** built using scikit-learn.

The app allows users to input important property features such as lot area, ground living area, number of full bathrooms, garage area, and pool area, and returns an estimated house price.

---

## Features

- Modern, professional UI with floating labels and gradient accents.
- Responsive design for desktop and mobile devices.
- Real-time prediction using a trained **Linear Regression model**.
- Easy-to-use input fields with placeholders and units for clarity.
- Clean error handling for network or server issues.

---

## Technology Stack

**Frontend:**
- HTML5 & CSS3
- JavaScript (Fetch API)

**Backend:**
- Python 3.x
- Flask (Web server)
- scikit-learn (Linear Regression)
- pandas (Data handling)
- SimpleImputer (Handling missing values)

---

## Input Fields

| Field        | Description                     | Units           | Example  |
| ------------ | ------------------------------- | --------------- | -------- |
| LotArea      | Lot area of the property        | Square feet     | 8450     |
| GrLivArea    | Ground living area              | Square feet     | 1710     |
| FullBath     | Number of full bathrooms        | Count           | 2        |
| GarageArea   | Garage area                     | Square feet     | 548      |
| PoolArea     | Pool area                       | Square feet     | 0        |

---

## How to Run

### Prerequisites
- Python 3.x installed
- pip installed

### Install Dependencies
```bash
pip install flask pandas scikit-learn
```
### Start the Flask Server
```bash
python app.py
```

- The server will start at http://127.0.0.1:5000.

### Open Frontend

Open the index.html file in a web browser. Enter the house details in the input fields and click Predict Price to get an estimate.

### Project Structure
```bash
House_Price_Prediction/
│
├── model/
│   └── house_model.pkl
│   └── imputer.pkl
├── templates/
│   └── index.html
├── app.py
├──House_price_predicton.py
├── train.csv
├── test.csv

```
