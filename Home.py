import streamlit as st
import pandas as pd
import numpy as np


st.markdown("""
<style>

.e1fb0mya1 css-fblp2m ex0cdmw0{
visibility: hidden;
}
.css-1lsmgbg{
visibility: hidden;
}

</style>
""",unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/EDA/EDA_1.png", output_format="auto")
with col2:
    st.title("DataVue")
    st.caption("Few Clicks to know your data")

st.write("___")
data = st.file_uploader("Please upload the data in the 'csv' Format.", type="csv")

if data is not None:
    df = pd.read_csv(data)
    if 'Unnamed: 0' in df.columns:
        df = df.drop("Unnamed: 0", axis=1)

    st.write("Upload Successful...")
    st.write("---")

# --------------------------------------------------------------------Functional Options--------------------------------------------------------------------------------------

    option = st.selectbox(
        'Select the Work among the following',
        ('', 'Numerical Analysis', 'Data Visualization', 'ML and Predictions'))
    #st.write("---")

# --------------------------------------------------------------------Numerical Analysis--------------------------------------------------------------------------------------

    if option == 'Numerical Analysis':
        st.write("In the Numerical Analysis, Following are the functionalities that are available...")

        head_check = st.checkbox("View my Dataset")           #---------------------------------------------------------------------------------------------
        if head_check:
            st.write(df.head())
            st.write("---")

        shape_check = st.checkbox("Shape of the Dataset")     #------------------------------------------------------------------------------------------------
        if shape_check:
            st.write("Number of Rows in the Dataset: ", df.shape[0])
            st.write("Number of Columns in the Dataset: ", df.shape[1])
            st.write("---")

        Colnames_check = st.checkbox("Column Names from DataSet")              #-------------------------------------------------------------------------------
        if Colnames_check:
            st.write(df.columns)
            st.write("---")

        catnum_check = st.checkbox("List out the categorical and numerical Columns separately")
        if catnum_check:
            cat_features = {}
            num_features = {}
            for name, column in df.iteritems():
                unique_count = column.unique().shape[0]
                total_count = column.shape[0]
                if unique_count / total_count < 0.05:
                    cat_features[name] = 'category'
                else:
                    num_features[name] = 'numerical'
            col1, col2 = st.columns(2)
            with col1:
                st.write("Numerical Features", pd.DataFrame(num_features.keys()))
            with col2:
                st.write("Categorical Features", pd.DataFrame(cat_features.keys()))
            st.write('---')

        describe_check = st.checkbox("6 point summary of the Numerical Columns")              #-------------------------------------------------------------------------------
        if describe_check:
            st.write(df.describe())
            st.write("---")

        missval_check = st.checkbox("Missing values with respect to each column")
        if missval_check:
            st.write(df.isnull().sum())
            st.write('---')

        nunique_check = st.checkbox("nunique for categorical columns")                      #------------------------------------------------------------------------------------------------
        if nunique_check:
            st.write(df.nunique())
            st.write("---")

        unique_check = st.checkbox("Unique Values")                 #------------------------------------------------------------------------------------------------
        if unique_check:
            st.write(df.unique())
            st.write("---")

        valuecounts_check = st.checkbox("Value Counts for the Categorical Columns in the Dataset")             #--------------------------------------------------------------------------------------------------
        if valuecounts_check:
            st.write(df.describe())
            st.write("---")


#----------------------------------------------------------------------------------------------Data Visualization-----------------------------------------------------------
    if option == 'Data Visualization':

        col1, col2 = st.columns(2)
        with col1:
            plotchoice = st.radio(
                'Following are different varieties of categories that are available in plots',
                ('Relational plots', 'Distribution plots', 'Categorical plots', 'Regression plots', 'Matrix plots'))
        with col2:
            if plotchoice == 'Relational plots':
                relplots_check = st.radio(
                    "Available Relational plots are...",
                    ('', 'relplot', 'scatterplot', 'lineplot'))
                if relplots_check == 'relplot':
                    st.write("'relplot'")
                if relplots_check == 'scatterplot':
                    st.write("'scatterplot'")
                if relplots_check == 'lineplot':
                    st.write("'lineplot'")

            if plotchoice == 'Distribution plots':
                distplots_check = st.radio(
                    "Available Distribution plots are...",
                    ('', 'distplot', 'histplot', 'kdeplot', 'ecdfplot', 'rugplot'))
                if distplots_check == 'distplot':
                    st.write("'distplot'")
                if distplots_check == 'histplot':
                    st.write("'histplot'")
                if distplots_check == 'kdeplot':
                    st.write("'kdeplot'")
                if distplots_check == 'ecdfplot':
                    st.write("'ecdfplot'")
                if distplots_check == 'rugplot':
                    st.write("'rugplot'")

            if plotchoice == 'Categorical plots':
                cateplots_check = st.radio(
                    "Available Categorical plots are...",
                    ('', 'catplot', 'stripplot', 'swarmplot', 'boxplot', 'violinplot', 'boxenplot', 'pointplot', 'barplot', 'countplot'))
                if cateplots_check == 'catplot':
                    st.write("'catplot'")
                if cateplots_check == 'stripplot':
                    st.write("'stripplot'")
                if cateplots_check == 'swarmplot':
                    st.write("'swarmplot'")
                if cateplots_check == 'boxplot':
                    st.write("'boxplot'")
                if cateplots_check == 'violinplot':
                    st.write("'violinplot'")
                if cateplots_check == 'boxenplot':
                    st.write("'boxenplot'")
                if cateplots_check == 'pointplot':
                    st.write("'pointplot'")
                if cateplots_check == 'barplot':
                    st.write("'barplot'")
                if cateplots_check == 'countplot':
                    st.write("'countplot'")

            if plotchoice == 'Regression plots':
                regreplots_check = st.radio(
                    "Available Regression plots are...",
                    ('', 'lmplot', 'regplot', 'residplot'))
                if regreplots_check == 'lmplot':
                    st.write("'lmplot'")
                if regreplots_check == 'regplot':
                    st.write("'regplot'")
                if regreplots_check == 'residplot':
                    st.write("'residplot'")

            if plotchoice == 'Matrix plots':
                matriplots_check = st.radio(
                    "Available Matrix plots are...",
                    ('', 'heatmap', 'cluster map'))
                if matriplots_check == 'heatmap':
                    st.write("'heatmap'")
                if matriplots_check == 'clustermap':
                    st.write("'clustermap'")

    st.write("---")


# ----------------------------------------------------------------------------------------------ML and Predictions-----------------------------------------------------------
    if option == 'ML and Predictions':
        st.write('You selected:', option)









