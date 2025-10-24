import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import streamlit as st

#% DATA LOADING PHASE
Garment_worker = pd.read_csv('Dataset/garments_worker_productivity.csv', sep=',')

#% PROCESSING AND ISOLATION PHASE OF THE FINAL DATASET
# Unnecessary columns are removed.
Garment_worker.drop(['quarter', 'team', 'idle_time', 'idle_men', 'no_of_style_change'], axis=1, inplace=True)
# Duplicates are removed
Garment_worker.drop_duplicates(inplace=True)
# Columns with missing values are removed
Garment_worker.drop(['wip'], axis=1, inplace=True)
# Only values where actual productivity is less than or equal to 1 will be taken.
Garment_worker = Garment_worker[Garment_worker['actual_productivity'] <= 1]
# Only values where targeted productivity is greater than 0.1 and overtime is less than 25000 will be taken.
Garment_worker = Garment_worker[(Garment_worker['targeted_productivity'] > 0.1) & (Garment_worker['over_time'] < 25000)]
# The labels 'finishing ' are replaced with 'finishing' in the 'department' column
Garment_worker.loc[Garment_worker['department'] == 'finishing ', 'department'] = 'finishing'
# The date column format is converted to datetime.
Garment_worker['date'] = pd.to_datetime(Garment_worker['date'])


# Page configuration
st.set_page_config(layout="wide")
st.title('Garment Workers Analysis Dashboard')

# Sidebar for variable and date selection
st.sidebar.header('Chart Settings')
variable = st.sidebar.selectbox('Select the variable to display:', options=['targeted_productivity', 'smv', 'over_time', 'incentive', 'no_of_workers', 'actual_productivity'])
start_date = st.sidebar.date_input('Start date:', value=Garment_worker['date'].min().date())
end_date = st.sidebar.date_input('End date:', value=Garment_worker['date'].max().date())

# The column is converted to a 'date' format to compare with the entered range
dates = Garment_worker['date'].dt.date

# Filter the DataFrame for the desired date range
mask = (dates >= start_date) & (dates <= end_date)
filtered_df = Garment_worker.loc[mask]

st.header('Description')
st.subheader('Visualization dashboard consisting of some graphs that allow observing behaviors and trends of some variables that influence employee productivity. It includes:\n1. Productivity by day of the week\n2. Productivity by date\n3. Productivity by goal\n4. Productivity by department.')

# VARIABLE TO DISPLAY 0: User's choice:
st.subheader(f'Graph of "{variable}". Chosen by the user')

st.scatter_chart(data = filtered_df, x = 'date', y = variable)

# VARIABLE TO DISPLAY 1: Productivity by day of the week
st.subheader('Productivity by day of the week')
plot = sn.barplot(
    x="day", 
    y="actual_productivity", 
    data=Garment_worker, 
    estimator='mean', 
    errorbar=None,
)

plot.set_title('Actual Productivity vs. Day of the week')
plot.grid()


st.pyplot(plot.get_figure())

# VARIABLE TO DISPLAY 2: Productivity by date
st.subheader('Productivity by date')
fig, ax = plt.subplots()

ax.bar(Garment_worker['date'], Garment_worker['actual_productivity'])
ax.set_title('Productivity vs. Date')
ax.set_xlabel('Date')
ax.set_ylabel('Productivity')
ax.grid()

st.pyplot(fig)

# 2.5
# The days of each month are grouped with the corresponding actual productivity and the average is obtained.
most_prod_day = Garment_worker.groupby(Garment_worker['date'].dt.day)['actual_productivity'].mean().reset_index()
most_prod_day.sort_values(by = 'actual_productivity', ascending=False, inplace=True)
less_prod_day = most_prod_day.sort_values(by = 'actual_productivity', ascending = True)
# The days are converted to categorical so that when graphing, it is not reorganized by higher or lower numerical value of the day.
most_prod_day['date'] = most_prod_day['date'].astype(str)
less_prod_day['date'] = less_prod_day['date'].astype(str)

plot = sn.barplot(
    x = 'date',
    y = 'actual_productivity',
    data=most_prod_day[0:5],  
    errorbar=None,
)

ax.set_title('Top 5 days with highest productivity')

st.pyplot(plot.get_figure())

plot = sn.barplot(
    x = 'date',
    y = 'actual_productivity',
    data=less_prod_day[0:5],  
    errorbar=None, 
)

ax.set_title('Top 5 days with lowest productivity')
st.pyplot(plot.get_figure())

# VARIABLE TO DISPLAY 3: Actual productivity vs. Targeted productivity
st.subheader('Productivity by goal')
# The targeted productivity is grouped with the actual productivity and the average is obtained.
tar_x_act = Garment_worker.groupby(Garment_worker['targeted_productivity'])['actual_productivity'].mean().reset_index()

#plot = sn.scatterplot(data = tar_x_act, x = 'targeted_productivity', y = 'actual_productivity')

st.scatter_chart(data = tar_x_act, x = 'targeted_productivity', y = 'actual_productivity')

# VARIABLE TO DISPLAY 4: Actual productivity vs. Department
st.subheader('Productivity by department')
plot = sn.barplot(
    x = 'department',
    y = 'actual_productivity',
    data=Garment_worker,
    estimator='mean',
    errorbar=None,
)
ax.set_title('Actual Productivity vs. Department')
st.pyplot(plot.get_figure())

#Execute in the terminal: python -m streamlit run "Streamlit Dashboard/Dashboard.py".