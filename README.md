# 🛍️ Shopper Spectrum: Customer Segmentation & Product Recommendation

## 📂 Project Description

This project focuses on analyzing customer transaction data from an e-commerce platform to derive actionable insights using RFM analysis, customer segmentation, and collaborative filtering. The solution includes a Streamlit app that delivers real-time customer segmentation and product recommendations based on user input.

---

## 🔧 Files Included

| File Name                       | Description                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `Shopper_spectrum.ipynb`        | Jupyter Notebook for EDA, RFM feature engineering, clustering, and similarity matrix creation                                |
| `pr_recommendation.py`          | Streamlit web app integrating customer segmentation and product recommendation features                                      |
| `rfm_kmeans_model.pkl`          | Serialized model file containing trained KMeans model, StandardScaler, PCA transformer, and cluster-to-segment label mapping |
| `product_similarity_matrix.pkl` | Cosine similarity matrix of products for item-based collaborative filtering                                                  |

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

> Ensure the following files are in the same folder:
>
> * `pr_recommendation.py`
> * `rfm_kmeans_model.pkl`
> * `product_similarity_matrix.pkl`

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




