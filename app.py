import pdb
import streamlit as st
import pandas as pd

data = pd.read_csv('test.csv')

st.set_page_config(
    page_title="DISC 결과 계산기",
    page_icon="📃"
)


st.title('DISC 결과 계산기')
st.caption('written by Jung Su-In')
st.divider()


button = st.button('결과 보기')

col1, col2, = st.columns(2)


with col1 :
    with st.container(border=True) :
        st.subheader('D')
        D = st.slider("D", value=10, min_value = 0, max_value = 64, label_visibility = 'hidden')
        D_T_score = data.loc[data['D'] == D, 'T'].values[0]

        if button : 
            st.subheader(f'{D_T_score}점')

with col2 :
    with st.container(border=True) :
        st.subheader('I')
        I = st.slider("I", value=10, min_value = 0, max_value = 64, label_visibility = 'hidden')
        I_T_score = data.loc[data['I'] == I, 'T'].values[0]
        
        
        if button :
            st.subheader(f'{I_T_score}점')

col3, col4 = st.columns(2)

with col3 :

    with st.container(border=True) :
        st.subheader('S')
        S = st.slider("S", value=10, min_value = 0, max_value = 64, label_visibility = 'hidden')
        S_T_score = data.loc[data['S'] == S, 'T'].values[0]
            
        if button : 
            st.subheader(f'{S_T_score}점')


with col4 :
    with st.container(border=True) :
        st.subheader('C')
        C = st.slider("C", value=10, min_value = 0, max_value = 64, label_visibility = 'hidden')
        C_T_score = data.loc[data['C'] == C, 'T'].values[0]

        if button:
            st.subheader(f'{C_T_score}점')