from sklearn import preprocessing
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

filename = 'final_model.sav'
load_model = pickle.load(open(filename, 'rb'))
df = pd.read_csv("Clustered_Data.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Market Segmentation")

with st.form("my_form"):
    Store_Area=st.number_input(label='Store_Area',step=0.001,format="%.6f")
    Items_Available=st.number_input(label='Items_Available',step=0.001,format="%.6f")
    Daily_Customer_Count=st.number_input(label='Daily_Customer_Count',step=0.01,format="%.2f")
    Store_Sales=st.number_input(label='Store_Sales',step=0.01,format="%.2f")


    data=[[Store_Area,Items_Available,Daily_Customer_Count,Store_Sales]]

    submitted = st.form_submit_button("Submit")

if submitted:
    clust=load_model.predict(data)[0]
    print('Data Belongs to Cluster',clust)

    cluster_centers=df[df['clusters']==clust]
    plt.rcParams["figure.figsize"] = (20,3)
    for c in  cluster_centers.drop(['clusters'],axis=1):
        fig, ax = plt.subplots()
        grid= sns.FacetGrid(cluster_centers, col='clusters')
        grid= grid.map(plt.hist, c)
        plt.show()
        st.pyplot(figsize=(5, 5))