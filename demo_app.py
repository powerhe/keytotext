import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
from keytotext import pipeline

############
## Main page
############
st.write("# Code for Keywords to Text")

#st.code(body='''keywords = st_tags(
#    label='# Enter Keywords:',
#    text='Press enter to add more',
#    value=['Zero', 'One', 'Two'],
#    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
#    maxtags = 4,
#    key='1')''',
#        language="python")

st.markdown("***Idea is to build a model which will take keywords as inputs and generate sentences as outputs.***")
        
st.sidebar.write("# Parameter Selection")
maxtags_sidebar = st.sidebar.slider('Number of tags allowed?', 1, 10, 3, key='ehikwegrjifbwreuk')
keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Summer', 'Shoes', 'Sports'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=maxtags_sidebar,
    key="aljnf")



##########
## sidebar
##########

# Add selectbox in streamlit
option = st.sidebar.selectbox(
     'Which model would you like to be selected?',
     ('k2t', 'k2t-base', 'mrm8488/t5-base-finetuned-common_gen'))

if st.button('Load Model'):
    nlp=pipeline(option)
    st.write("Load Successfully!")

if st.button('Generate Text'):
    out=nlp(keywords)
    st.write(out)

st.write("## Results:")
