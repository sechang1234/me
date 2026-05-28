import streamlit as st
import time
import random

# 페이지 설정
st.set_page_config(page_title="반응속도 테스트", page_icon="⚡", layout="centered")

st.title("⚡ 반응속도 테스트")
st.write("화면이 **초록색**으로 바뀌는 순간 마우스를 재빨리 클릭하세요!")

# 세션 상태 변수 초기화
if "stage" not in st.session_state:
    st.session_state.stage = "home"  # home, waiting, ready, result, foul
if "start_time" not in st.session_state:
    st.session_state.start_time = 0.0

# --- 선명하고 진한 색상을 위한 CSS 스타일 고도화 ---
st.markdown("""
    <style>
    /* 기본 버튼 스타일 리셋 및 강화 */
    div.stButton > button {
        width: 100% !important;
        height: 350px !important;
        font-size: 40px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important; /* 무조건 흰색 글씨 */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5); /* 글씨 그림자로 가시성 확보 */
        border-radius: 20px !important;
        border: 5px solid #FFFFFF !important; /* 테두리 흰색 선명하게 */
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3) !important;
        transition: none !important;
    }
    
    /* 1. 시작 화면 (진한 파란색) */
    .css-home div.stButton > button {
        background-color: #1E3A8A !important; 
    }
    
    /* 2. 대기 화면 (강렬한 빨간색) */
    .css-waiting div.stButton > button {
        background-color: #DC2626 !important; 
    }
    
    /* 3. 클릭 화면 (선명한 초록색) */
    .css-ready div.stButton > button {
        background-color: #16A34A !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 게임 로직 제어 ---

# 1. 시작 화면
if st.session_state.stage == "home":
    st.markdown('<div class="css-home">', unsafe_allow_html=True)
    if st.button("시작하려면 클릭 (파란색)"):
        st.session_state.stage = "waiting"
        st.rerun()
    st.
