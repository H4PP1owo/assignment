#BUCKETLISTS

#library import
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(     # 페이지 설정
    page_title="Info LOADING...", # 페이지 Tab의 타이틀
    page_icon="🙃",     # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    initial_sidebar_state="expanded", # 사이드바 초기 상태: auto, collapsed, expanded
)

st.write("👾        access to the profile...")
st.write("👾        access approved")
st.write("👾        profile loading... H4PP1 : bucketlists_1year")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.header('Bucketlists')
st.write('these days H4PP1 looks interested in wide area, eager to study a lot for herself.')
st.write('by recording her conversation with others, and tracking her Internet usage, we found some clues of her bucketlists.')
st.write('found that we can separate them in short-term goals and long-term wishes.')

st.sidebar.header('check_progress')
st.sidebar.write('progress_checksheet_short')
st.sidebar.checkbox('⭑1')
st.sidebar.checkbox('⭑2')
st.sidebar.checkbox('⭑3')
st.sidebar.checkbox('⭑4')
st.sidebar.checkbox('⭑5')
st.sidebar.checkbox('⭑6')
st.sidebar.checkbox('⭑7')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('progress_checksheet_long')
st.sidebar.checkbox('✩1')
st.sidebar.checkbox('✩2')
st.sidebar.checkbox('✩3')
st.sidebar.checkbox('✩4')
st.sidebar.checkbox('✩5')
st.sidebar.checkbox('✩6')
st.sidebar.checkbox('✩7')



tab_1, tab_2 = st.tabs(['⭑.ᐟ','⁺˚⋆｡°✩₊'])
with tab_1:
    st.subheader('⭑.ᐟ short-term goals(1 year)')
    st.write('1. to perfectly finish the large game project I participate.')
    st.write('2. to finish uploading the whole movie of < A Little Fish\'s Dream > on youtube this year.')
    st.write('3. to upload another 3D animation movie.')
    st.write('4. to master C4D so make only time matters to make a work.')
    st.write('5. to study a whole book about C language at least once.')
    st.write('6. to participate at least 2 contest.')
    text = st.text_input('what\'s your short-term goals?') # 텍스트 입력은 입력된 값을 반환
    st.write(f'7: {text}')
with tab_2:
    st.subheader('⁺˚⋆｡°✩₊ long-term goals')
    st.write('1. to make a successful one-man developed game after resigning.')
    st.write('2. to enter a named game company.')
    st.write('3. to get many works with my ability of making arts.')
    st.write('4. to keep beautiful fish I want to see like L236sw pleco.')
    st.write('5. to live in an environment with balanced work and recess.')
    st.write('6. to travel far away for several month for a rest accessed with nobody.')
    text = st.text_input('what\'s your long-term wishes?') # 텍스트 입력은 입력된 값을 반환
    st.write(f'7: {text}')
    