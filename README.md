# 💻 Laptop Price Predictor

A machine learning web application that predicts the price of a laptop based on its specifications. Built using a trained pipeline model and deployed via Streamlit.

---

## 🔍 Overview

This project explores a dataset of laptop specifications and builds a regression model to predict laptop prices. The final trained pipeline (including preprocessing and model) is exported and used in a user-friendly Streamlit app.

---

## 📦 Features

- Cleaned and preprocessed laptop dataset
- Feature engineering: handling categorical, numerical, and derived features
- Pipeline creation for reproducible preprocessing and modeling
- Model selection and evaluation using various regression algorithms
- Exported model using `joblib`
- Interactive web application with Streamlit to predict laptop prices

---

> **Note:** The app uses the trained `pipe.pkl` file to load the pipeline and predict prices.

---

## 🧠 Machine Learning Workflow

- **EDA & Feature Engineering:** Extracted features like RAM, storage, GPU brand, etc.
- **Pipeline:** Used `ColumnTransformer` and `Pipeline` for preprocessing + model
- **Models tried:** Linear Regression, Ridge, Lasso, Random Forest, etc.
- **Best model:** Exported using `joblib` and integrated into the Streamlit app

---

## 📁 Project Structure

```
├── app.py
├── model/
│   └── pipe.pkl
├── laptop_price_predictor.ipynb
├── requirements.txt
└── README.md
```

---

## 📊 Sample Inputs for Prediction

The model predicts laptop prices based on:

- Brand
- Type of Laptop
- RAM (in GB)
- Weight
- Touchscreen or not
- IPS Display or not
- Screen Size
- Screen Resolution
- CPU Brand
- GPU Brand
- HDD/SSD
- Operating System

---

---

## 📈 Sample Output

> 💬 “A Dell Gaming Laptop with i7 CPU, 16GB RAM, and SSD might cost around ₹80,000.”

---

## 📚 Dataset

Dataset was scraped or collected manually from online sources. You may replace this with a Kaggle link if applicable.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---


