import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title='Personal Data Analyzer',
    page_icon='📊'
)

st.title(':rainbow[Data Analysis With Savant]')
st.subheader(':gray[Explore Data with ease.]', divider = 'rainbow')

#FILE UPLOAD

file = st.file_uploader('Drop csv or excel file', type = ['csv','xlsx'])
if(file!=None):
    if(file.name.endswith('csv')):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    st.dataframe(df)
    st.info("File is successfully uploaded!!")


#BASIC INFORMATION
    st.subheader(':rainbow[Basic Information of Dataset]', divider='rainbow')
    tab1, tab2, tab3, tab4 = st.tabs(['Summary','Top and Bottom Rows ','Data Types','Columns'])
    with tab1:
        st.write(f'There are {df.shape[0]} rows and {df.shape[1]} columns in the dataset')
        st.subheader(':gray[Statistics of the Dataset]', divider='rainbow')
        st.dataframe(df.describe())
        
    with tab2:
        st.subheader(':gray[Top Rows]')
        toprows = st.slider('Number of rows you want:', 1, df.shape[0],key='topslide')
        st.dataframe(df.head(toprows))
        st.subheader(':gray[Bottom Rows]')
        bottomrows = st.slider('Number of bottom rows you want', 1, df.shape[1], key='bottomslide')
        st.dataframe(df.tail(bottomrows))
        
    with tab3:
        st.dataframe(df.dtypes)
    with tab4:
        st.dataframe(list(df.columns))


#COUNTING VALUES
    
    st.subheader(":rainbow[Columns Values to Count]", divider='rainbow')
    with st.expander('Value Count'):
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Select Column Name:', options=list(df.columns))
        with col2:
            toprows = st.number_input('Top Rows', min_value = 1, step=1)

        count = st.button('Count')
        if (count==True):
            result = df[column].value_counts().reset_index().head(toprows)
            # result.columns = [column, 'count']
            st.dataframe(result)
            st.subheader('Visualization: ', divider='gray')
            fig = px.bar(data_frame=result, x=column, y='count',text='count',template='plotly_white')
            st.plotly_chart(fig)

            fig = px.line(data_frame=result, x=column, y='count', text='count',template='plotly_white')
            st.plotly_chart(fig)

            fig = px.pie(data_frame=result,names=column, values='count')
            st.plotly_chart(fig)

#MISSING VALUES HANDLING

    st.header(':rainbow[Missing Values Handler]', divider='rainbow')

    st.subheader(":gray[Find Missing Values]",divider='gray')

    if st.button("Find Missing Values"):
        missing_values = df.isnull().sum()
    
        for col in df.columns:
            if missing_values[col] > 0:
                st.markdown(f"<span style='color:red'>{col}: {missing_values[col]} missing values (Data type: {df[col].dtype})</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color:green'>{col}: No missing values (Data type: {df[col].dtype})</span>", unsafe_allow_html=True)

    
    st.subheader(":gray[Remove Missing Values]",divider='gray')

    if st.button("Remove Missing Values"):
        cleaned_df = df.dropna()

    
        remaining_missing_values = cleaned_df.isnull().sum()

        st.write("Missing values have been removed. Here are the columns with their missing values count after removal:")

    
        for col in cleaned_df.columns:
            st.write(f"{col}: {remaining_missing_values[col]} missing values")

#MANIPULATING DATA USING GROUPBY AND VISUALIZATIONS


    st.header(':rainbow[Groupby : Simplify your data analysis]', divider='rainbow')
    st.write('The groupby lets you summarize data by specific categories and groups')

            
    with st.expander('Group By your columns'):
        col1, col2, col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect('Choose your column to groupby', options=list(df.columns))
        with col2:
            operation_col = st.selectbox('Choose column for operation', options=list(df.columns))
        with col3:
            operation = st.selectbox('Choose operation', options=['sum', 'max', 'min', 'mean', 'median', 'count'])
                
        if groupby_cols:
            result = df.groupby(groupby_cols).agg(
                newcol=(operation_col, operation)
            ).reset_index()
            
        st.dataframe(result)
            
    st.subheader(':gray[Data Visualization]', divider='gray')
    graphs = st.selectbox('Choose your graphs', options=['line', 'bar', 'scatter', 'pie', 'sunburst'])
            
    if graphs == 'line':
            x_axis = st.selectbox('Choose X axis', options=list(result.columns))
            y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            fig = px.line(data_frame=result, x=x_axis, y=y_axis, color=color, markers='o')
            st.plotly_chart(fig)        

    elif graphs == 'bar':
            x_axis = st.selectbox('Choose X axis', options=list(result.columns))
            y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            facet_col = st.selectbox('Column Information', options=[None] + list(result.columns))
            fig = px.bar(data_frame=result, x=x_axis, y=y_axis, color=color, facet_col=facet_col, barmode='group')
            st.plotly_chart(fig)
    

    elif graphs == 'scatter':
            x_axis = st.selectbox('Choose X axis', options=list(result.columns))
            y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
            color = st.selectbox('Color Information', options=[None] + list(result.columns))
            size = st.selectbox('Size Column', options=[None] + list(result.columns))
            fig = px.scatter(data_frame=result, x=x_axis, y=y_axis, color=color, size=size)
            st.plotly_chart(fig)
    elif graphs == 'pie':
            values = st.selectbox('Choose Numerical Values', options=list(result.columns))
            names = st.selectbox('Choose labels', options=list(result.columns))
            fig = px.pie(data_frame=result, values=values, names=names)
            st.plotly_chart(fig)
    elif graphs == 'sunburst':
            path = st.multiselect('Choose your Path', options=list(result.columns))
            fig = px.sunburst(data_frame=result, path=path, values='newcol')
            st.plotly_chart(fig)

    
#INCONSISTENCY CHECKING USING HEATMAPS AND BOXPLOTS

#WILL WORK ONLY ON DATASETS WITH NUMERIC DATATYPES

    

    st.header(':rainbow[Inconsistency Checker]', divider='rainbow')
    

    st.subheader(":gray[Check for High Collinearity]", divider='gray')

    if st.button("Check Collinearity"):

        corr = df.corr()

        fig = px.imshow(corr, color_continuous_scale='RdBu', text_auto=True, aspect="auto")
        fig.update_layout(title="Correlation Heatmap", coloraxis_showscale=True)
        st.plotly_chart(fig)


        high_corr_pairs = []
        threshold = 0.8
        for i in range(len(corr.columns)):
            for j in range(i):
                if abs(corr.iloc[i, j]) > threshold:
                    high_corr_pairs.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))

        if high_corr_pairs:
            st.write("Columns with high collinearity (>|0.8|):")
            for col1, col2, corr_value in high_corr_pairs:
                st.markdown(
                    f"<span style='color:red;background-color:rgba(48,49,45,0.5);padding:5px;font-weight:bold;font-size:18px;'>{col1} and {col2}: {corr_value:.2f}</span>",unsafe_allow_html=True)
            st.write("**Handling Suggestions**: You can handle high collinearity by removing one of the correlated variables or combining them if it makes sense for your analysis.")
        else:
            st.markdown("<span style='color:lightgreen;background-color:rgba(48,49,45,0.5);padding:5px;font-weight:bold;font-size:18px;'>No high collinearity detected!</span>", unsafe_allow_html=True)



    st.subheader(":gray[Check for Outliers]", divider='gray')

    if st.button("Check Outliers"):
        st.write("Boxplots for Outlier Detection:")

    
        for col in df.select_dtypes(include=[np.number]).columns:
            st.write(f"Boxplot for {col}:")
        
        
            fig = go.Figure()
            fig.add_trace(go.Box(y=df[col], name=col, boxpoints='suspectedoutliers'))
            fig.update_layout(title=f"Boxplot for {col}")
            st.plotly_chart(fig)

        
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()

        
            if outliers > 0:
                st.markdown(
                    f"<span style='color:red;background-color:rgba(48, 45, 45, 0.5);padding:5px;font-weight:bold;font-size:18px;'>Outliers: {outliers}</span>",unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<span style='color:lightgreen;background-color:rgba(41, 39, 39, 0.5);padding:5px;font-weight:bold;font-size:18px;'>Outliers: {outliers}</span>",unsafe_allow_html=True)
    

    







        
        



