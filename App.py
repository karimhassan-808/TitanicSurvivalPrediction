import streamlit as st
import pandas as pd
import joblib
import sklearn
from sklearn.tree import DecisionTreeClassifier

# Load the trained rf_model
rf_model = joblib.load("titanic_randomforest_model.pkl")

# Define input fields
st.title("Titanic Survival Predictor")

st.write("Enter the passenger's details:")

# Input fields
Pclass = st.selectbox("Passenger Class", [1, 2, 3])
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.slider("Age", 0, 100, 25)
SibSp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
Parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
Fare = st.number_input("Fare Paid", min_value=0.0, max_value=600.0, value=30.0)
Embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

if st.button("Predict Survival"):
    # Binary encoding for 'Sex'
    sex_encoded = 1 if Sex == "male" else 0  # Sex

    # One-hot encoding for 'Embarked'
    embarked_C = 1 if Embarked == "C" else 0
    embarked_Q = 1 if Embarked == "Q" else 0
    embarked_S = 1 if Embarked == "S" else 0

    # Final input features based on training
    input_df = pd.DataFrame([{
        "Pclass": Pclass,
        "Sex": sex_encoded,
        "Age": Age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "Embarked_C": embarked_C,
        "Embarked_Q": embarked_Q,
        "Embarked_S": embarked_S
    }])

    # Predict
    prediction = rf_model.predict(input_df)[0]

    # Output result
    st.subheader("Prediction:")
    if prediction == 1:
        st.success("They would have SURVIVED!")
    else:
        st.error("They would NOT have survived...")
