#HOBBY

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
st.write("👾        profile loading... H4PP1 : hobby")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

# 레이아웃: 탭
st.header('Hobby')
st.write('found that she enjoys some hobbies daily life. recorded some meaningful activities during her leisure.')
st.write('Generally saying, she spends a lot of time sleeping or seeking for fun in SNS than those activities.')
st.write('Except for fish feeding, we found that she does that activities when she is in **a very good mood**.')
tab_1, tab_2, tab_3, tab_4 = st.tabs(['✎ᝰ', '𓆡', '𝄞', '𖤣𖥧𖡼'])  # 탭 인스턴스 생성. 4개의 탭을 생성

with tab_1:
    st.write('### ✎ᝰ digital artworking')
    st.write('H4PP1 loved to make arts since her childhood. after getting IPad as a gift, enjoyed making digital arts.')
    st.write('loved to draw anime characters when teenagers, after having pets tends to scribble fish.')
    st.write('here are some **scribbles** she\'ve done digital and physical both. neat art will be displayed in ACTIVITIES section.')
    img = Image.open('pages/veryYoung.jpg')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('**\* very valuable record here...** to get the scribbles in early childhood')
    img = Image.open('pages/animeScribble1.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/animeScribble2.PNG')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/animeScribble3.PNG')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/animeScribble4.PNG')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/recentscribble.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/bugScribble.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/creature.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    img = Image.open('pages/fishScribble.PNG')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('')
    st.write('recently after 3D design class, seems to fall in love with 3D graphics she tend to unlike.')
    img = Image.open('pages/3dscribble.png')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력

with tab_2:
    st.write('### 𓆡 fish feeding')

    st.write('got the information that she started to keep a tank since 2024.03.04. seemed that she had been interested in aquariums.')
    st.write('have details that she had kept fish in her childhood. had been more than 3 month as of today.(2024.06.21)')
    st.write('beneath this text is some photo history of her tank.')
    st.write('')
    img = Image.open('pages/initial.jpg')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('2024.03.27 07:06')
    st.write('')
    img = Image.open('pages/middle.jpg')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('2024.04.02 23:21')
    st.write('')
    img = Image.open('pages/recent.jpg')    # 이미지 파일 열기
    st.image(img, width=400)          # 이미지 출력
    st.write('2024.06.12 18:06')
    st.write('')

    st.write('#### the amount of fish every year')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    data = {'3': 5, '4': 10, '5': 12, '6': 19}
    st.line_chart(data)

    st.write('hardly got informations of her fish, also we have not certain informations of every types of fish she had kept.')
    st.write('only recorded the information which is **clear**, trying to get more informations.')
    st.write('think we need more informations of something looks like \'hillstream loach\' found in some photoes taken in initial stage.')

    tab_2_1, tab_2_2, tab_2_3 = st.tabs(['platy', 'guppy', 'gourami'])
    with tab_2_1:
        st.write('#### coral platy')
        img = Image.open('pages/platy.jpg')    # 이미지 파일 열기
        st.image(img, width=400)
        platyDF = pd.Series({'nickname':'Fatty', 'amount':'12'
                       , 'color':'red', 'size':'about 4cm', 'characteristics':'seems having obesity, never stop eating.'})
        st.table(platyDF)
        st.write("the one which H4PP1 kept from the start. got bigger and fatter day after day.")
        st.write("**Always waiting for feed in the front of the tank.**")

    with tab_2_2:
        st.write('#### albino full platinum guppy')
        img = Image.open('pages/guppy.jpg')    # 이미지 파일 열기
        st.image(img, width=400)
        guppyDF = pd.Series({'nickname':'Guppi', 'amount':'4'
                       , 'color':'white', 'size':'about 5cm', 'characteristics':'having little blindness, most expensive.'})
        st.table(guppyDF)
        st.write("the one which are most expensive. hard to breed because of weakness of sight. Some eat algaes a lot.")
        st.write('sometimes tends to try **breeding with the \'Fatty\'s**, look awkward.')
        img = Image.open('pages/guppyHospital.jpg')    # 이미지 파일 열기
        st.image(img, width=400)
        st.write('recently, H4PP1 went to fish hospital for medication of one of the guppies, had __Aeromonas__.')

    with tab_2_3:
        st.write('#### chocolate gourami')
        st.write('sorry, we couldn\'t get the photo of the creature. trying to get as soon as possible.')
        gouramiDF = pd.Series({'nickname':'Choco', 'amount':'1'
                       , 'color':'brown with ivory grids', 'size':'about 4cm', 'characteristics':'slow swimmer, very sensitive.'})
        st.table(gouramiDF)
        st.write("the one from wild, hard to adjust in the artificial environment. took a month to eat fish feed instead of bugs.")

with tab_3:
    st.write('### 𝄞 music')
    st.subheader('what H4PP1 listens')
    st.write('got to know that she tends to enjoy music in her recess, especially J-POPs. we got some main music in her playlists')
    st.write('**Royal Scandal** is an interesting part. think she loves the artist.')
    musicDF = pd.DataFrame({'music':['unravel','Phantasmagoria','Mermaid Theater','Bullet','Cherry Hunt','Queen of Heart','Mahou','Wonderland in Alice','SECRET;WEAPON','Meismerizer','Charles','Lower'], 'artist':['Ado','Attwn Park','Royal Scandal','Royal Scandal','Royal Scandal','Royal Scandal','Royal Scandal','Royal Scandal','CYTUS II: NOMA, Apo11o program','Satsuki','Balloon','Nooyuri'] })
    st.table(musicDF)
    st.markdown(
        """
        got some links related to the musics. those might help to understand H4PP1 more.
        - [Royal scandal] (https://royal-scandal.com/)
        - [Ado] (https://www.youtube.com/@Ado1024)
        - [Attwn Park] (https://www.youtube.com/@attwnpark)
        - [CYTUS II] (https://play.google.com/store/apps/details?id=com.rayark.cytus2&hl=en&pli=1)
        - [Mesmerizer] (https://youtu.be/19y8YTbvri8?feature=shared)
        - [Charles] (https://youtu.be/TA5OFS_xX0c?feature=shared)
        - [Lower] (https://youtu.be/3sEptl-psU0?feature=shared)
        """
    )
with tab_4:
    st.write('### 𖤣𖥧𖡼 strolling')
    st.write('interesting that she loves to stroll even if she doesn\'t like physical activities so much.')
    st.write('seems that she enjoys clean atmosphere outside, and boasting her pretty fashions.')
    img = Image.open('pages/strollroute.png')    # 이미지 파일 열기
    st.image(img, width=400)
    st.write('known that this is her stroll route everyday. takes about 1 hour and a half for a round trip.')
    img = Image.open('pages/cafe.jpg')    # 이미지 파일 열기
    st.image(img, width=400)
    st.write('guess she loves to visit a nice cafe during the strolling times.')
