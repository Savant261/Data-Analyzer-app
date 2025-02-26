import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title='Personal DA Portal',
    page_icon='📊'
)

st.title(':rainbow[Data Analytics Portal]')
st.subheader(':gray[Explore Data with ease.]', divider = 'rainbow')

file = st.file_uploader('Drop csv or excel file', type = ['csv','xlsx'])
if(file!=None):
    if(file.name.endswith('csv')):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    st.dataframe(df)
    st.info("File is successfully uploaded!!")

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
            fig, ax = plt.subplots()
            ax.bar(result[column],result['count'],color='lightblue',edgecolor='black')
            ax.set_xlabel(column, fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            ax.set_title(f'Top {toprows} counts of {column}',fontsize=15)
            plt.xticks(rotation=90)

            ax.set_facecolor('black')
            fig.patch.set_facecolor('black')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color('white')
            ax.spines['bottom'].set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.yaxis.label.set_color('white')
            ax.xaxis.label.set_color('white')
            ax.title.set_color('white') 
            st.pyplot(fig)

            #line plot  
            fig1, ax1 = plt.subplots()
            ax.plot(result[column],result['count'],color='white',marker='o',ls='-',lw=2)
            ax.set_xlabel(column, fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            ax.set_title(f'Line Chart of {column}', fontsize=15)
            plt.xticks(rotation=0)

            ax.set_facecolor('black')  # Dark background for the plot
            fig.patch.set_facecolor('black')  # Dark background for the figure
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color('white')
            ax.spines['bottom'].set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.yaxis.label.set_color('white')
            ax.xaxis.label.set_color('white')
            ax.title.set_color('white')

            st.pyplot(fig)

    st.subheader(':rainbow[Groupby : Simplify your data analysis]', divider='rainbow')
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
            
            
    if graphs == 'line' or graphs == 'bar' or graphs == 'scatter':
        x_axis = st.selectbox('Choose X axis', options=list(result.columns))
        y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
        color = st.selectbox('Color Information', options=[None] + list(result.columns))

    if graphs == 'line':
        fig, ax = plt.subplots()
        ax.plot(result[x_axis], result[y_axis], marker='o', label=f'{x_axis} vs {y_axis}', color='blue')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'{y_axis} by {x_axis} (Line Chart)')
        ax.legend()
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif graphs == 'bar':
        fig, ax = plt.subplots()
        ax.bar(result[x_axis], result[y_axis], color='skyblue')
        # for i, v in enumerate(result[y_axis]):
        #     ax.text(i, v + 0.2, str(v), ha='center')  # Adding count text
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'{y_axis} by {x_axis} (Bar Chart)')
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif graphs == 'scatter':
        fig, ax = plt.subplots()
        size = st.selectbox('Size Column', options=[None] + list(result.columns))
        ax.scatter(result[x_axis], result[y_axis], c='blue', s=result[size] * 10 if size else 50)
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'{y_axis} by {x_axis} (Scatter Plot)')
        plt.xticks(rotation=90)
        st.pyplot(fig)

    







        
        



