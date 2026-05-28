import streamlit as st
import time
import random

# 1. 페이지 초기 설정
st.set_page_config(page_title="반응속도 테스트", layout="centered")
st.title("⚡ 반응속도 테스트")
st.write("빨간색 화면이 초록색으로 바뀌면 최대한 빨리 클릭하세요!")

# 2. 세션 상태(데이터 기억) 초기화
if "stage" not in st.session_state:
    st.session_state.stage = "home"
if "start_time" not in st.session_state:
    st.session_state.start_time = 0.0

# 3. 화면을 큼직하게 채워줄 확실한 CSS 스타일
st.markdown("""
    <style>
    div.stButton > button {
        width: 100% !important;
        height: 300px !important;
        font-size: 35px !important;
        font-weight: bold !important;
        color: white !important;
        border-radius: 15px !important;
    }
    .css-home div.stButton > button { background-color: #1E3A8A !important; }
    .css-waiting div.stButton > button { background-color: #DC2626 !important; }
    .css-ready div.stButton > button { background-color: #16A34A !important; }
    </style>
""", unsafe_allow_html=True)

# 4. 게임 핵심 로직 (왼쪽 벽에 딱 붙여서 에러 방지)
if st.session_state.stage == "home":
    st.markdown('<div class="css-home">', unsafe_allow_html=True)
    if st.button("시작하려면 클릭 (파란색)"):
        st.session_state.stage = "waiting"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.stage == "waiting":
    st.markdown('<div class="css-waiting">', unsafe_allow_html=True)
    if st.button("아직 누르지 마세요 (빨간색)"):
        st.session_state.stage = "foul"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2초 ~ 4초 사이 랜덤 대기 후 초록불로 전환
    delay = random.uniform(2.0, 4.0)
    time.sleep(delay)
    st.session_state.stage = "ready"
    st.session_state.start_time = time.time()
    st.rerun()

elif st.session_state.stage == "ready":
    st.markdown('<div class="css-ready">', unsafe_allow_html=True)
    if st.button("지금 클릭하세요 (초록색)"):
        end_time = time.time()
        reaction_time = (end_time - st.session_state.start_time) * 1000
        st.session_state.reaction_time = int(reaction_time)
        st.session_state.stage = "result"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif
