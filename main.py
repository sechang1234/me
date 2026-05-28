import streamlit as st
import time
import random

# 페이지 레이아웃을 '전체 화면(wide)'으로 강제 설정
st.set_page_config(page_title="반응속도 테스트", layout="wide")

# 세션 상태 초기화
if "stage" not in st.session_state:
    st.session_state.stage = "home"
if "start_time" not in st.session_state:
    st.session_state.start_time = 0.0

# --- 화면 전체를 색상으로 채워버리는 강력한 CSS ---
st.markdown("""
    <style>
    /* 상단 메뉴바와 여백을 완전히 제거해서 화면을 꽉 채웁니다 */
    [data-testid="stHeader"] {background: rgba(0,0,0,0) !important;}
    .block-container {padding: 0px !important; max-width: 100% !important;}
    
    /* 화면 전체를 버튼으로 만드는 스타일 */
    div.stButton > button {
        width: 100vw !important;
        height: 100vh !important;
        font-size: 60px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        border: none !important;
        border-radius: 0px !important;
        position: fixed !important;
        top: 0; left: 0; z-index: 99999;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- 게임 로직 및 색상 강제 지정 ---

# 1. 시작 화면 (진한 파란색)
if st.session_state.stage == "home":
    st.markdown("<style>div.stButton > button {background-color: #1E40AF !important;}</style>", unsafe_allow_html=True)
    if st.button("화면을 클릭하면 테스트가 시작됩니다"):
        st.session_state.stage = "waiting"
        st.rerun()

# 2. 대기 화면 (강렬한 빨간색)
elif st.session_state.stage == "waiting":
    st.markdown("<style>div.stButton > button {background-color: #DC2626 !important;}</style>", unsafe_allow_html=True)
    if st.button("아직 누르지 마세요! 초록색이 되면 클릭하세요!"):
        st.session_state.stage = "foul"
        st.rerun()
    
    # 2초 ~ 4.5초 사이 랜덤 대기
    delay = random.uniform(2.0, 4.5)
    time.sleep(delay)
    
    # 초록불로 전환
    st.session_state.stage = "ready"
    st.session_state.start_time = time.time()
    st.rerun()

# 3. 초록불 화면 (선명한 초록색)
elif st.session_state.stage == "ready":
    st.markdown("<style>div.stButton > button {background-color: #16A34A !important;}</style>", unsafe_allow_html=True)
    if st.button("지금 클릭하세요!!!"):
        end_time = time.time()
        reaction_time = (end_time - st.session_state.start_time) * 1000
        st.session_state.reaction_time = int(reaction_time)
        st.session_state.stage = "result"
        st.rerun()

# 4. 결과 화면 (회색 배경에 결과 표시)
elif st.session_state.stage == "result":
    st.markdown("<style>div.stButton > button {background-color: #4B5563 !important; height: 200px !important; position: static !important;}</style>", unsafe_allow_html=True)
    
    st.container()
    st.markdown(f"<h1 style='text-align:center; margin-top:100px; font-size:80px;'>🎯 {st.session_state.reaction_time} ms</h1>", unsafe_allow_html=True)
    
    if st.session_state.reaction_time < 200:
        st.markdown("<h3 style='text-align:center; color:#16A34A;'>🏃‍♂️ 인간계를 초월한 신체 능력!</h3>", unsafe_allow_html=True)
    elif st.session_state.reaction_time < 300:
        st.markdown("<h3 style='text-align:center; color:#2563EB;'>👍 평균보다 빠른 편입니다!</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align:center; color:#DC2626;'>🐢 조금 더 집중해 보세요!</h3>", unsafe_allow_html=True)
        
    if st.button("🔄 다시 도전하려면 여기를 클릭"):
        st.session_state.stage = "waiting"
        st.rerun()

# 5. 부정 클릭 화면
elif st.session_state.stage == "foul":
    st.markdown("<style>div.stButton > button {background-color: #7C2D12 !important; height: 200px !important; position: static !important;}</style>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; margin-top:100px; color:#DC2626; font-size:60px;'>⚠️ 너무 빨랐습니다!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>초록색 불이 켜진 후에 눌러야 합니다.</h3>", unsafe_allow_html=True)
    
    if st.button("🔄 다시 도전하기"):
        st.session_state.stage = "waiting"
        st.rerun()
