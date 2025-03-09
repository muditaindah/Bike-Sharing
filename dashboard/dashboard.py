import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #d1d1d1;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #000000;
    }
    .stMarkdown {
        color: #d1d1d1;
    }

    /* Customize font for the sidebar and other text */
    .stSidebar {
        font-family: 'Arial', sans-serif;
        color: #d1d1d1;
    }

    /* Ensure the metrics text color is white */
    .stMetric {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="text-align: center; color: white;">Bike Sharing Dashboard</h1>
    """, unsafe_allow_html=True
)

def load_data():
    df = pd.read_csv("df_hour.csv")  
    df['dteday'] = pd.to_datetime(df['dteday']).dt.date
    return df

df = load_data()

total_rentals = df['cnt'].sum()
total_operation_days = df['dteday'].nunique()

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <h4 style="text-align: center; color: "#5DBAE8";">Total Rentals</h4>
        """, unsafe_allow_html=True
    )
    st.markdown(
        f'<h3 style="text-align: center; color: "#5DBAE8";">{total_rentals}</h3>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <h4 style="text-align: center; color: "#5DBAE8";">Total Operation Days</h4>
        """, unsafe_allow_html=True
    )
    st.markdown(
        f'<h3 style="text-align: center; color: "#5DBAE8";">{total_operation_days}</h3>',
        unsafe_allow_html=True
    )

df["year"] = pd.to_datetime(df["dteday"]).dt.year
df['month'] = pd.to_datetime(df['dteday']).dt.month
filtered_df_2011 = df[df["year"] == 2011]
filtered_df_2012 = df[df["year"] == 2012]

col1, col2 = st.columns(2)

# 2011 Donut Chart
with col1:
    total_registered_2011 = filtered_df_2011["registered"].sum()
    total_casual_2011 = filtered_df_2011["casual"].sum()
    labels_2011 = ["Registered", "Casual"]
    sizes_2011 = [total_registered_2011, total_casual_2011]
    colors_2011 = ["#4A90E2", "#50E3C2"]

    fig_2011, ax_2011 = plt.subplots(figsize=(6, 6))
    ax_2011.pie(
        sizes_2011,
        labels=labels_2011,
        autopct="%1.1f%%",
        colors=colors_2011,
        wedgeprops={"edgecolor": "black"},
        startangle=90
    )
    centre_circle_2011 = plt.Circle((0, 0), 0.70, fc="black")
    ax_2011.add_artist(centre_circle_2011)
    ax_2011.set_title("2011 - Registered vs Casual Users", color="white")
    fig_2011.patch.set_facecolor("black")
    ax_2011.set_facecolor("black")
    st.pyplot(fig_2011)

# 2012 Donut Chart
with col2:
    total_registered_2012 = filtered_df_2012["registered"].sum()
    total_casual_2012 = filtered_df_2012["casual"].sum()
    labels_2012 = ["Registered", "Casual"]
    sizes_2012 = [total_registered_2012, total_casual_2012]
    colors_2012 = ["#4A90E2", "#50E3C2"]

    fig_2012, ax_2012 = plt.subplots(figsize=(6, 6))
    ax_2012.pie(
        sizes_2012,
        labels=labels_2012,
        autopct="%1.1f%%",
        colors=colors_2012,
        wedgeprops={"edgecolor": "black"},
        startangle=90
    )
    centre_circle_2012 = plt.Circle((0, 0), 0.70, fc="black")
    ax_2012.add_artist(centre_circle_2012)
    ax_2012.set_title("2012 - Registered vs Casual Users", color="white")
    fig_2012.patch.set_facecolor("black")
    ax_2012.set_facecolor("black")
    st.pyplot(fig_2012)

# Sidebar
st.sidebar.header("Customize based on your needs")
selected_date = st.sidebar.date_input("Choose a date", df['dteday'].min())

# Filter Data
filtered_data = df[df['dteday'] == selected_date]

if not filtered_data.empty:
    fig, ax = plt.subplots()
    ax.plot(
        filtered_data['hr'], 
        filtered_data['cnt'], 
        color='#4A90E2', marker='o', linestyle='-', linewidth=2
    )
    ax.set_title(f"Bike Rentals on {selected_date}", color="white")
    ax.set_xlabel("Hour of Day", color="white")
    ax.set_ylabel("Total Rentals", color="white")
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.tick_params(axis='both', colors="white")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    st.pyplot(fig)
else:
    st.write("No data available for the selected date.")


col1, col2 = st.columns(2)

with col1:
    monthly_rentals_2011 = filtered_df_2011.groupby('month')['cnt'].sum()
    fig_2011_rentals, ax_2011_rentals = plt.subplots(figsize=(6, 4))
    ax_2011_rentals.bar(monthly_rentals_2011.index, monthly_rentals_2011.values, color='#5DBAE8')
    ax_2011_rentals.set_title("Total Rents in 2011", color="white")
    ax_2011_rentals.set_xlabel("Month", color="white")
    ax_2011_rentals.set_ylabel("Total Rentals", color="white")
    ax_2011_rentals.grid(True, linestyle='--', alpha=0.4)
    ax_2011_rentals.tick_params(axis='both', colors="white")
    fig_2011_rentals.patch.set_facecolor("black")
    ax_2011_rentals.set_facecolor("black")
    st.pyplot(fig_2011_rentals)

with col2:
    monthly_rentals_2012 = filtered_df_2012.groupby('month')['cnt'].sum()
    fig_2012_rentals, ax_2012_rentals = plt.subplots(figsize=(6, 4))
    ax_2012_rentals.bar(monthly_rentals_2012.index, monthly_rentals_2012.values, color='#82D1F1')
    ax_2012_rentals.set_title("Total rents in 2012", color="white")
    ax_2012_rentals.set_xlabel("Month", color="white")
    ax_2012_rentals.set_ylabel("Total Rentals", color="white")
    ax_2012_rentals.grid(True, linestyle='--', alpha=0.4)
    ax_2012_rentals.tick_params(axis='both', colors="white")
    fig_2012_rentals.patch.set_facecolor("black")
    ax_2012_rentals.set_facecolor("black")
    st.pyplot(fig_2012_rentals)

df['hour'] = pd.to_datetime(df['hr'], format='%H').dt.hour

st.markdown(
    """
    <h2 style="text-align: center; color: white;">Clustering User Behavior</h2>
    """, unsafe_allow_html=True
)

# Classify users based on hour of day
def classify_users(df):
    conditions = [
        (df['hour'] >= 19),  # Night Users
        (df['hour'] >= 0) & (df['hour'] <= 5),  # Early Morning Users
        ((df['hour'] >= 6) & (df['hour'] <= 9)) | ((df['hour'] >= 16) & (df['hour'] <= 19)),  # Peak Hour Users
        (df['hour'] >= 10) & (df['hour'] <= 15)  # Noon Riders
    ]
    labels = ['Night Users', 'Early Morning', 'Peak Hour', 'Noon Riders']
    df['user_category'] = np.select(conditions, labels, default='Other')
    return df

df = classify_users(df)

hourly_category_rentals = df.groupby(['hour', 'user_category'])['cnt'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
blue_palette = sns.color_palette("Blues", 4)

sns.barplot(data=hourly_category_rentals, x='hour', y='cnt', hue='user_category', ax=ax, palette=blue_palette)
ax.set_xlabel("Hour of Day", color="white")
ax.set_ylabel("Total Rentals", color="white")
ax.tick_params(axis='both', colors="white")
ax.set_xticks(range(0, 24))
ax.set_xticklabels(range(0, 24))
ax.grid(True, linestyle='--', alpha=0.4)
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

st.pyplot(fig)
