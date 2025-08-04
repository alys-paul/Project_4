# 🛍️ Shopper Spectrum: Customer Segmentation & Product Recommendation

## 📂 Project Description

This project focuses on analyzing customer transaction data from an e-commerce platform to derive actionable insights using RFM analysis, customer segmentation, and collaborative filtering. The solution includes a Streamlit app that delivers real-time customer segmentation and product recommendations based on user input.

---

## 🔧 Files Included

| File                         | Purpose                                 |
|------------------------------|-----------------------------------------|
| `app.py` | Main Streamlit app                    |
| `online_retail.csv`         | Transaction dataset                     |
| `kmeans_model.pkl`          | Pretrained clustering model             |
| `scaler.pkl`                | Pre-fitted scaler for RFM normalization |
| `item_similarity.pkl`       | Product similarity matrix               |
| `product_map.pkl`           | StockCode → Product name mapping        |
| `requirements.txt`          | Required Python libraries               |

---

## 🚀 Features

### 📊 Dashboard (EDA)
- Top countries by transactions
- Best-selling products
- Monthly sales trend

### 🎯 Product Recommendation
- Input: Product **name**
- Output: 5 similar products based on cosine similarity

### 🔍 Customer Segmentation
- Input: Recency, Frequency, Monetary
- Output: Predicted customer segment:
  - High-Value
  - Regular
  - Occasional
  - At-Risk

---

## 📈 Streamlit App Features

### 🎯 1️⃣ Product Recommendation Module

* **Objective**: Suggests 5 similar products based on purchase history.
* **How It Works**:

  * User enters a product name.
  * The app uses cosine similarity on a customer-product quantity matrix.
  * Top 5 similar products are displayed.

### 🧠 2️⃣ Customer Segmentation Module

* **Objective**: Categorizes a customer into a behavior-based segment.
* **How It Works**:

  * User inputs: Recency, Frequency, and Monetary values.
  * The app applies StandardScaler → PCA → KMeans to predict the cluster.
  * Outputs the interpreted customer segment (e.g., High-Value, At-Risk).

---

## ▶️ How to Run the App

1. ✅ Install required packages:

```bash
pip install streamlit pandas numpy scikit-learn
```

2. ▶️ Launch the Streamlit app:

```bash
streamlit run pr_recommendation.py
```

> Ensure the above files are in the same folder

---

## 🔍 Behind the Scenes

* **Clustering**:

  * Features: Recency, Frequency, Monetary
  * Scaled using StandardScaler
  * Dimensionality reduced using PCA (2 components)
  * Clustered using KMeans (4 clusters)
  * Interpreted using RFM averages & ranked scoring

* **Recommendations**:

  * Built using item-based collaborative filtering
  * Cosine similarity computed on product purchase matrix (CustomerID × Product)

---

## 🧾 Technical Keywords

`Pandas`, `Numpy`, `Data Cleaning`, `Feature Engineering`, `EDA`, `RFM`, `Customer Segmentation`, `KMeans`, `PCA`, `Cosine Similarity`, `Collaborative Filtering`, `Streamlit`, `Retail Analytics`, `Machine Learning`, `Real-Time Prediction`

---




