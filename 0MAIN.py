#MAIN_Page

#library import
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit_pandas as sp
from PIL import Image




#CODE
st.set_page_config(     # 페이지 설정
    page_title="Profile LOADING...", # 페이지 Tab의 타이틀
    page_icon="🙃",     # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    initial_sidebar_state="expanded", # 사이드바 초기 상태: auto, collapsed, expanded
)

st.write("👾        access to the profile...")
st.write("👾        access approved")
st.write("👾        profile loading... codeName : H4PP1")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.markdown(   # st.markdown()을 이용한 본문 작성
    """
    ## H4PP1
    """
)

img = Image.open('profile.jpg')    # 이미지 파일 열기
st.image(img, width=400)          # 이미지 출력
img = Image.open('snapshot.jpg')    # 이미지 파일 열기
st.image(img, width=400)          # 이미지 출력
st.write("quite a nice photo we hardly got...")

df = pd.DataFrame({'details':['Noh Yena (노예나)','female','21','South Korea','student','Hongik University, Seoul','graphic design','INTJ','sunshine yellow(#FFFF00)','☻ usually hides behind her codename \'H4PP1\'.(read in \'happi\')  ☻ concept of profile character is from the smiling emoji.   ☻ says the ultimate goal is to become a one-man game developer, actually studying both design and programming now. actively working in game developing circle ExP. ☻ best work regardless of genre, she says that it is < A Little Fish\'s Dream > which was made with C4D. She says it is sad that she couldn\'t finish the work in time for exhibition, but keep developing for a perfect end.  ☻ at first it seemed she didn\'t like using 3D, but now she is enjoying it.    ☻ likes to play games, especially prefers character development genre.(some of the best games in her life is \'Pokemon series(Nintendo, Game Freak)\', \'Happy Fish(Happy Elements)\', \'Catcafe(Estgames)\', \'GirlsFrontline(Sunborn)\', most are mobile games.)      ☻ loves little fish, actually keeps some fish as a pet. frequently uploads photo of her pets.   ☻ talks a lot about trivial things in daily life in SNS. \'Want to go home...\' is never been absent.   ☻ never stopped art since 7years old.']}
                  , index=['real name','sex','age','nationality','job','affiliation','major','MBTI','representing color','characteristics'])

st.table(df)
    
st.markdown(
    """
    #### SNS accounts :
    - [☻☻☻☻☻] (https://www.instagram.com/happi_owo/)
    - [𓆝 ⋆｡𖦹°‧] ("https://www.instagram.com/happi._.oo/)
    - [����] ("https://www.instagram.com/exit.aht4e_lpipe1r/)

    Information collected **left sidebar**. Only **APPROVED** users can open the files.\n\n
    

    #### server manager :
    - main :    ����     (@�����.���)
    - sub :     ���      (@����), 
                �������� (@- )\n\n
  
    #### file modification history :
    """
)
  
st.write('[click HERE] (http://localghost:666/)')

st.sidebar.success("Access Approved")  # 사이드바에 success 메시지 출력