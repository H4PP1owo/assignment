#HISTORY

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
st.write("👾        profile loading... H4PP1 : activities")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

# 레이아웃: 탭
st.header('Activities')
st.write('dreaming to become a great artist in her childhood, she seemed to have made plenty of artworks.')
st.write('as she grows, not only her personal work but also team projects are remarkable. Let\'s take a look of some of them.')

tab_1, tab_2, tab_3, tab_4 = st.tabs(['✎ᝰ','⬡','𓂉','𖠋𖠋𖠋'])
with tab_1:
    st.subheader('✎ᝰ illustrations')
    st.write('since drawing every time her time is left, and is an easiest way to enter the world of art')
    st.write('hard to pick the best piece to record here.')
    tab_1_1, tab_1_2, tab_1_3 = st.tabs(['𖠋','🐾','𓆤'])
    with tab_1_1:
        st.write('#### 𖠋 anime characters')
        img = Image.open('pages/anime1.jpg')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/anime2.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/anime3.png')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/anime4.png')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/anime5.png')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/anime6.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
    with tab_1_2:
        st.write('#### 🐾 animals')
        img = Image.open('pages/animal.png')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/animal1.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/animal2.jpg')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
    with tab_1_3:
        st.write('#### 𓆤 moth')
        img = Image.open('pages/moth1.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/moth2.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        st.write('one of H4PP1\'s favorite **original character(OC)** she made.')
with tab_2:
    st.subheader('⬡ 3D works')
    st.write('even a short period of adjusting the tool, she tried many things. can\'t wait for the whole works.')
    img = Image.open('pages/shot1.jpg')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('guess this is a trial step.')
    img = Image.open('pages/rendertestshot.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/rendertestshot1.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/trailer.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('**< A Little Fish\'s Dream >**, the one H4PP1 thinks masterpiece.')
    st.write('**WAIT till the whole movie uploads...**')
    st.write('[H4PP1] (https://www.youtube.com/@happi-owo)')
with tab_3:
    st.subheader('𓂉 other artworks')
    st.write('seems that those works are belong during the class, since there is some datas that H4PP1 hate abstract arts')
    st.write('but think quite nice to appreciate, would H4PP1 herself have loved her works she done?')
    img = Image.open('pages/other1.jpg')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('< Untitled >')
    st.write('')
    img = Image.open('pages/other2.PNG')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('< Untitled >')
    st.write('')
    img = Image.open('pages/p1.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('< How to explain DEATH to a Fish >')
    st.write('')
    img = Image.open('pages/p2.PNG')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('< Untitled >')
    st.write('')
    img = Image.open('pages/p3.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('< Memory >')
    st.write('silent, peaceful mood outstands in the whole works.')

with tab_4:
    st.subheader('𖠋𖠋𖠋 team project')
    st.write('since H4PP1 entered university, she kept participated in team projects held in her circle.')
    st.write('seems that she took charge of graphic parts, especially in UIs')
    st.write('')
    tab_4_1, tab_4_2, tab_4_3 = st.tabs(['𖠰','၊၊||၊','☾'])
    with tab_4_1:
        st.subheader('𖠰 my Tree House')
        img = Image.open('pages/타이틀ui배치설명.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/ui배치수정1.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/인벤토리 ui 수정본.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        st.write('she\'d done a hard work in the project I guess...')
    with tab_4_2:
        st.subheader('၊၊||၊ CITYSCAPE')
        img = Image.open('pages/ui가이드.png')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        img = Image.open('pages/ui가이드2수정.PNG')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        st.write('heard that it\'s her favorite project ever done.')
    with tab_4_3:
        st.subheader('☾ Save the Moon~')
        img = Image.open('pages/summary.gif')    # 이미지 파일 열기
        st.image(img, width=400)          # 이미지 출력
        st.write('quite fast work to finish graphics in 24 hours.')
