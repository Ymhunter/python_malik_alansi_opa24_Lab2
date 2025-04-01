import streamlit as st
import plotly.express as px
from read_data import read_data
import matplotlib.pyplot as plt

# Read data
df = read_data()

# --- Dashboard Components ---
st.markdown("# Skolverket")

# Description
st.markdown("This is a simple dashboard about statistics for the national tests in grade 9. The results from the education can be filtered in this dashboard.")

# KPIs
st.markdown("## KPIs in Sweden")

cols = st.columns(3)

years_filter = ["2018/19", "2019/20", "2020/21", "2021/22", "2022/23"]
df_filtered_years = df[df["Unnamed: 0"].isin(years_filter)]
df_filtered_years = df_filtered_years.rename(columns={"Unnamed: 0": "Year", "Totalt.2": "Total", "Flickor.2": "Girls", "Pojkar.2": "Boys"})
df_melted = df_filtered_years.melt(id_vars=["Year"], value_vars=["Total", "Girls", "Boys"], var_name="Category", value_name="Missing Grades")


fig = px.line(df_melted, x="Year", y="Missing Grades", color="Category", title="Missing Grades by Gender from 2018 to 2023")
st.plotly_chart(fig)  

plt.figure(figsize=(10, 5))
plt.plot(df_filtered_years["Year"], df_filtered_years["Total"], label="Total")
plt.plot(df_filtered_years["Year"], df_filtered_years["Girls"], label="Girls")
plt.plot(df_filtered_years["Year"], df_filtered_years["Boys"], label="Boys")
plt.xlabel("Year")
plt.ylabel("Missing Grades")
plt.title("Missing Grades by Gender from 2018 to 2023")
plt.legend()
plt.show()



years_filter = ["2018/19", "2019/20", "2020/21", "2021/22", "2022/23"]
df_filtered_years = df[df["Unnamed: 0"].isin(years_filter)]

df_filtered_years = df_filtered_years.rename(columns={"Unnamed: 0": "Year", "Totalt": "Total", "Flickor": "Girls", "Pojkar": "Boys"})

df_melted = df_filtered_years.melt(id_vars=["Year"], value_vars=["Total", "Girls", "Boys"], 
                                   var_name="Category", value_name="Merit Value")


figMerit = px.line(df_melted, x="Year", y="Merit Value", color="Category",
              title="Merit Value for 16 Subjects by Gender from 2018 to 2023")
st.plotly_chart(figMerit)


plt.figure(figsize=(10, 5))
plt.plot(df_filtered_years["Year"], df_filtered_years["Total"], label="Total")
plt.plot(df_filtered_years["Year"], df_filtered_years["Girls"], label="Girls")
plt.plot(df_filtered_years["Year"], df_filtered_years["Boys"], label="Boys")
plt.xlabel("Year")
plt.ylabel("Merit Value for 16 Subjects")
plt.title("Merit Value for 16 Subjects by Gender from 2018 to 2023")
plt.legend()
plt.show()



# Raw Data Table
st.markdown("## Raw Data")
st.dataframe(df)
