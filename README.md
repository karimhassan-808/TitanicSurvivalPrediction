# 🚢 Titanic Survival Prediction - Machine Learning Project

This project uses machine learning to predict whether a passenger would survive the Titanic disaster, based on data such as age, class, fare, and embarkation point. It includes exploratory data analysis (EDA), model building, evaluation, and a user-friendly web app powered by Streamlit.

---

## 📂 Project Structure

```
📁 titanic-survival-ml-app/
│
├── app.py
├── titanic_randomforest_model.pkl  ✅ "the one in use after doing the comparison"
├── titanic_decisiontree_model.pkl
├── requirements.txt
├── README.md
│
├── notebooks/
│   ├── titanic_eda.ipynb
│   └── titanic_ml.ipynb
```

---

## 🧠 Machine Learning Models Used

| Model                | Accuracy | F1 Score | ROC-AUC |
|---------------------|----------|----------|---------|
| Decision Tree        | 78.8%    | 0.747    | 0.803   |
| Logistic Regression  | 81.0%    | 0.764    | 0.883   |
| Random Forest        | 81.0%    | **0.770** | **0.893** |
| K-Nearest Neighbors  | 71.5%    | 0.604    | 0.763   |
| XGBoost              | 65.9%    | 0.384    | 0.804   |

📌 **Best Performing Model:** Random Forest — highest F1 score and ROC-AUC, making it the optimal balance between precision and recall.

---

## 🚀 Streamlit App

A simple web app where users can input passenger details and get a survival prediction based on the trained Random Forest model.

---

## 📦 Installation
1 - Clone the repo:
```
git clone https://github.com/your-username/titanic-ml-project.git
cd titanic-ml-project
```
2 - Install dependencies:
```
pip install -r requirements.txt
```

## 🚀 How to run
- run this in terminal.
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack
- Python

- Pandas, NumPy, Scikit-learn

- Seaborn, Matplotlib

- Streamlit

- Joblib

---

## 📚 What I Learned
- Performing EDA and data preprocessing (encoding, filling missing values)

- Evaluating classification models using metrics like accuracy, F1, ROC-AUC

- Comparing model performance to select the best fit

- Deploying a machine learning model with a UI via Streamlit

---

## Project Video
[Titanic Survival Predictor](https://github.com/user-attachments/assets/50e94f25-0ec0-44d8-b2df-15317a81626b)

---

## 📬 Contact
📧 [Email](mailto:karimhassanbinich@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/karim-hassan-30b389315/)
