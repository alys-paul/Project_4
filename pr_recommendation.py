import streamlit as st
import pickle
import numpy as np

# --- Load KMeans Model, Scaler, and Segment Map ---
try:
    with open("rfm_kmeans_model.pkl", "rb") as f:
        model_data = pickle.load(f)
        kmeans = model_data["model"]
        scaler = model_data["scaler"]
        segment_map = model_data.get("segment_map", {})  # Optional
except Exception as e:
    st.error(f"Error loading clustering model: {e}")
    st.stop()

# --- Load Product Similarity Matrix ---
try:
    with open("product_similarity_matrix.pkl", "rb") as f:
        similarity_matrix = pickle.load(f)
except Exception as e:
    st.error(f"Error loading product similarity matrix: {e}")
    st.stop()

# --- Product Recommendation Function ---
def get_similar_products(product_name, similarity_matrix, top_n=5):
    if product_name not in similarity_matrix.columns:
        return []
    similar_scores = similarity_matrix[product_name].sort_values(ascending=False)
    return similar_scores.iloc[1:top_n+1]  # skip the product itself

# --- Sidebar Navigation ---
st.sidebar.title("🛍️ Shopper Spectrum")
page = st.sidebar.radio("Go to", ["🔁 Recommendation", "📊 Segmentation"])

# -------------------------------
# 🎯 PRODUCT RECOMMENDATION PAGE
# -------------------------------
if page == "🔁 Recommendation":
    st.title("🎯 Product Recommendation")
    st.markdown("Enter a product name to get 5 similar product suggestions.")

    product_input = st.text_input("Enter Product Name", placeholder="E.g. GREEN VINTAGE SPOT BEAKER").strip().upper()

    if st.button("Get Recommendations"):
        if product_input:
            recommendations = get_similar_products(product_input, similarity_matrix)
            if isinstance(recommendations, list) or recommendations.empty:
                st.warning("❌ Product not found. Please try a valid name.")
            else:
                st.success("🔍 Top 5 Similar Products:")
                for product, score in recommendations.items():
                    st.markdown(f"- 🛍️ **{product}**")
        else:
            st.warning("Please enter a product name.")

# 👤 CUSTOMER SEGMENTATION PAGE
if page == "📊 Segmentation":
    st.title("👤 Customer Segmentation")
    st.markdown("Enter Recency and Monetary values to predict the customer's segment.")

    recency = st.number_input("📅 Recency (days since last purchase):", min_value=0, step=1)
    monetary = st.number_input("💰 Monetary (total spend):", min_value=0.0, step=1.0)

    if st.button("Predict Segment"):
        input_data = np.array([[recency, monetary]])
        input_scaled = scaler.transform(input_data)
        cluster_id = kmeans.predict(input_scaled)[0]
        segment = segment_map.get(cluster_id, f"Cluster {cluster_id}")
        st.success(f"🧾 Predicted Segment: **{segment}**")
