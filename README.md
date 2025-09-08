<<<<<<< HEAD
# 🩺 Breast Cancer Prediction Model using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green?logo=flask)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)

---

## 🚀 Project Overview

Predict breast cancer diagnosis (malignant or benign) using machine learning. This project combines data science, web development, and interactive analysis for impactful medical insights.

---

## ✨ Features

- 📊 Data analysis & visualization in Jupyter Notebook
- 🤖 Machine learning model training & evaluation
- 🌐 Flask web app for instant predictions
- 🎨 Interactive Bootstrap-powered web interface
- 💾 Model serialization for fast, repeatable results

---

## 📁 Dataset Description

`breast cancer.csv` contains:

- **ID**
- **Diagnosis**: `M` = Malignant, `B` = Benign
- **30 real-valued features**: radius_mean, texture_mean, perimeter_mean, area_mean, etc.

---

## 🛠️ Model Building & Training

Notebook: `Breast Cancer Prediction using Machine Learning.ipynb`

- Data loading & exploration
- Data cleaning (missing values, column drops)
- Feature selection & scaling
- Model training (Logistic Regression, SVM, Random Forest, etc.)
- Evaluation (accuracy, confusion matrix)
- Model saved as `model.pkl`

---

## 🌐 Web Application Usage

App: `app.py` | Interface: `index.html`

- Enter features as comma-separated values
- Get instant prediction: **Malignant** or **Benign**
- Visual feedback with images & messages

#### Example Input

`17.99,10.38,122.8,1001,...` _(30 features)_

---

## 📒 Jupyter Notebook Analysis

- Step-by-step data exploration
- Feature distribution plots
- Model training & validation
- Insights into feature importance

---

## ⚡ Installation & Setup

```bash
git clone https://github.com/Artamta/Brest_Cancer_Detection_Model.git
cd Brest_Cancer_Detection_Model
pip install flask numpy pandas scikit-learn
# (Optional) For notebook analysis
pip install notebook
```

---

## ▶️ How to Run

### Run Flask Web App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and enter features to predict.

### Run Jupyter Notebook

```bash
jupyter notebook "Breast Cancer Prediction using Machine Learning.ipynb"
```

---

## 🏆 Results & Performance

- High accuracy in distinguishing malignant/benign tumors
- Metrics & visualizations in notebook
- Instant web predictions

---

## 📂 File Structure

```
├── app.py                        # Flask web application
├── index.html                    # Web interface template
├── model.pkl                     # Trained ML model
├── breast cancer.csv             # Dataset
├── Breast Cancer Prediction...   # Jupyter notebook
├── README.md                     # Project documentation
├── Breast Cancer Project...      # Project report (docx)
```

---

## 📚 References

- [UCI ML Repository: Breast Cancer Wisconsin (Diagnostic)](<https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)>)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

## 💬 Contact

**Project Owner:** Artamta  
**GitHub:** [Artamta](https://github.com/Artamta)

---

> 🧠 _This project demonstrates the power of machine learning in medical diagnostics and provides a user-friendly interface for real-world application._
=======
# Brest_Cancer_Detection_Model
>>>>>>> d90078e9c7b07b538cbf381c2cf827cbb789e378
