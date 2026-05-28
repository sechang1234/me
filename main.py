import streamlit as st
import time
import random

# 페이지 설정
st.set_page_config(page_title="반응속도 테스트", page_icon="⚡", layout="centered")

st.title("⚡ 반응속도 테스트")
st.write("빨간색 화면이 **초록색**으로 바뀌는 순간 마우스를 재빨리 클릭하세요!")

# 세션 상태 변수 초기화
if "stage" not in st.session_state:
    st.session_state.stage = "home"  # home, waiting, ready, result, foul
if "start_time" not in st.session_state:
    st.session_state.start_time = 0.0

# 스타일 지정을 위한 CSS 믹스인 (큰 버튼 구현)
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 300px;
        font-size: 30px !important;
        font-weight: bold;
        color: white !important;
        border-radius: 15px;
        border: none;
        transition: 0.1s;
    }
    /* 각 상태별 버튼 색상 지정 */
    .css-home > div.stButton > button { background-color: #4A90E2; }
    .css-waiting > div.stButton > button { background-color: #E24A4A; }
    .css-ready > div.stButton > button { background-color: #2ECC71; }
    </style>
""", unsafe_allow_html=True)

# --- 게임 로직 제어 ---

# 1. 시작 화면
if st.session_state.stage == "home":
    st.markdown('<div class="css-home">', unsafe_allow_html=True)
    if st.button("시작하려면 클릭하세요 (파란색)"):
        st.session_state.stage = "waiting"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 대기 화면 (빨간불)
elif st.session_state.stage == "waiting":
    st.markdown('<div class="css-waiting">', unsafe_allow_html=True)
    
    # 부정클릭 방지용 버튼
    # 초록불이 되기 전에 누르면 '부정클릭(foul)' 처리
    if st.button("초록색이 되면 클릭하세요! (지금은 빨간색)"):
        st.session_state.stage = "foul"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
