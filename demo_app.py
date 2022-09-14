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

st.text('Idea is to build a model which will take keywords as inputs and generate sentences as outputs. \n
        Potential use case can include: \n
        - Marketing \n
        - Search Engine Optimization \n
        - Topic generation etc. \n
        - Fine tuning of topic modeling models \n')
        
maxtags_sidebar = st.sidebar.slider('Number of tags allowed?', 1, 10, 3, key='ehikwegrjifbwreuk')
keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=maxtags_sidebar,
    key="aljnf")

st.write("## Results:")

##########
## sidebar
##########
st.sidebar.write("# Parameter Selection")

# Add selectbox in streamlit
option = st.selectbox(
     'Which model would you like to be selected?',
     ('k2t', 'k2t-base', 'mrm8488/t5-base-finetuned-common_gen'))

if st.button('Text Generation'):
    nlp=pipeline(option)
    out=nlp(keywords)
    st.write(out)
