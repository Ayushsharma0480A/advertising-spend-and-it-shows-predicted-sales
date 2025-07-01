# 📊 Advertising Spend vs. Sales Predictor
This project predicts how many units will be sold based on the advertising spend, using a Linear Regression model.  
It also features an interactive **Streamlit dashboard** where users can input ad budgets and instantly see predicted sales.
- 📈 Predicts sales based on ad budget
- 💡 Real-world regression modeling
- 🎯 Streamlit dashboard for interactivity
- 💾 Model saved with Joblib
      - Python
      - scikit-learn
      - Streamlit
      - joblib
      - NumPy
      - Jupyter Notebook
1. Model Performance
    - Training R² Score: **0.7426**
    - Cross-validation R² Score: **0.7327**
    - ✅ No overfitting detected
  📦 9. Project Structure
      ├── app.py                   # Streamlit app
      ├── sales_model.joblib       # Trained model
      ├── requirements.txt         # Dependencies
      ├── notebooks/
      │   └── model_training.ipynb # Jupyter Notebook for training
      └── README.md
