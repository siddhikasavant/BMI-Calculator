# 🧮 BMI Calculator App

A simple and interactive **Body Mass Index (BMI) Calculator**, made using **Random Forest Classifier** built using **Streamlit**!  
Predict your BMI category based on **Gender**, **Height**, and **Weight** using a **pre-trained Machine Learning model**.  
Deployed live: 
[Click to try the app](https://siddhikabmicalculator.streamlit.app)

---

## 🧠 About the Project

The BMI Calculator:
- Takes user input: Gender, Height (in cm), and Weight (in kg)
- Predicts BMI category using a **classification ML model**
- Shows results with categories like:  
  `0 - Extremely Weak`, `1 - Weak`, `2 - Normal`, `3 - Overweight`, `4 - Obesity`, `5 - Extreme Obesity`

---

## 🧪 Tech Stack

- 🐍 Python
- 📊 Pandas & NumPy
- 🧠 scikit-learn (RandomForestClassifier)
- 💾 joblib (for model saving/loading)
- 🎨 Streamlit (UI)
- ☁️ Streamlit Cloud (Deployment)

---

## 📂 Project Structure

```
BMI-Calculator/
├── app.py                  
├── bmi_model.joblib     
├── bmi.csv         
├── requirements.txt
├── model_evaluation.ipynb
├── LICENSE    
└── README.md               
````

---

## 🚀 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/siddhikasavant/BMI-Calculator.git
cd BMI-Calculator
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run Streamlit app**

```bash
streamlit run app.py
```

---

## 🔗 Live App

Try it out here:
🌐 [https://siddhikabmicalculator.streamlit.app](https://siddhikabmicalculator.streamlit.app)

---

## 📝 Model Training Summary

* Used Random Forest Classifier for prediction
* Trained on dataset with features:

  * `Gender`, `Height`, `Weight`
* Target variable: `Index` (BMI Category)

---

## 👩‍💻 Author

**Siddhika Savant**
📌 [GitHub](https://github.com/siddhikasavant) | [LinkedIn](https://linkedin.com/in/siddhikasavant)

---

## ⭐️ Show Your Support

If you found this useful:

* 🌟 Star the repo
* 🛠️ Fork and contribute
* 💬 Share your feedback!

---

## 📌 License

This project is licensed under the **MIT License**.

---

```

---

Just drop me the links or say *“yes chef”* 😎👩‍🍳
```
