import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Zomato Dashboard", layout="wide")

st.title("🍽️ Zomato Data Analysis Dashboard")

# Upload Dataset
uploaded_file = st.file_uploader("D:\ADITI RAJESH NAIR\DATA SCIENCE\ZOMATO DATA ANALYSIS\Zomato data .csv", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Create 3 columns so graphs appear side-by-side
    col1, col2, col3 = st.columns(3)

    # ==========================
    # 1️⃣ BAR GRAPH
    # ==========================
    if "listed_in(type)" in data.columns and "votes" in data.columns:
        with col1:
            st.subheader("📊 Votes by Type")

            grouped_data = data.groupby("listed_in(type)")["votes"].sum()

            fig1, ax1 = plt.subplots(figsize=(4, 3))  # smaller size
            ax1.bar(grouped_data.index, grouped_data.values)
            ax1.set_xticklabels(grouped_data.index, rotation=45, fontsize=6)
            ax1.set_title("Total Votes", fontsize=10)
            ax1.tick_params(axis='y', labelsize=6)

            st.pyplot(fig1)

    # ==========================
    # 2️⃣ LINE GRAPH
    # ==========================
    if "rate" in data.columns:
        with col2:
            st.subheader("📈 Rating Trend")

            rating_counts = data["rate"].value_counts().sort_index()

            fig2, ax2 = plt.subplots(figsize=(4, 3))
            ax2.plot(rating_counts.index, rating_counts.values)
            ax2.set_title("Rating Distribution", fontsize=10)
            ax2.tick_params(axis='both', labelsize=6)

            st.pyplot(fig2)

    # ==========================
    # 3️⃣ PIE CHART
    # ==========================
    if "online_order" in data.columns:
        with col3:
            st.subheader("🥧 Online Orders")

            order_counts = data["online_order"].value_counts()

            fig3, ax3 = plt.subplots(figsize=(4, 3))
            ax3.pie(order_counts.values, labels=order_counts.index,
                    autopct="%1.1f%%", textprops={'fontsize': 6})
            ax3.set_title("Order Distribution", fontsize=10)

            st.pyplot(fig3)

else:
    st.warning("Please upload a CSV file to continue.")
