import streamlit as st
import pandas as pd
dataframe = pd.read_csv('abalone.csv')
dataframe.drop(columns = 'Sex')
st.line_chart(dataframe)