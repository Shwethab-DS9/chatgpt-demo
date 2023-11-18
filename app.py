import pandas as pd
import streamlit as st
from chatGPT import gpt_helper

def main():
    st.title("Data Extraction Tool")

    col1, col2=st.columns([3,2])

    financial_data_df=pd.DataFrame(
        {
            "measure":["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
            "values":["", "", "", "", ""]
        }
    )

    with col1:
        news_article=st.text_area(
            "Paste your financial news article",height=300
        )
        if st.button("Extract"):
            financial_data_df= gpt_helper.extract_fin_data(news_article)
    
    with col2:
        st.markdown(
             "<br/>" *5, unsafe_allow_html= True
        )
        display_data(financial_data_df)
    
def display_data(df):
    st.dataframe(
        df,
        column_config={
            "measure":st.column_config.Column(width=150),
            "value":st.column_config.Column(width=150),
        },
        hide_index=True

    )
    
if __name__ == "__main__" :
    main()
       