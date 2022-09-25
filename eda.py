from os import P_WAIT
import pandas as pd 
import streamlit as st
import numpy as np
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp ka title
st.markdown(''' 
# **Exploratory Data Analysis web Application**
This app is developed by codanics channel called **EDA app**
''')

# how to upload a file from pc
with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset("titanic")
    st.sidebar.markdown("[Example CSV file]()")

# profiling report for pandas
if uploaded_file is not None:

    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for csv file')
    if st.button('Press to use example data'):
        # example daraset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),
                               columns=['age', 'banana', 'cat', 'dog', 'elefant'])
            return a
        pr = ProfileReport(df, explorative=True)
        df = load_data()
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)