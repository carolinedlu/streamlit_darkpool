from typing import Any, Dict, List

import streamlit as st


# Page config
st.set_page_config(page_title="darkpool", layout="wide")

# Load config
config, instructions, readme = load_config(
    "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"
)

# Initialization
dates: Dict[Any, Any] = dict()
report: List[Dict[str, Any]] = []

# Info
with st.beta_expander("What is darkpool?", expanded=True):
    st.write(readme["app"]["app_intro"])
    st.write("")
st.write("")
st.sidebar.image(load_image("darkpool.png"), use_column_width=True)
#display_links(readme["links"]["repo"],readme["links"]["repo"])



st.sidebar.title("Configure your analysis")

# Select Dataset
with st.sidebar.beta_expander("Data", expanded=True):
    dataset = st.selectbox('Select your dataset for analysis',('Credit Card Fraud','Churn'))

# Column names - change to target variable
with st.sidebar.beta_expander("Columns", expanded=True):
    if dataset == 'Credit Card Fraud':   
        column = st.selectbox('Select your target outcome variable',('ISFRAUD','ISFLAGGEDFRAUD'))
    if dataset == 'Churn':   
        st.write("No dataset is available")

# Launch analysis
with st.sidebar.beta_expander("Boost", expanded=True):
#    st.write("Choose the data sets for your analysis:")
    analysis = st.radio ("Choose the data sets for your analysis:",('None','Own Set','BOOST'))
    if analysis == 'Own Set': 
        st.write('You selected ML analysis on your own data set only.')
    if analysis == 'BOOST': 
        st.write('You selected to boost your ML accuracy with data from the dark pool.')
        

# Visualizations        
 
st.header("1. Overview (visualization of data)")
st.write("")
st.header("2. Evaluation on Dataset")
st.subheader("Performance Metrics")
with st.beta_expander("More info on evaluation metrics",expanded=True):
    st.write(readme["plots"][ "metrics"])
st.write("")
st.header("3. Impact of components and regressors")
st.write("")





