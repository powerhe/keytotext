import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
from keytotext import pipeline

############
## Main page
############
st.write("# Code for Keywords to Text")

st.code(body='''keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags = 4,
    key='1')''',
        language="python")

maxtags = st.slider('Number of tags allowed?', 1, 10, 3, key='jfnkerrnfvikwqejn')

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=maxtags,
    key="aljnf")

st.write("### Results:")

##########
## sidebar
##########
st.sidebar.write("# Code for Keywords to Text sidebar")

st.sidebar.code(body='''keyword = st_tags_sidebar(
label='# Enter Keywords:',
text='Press enter to add more',
value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 
'eight', 'nine', 'three', 
'eleven', 'ten', 'four'],
maxtags = 4)''',
                language="python")

maxtags_sidebar = st.sidebar.slider('Number of tags allowed?', 1, 10, 3, key='ehikwegrjifbwreuk')

keyword = st_tags_sidebar(label='# Enter Keywords:',
                          text='Press enter to add more',
                          value=['Zero', 'One', 'Two'],
                          suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
                          maxtags=maxtags_sidebar,
                          key="afrfae")

nlp=pipeline("k2t")
if st.button('Text Generation'):
    out=nlp(keywords)
    st.write(out)
