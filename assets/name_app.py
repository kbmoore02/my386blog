import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

st.title('Explore Name Trends')

selected_name = st.text_input('Type a name to search', placeholder='Enter a name')
selected_sex = st.selectbox('Select a gender',['Males','Females'])

sex = 'F'
if selected_sex=='Males':
    sex = 'M'

name_df = df[df['name']==selected_name]
sex_df = name_df[name_df['sex']==sex]
fig, x = plt.subplots()
x.plot(sex_df['year'],sex_df['n'])
plt.xlabel('Year')
plt.ylabel('')
plt.title(f'Name Trend for {selected_sex} named {selected_name} from 1910-2021')
st.pyplot(fig)