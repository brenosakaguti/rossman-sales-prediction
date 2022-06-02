import streamlit as st
import pandas as pd
import altair as alt

data = pd.read_csv("computed_data.csv")
data["Date"] = data["Date"].astype("datetime64")

st.title("Rossmann Sales Prediction")
store_number = st.selectbox("Select store number:", data["Store"].unique())

filtered_data = data[data["Store"] == store_number]

sum = int(filtered_data["Sales"].sum())
st.subheader("The store " + str(store_number) + " will sell " + str(sum) + " units in the time period")

lines = alt.Chart(filtered_data).mark_line(tooltip=True).encode(x="Date", y="Sales")
st.altair_chart(lines, use_container_width=True)