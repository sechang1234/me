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

# --- 선명하고 진한 색상을 위한 CSS 스타일 ---
st.markdown("""
    <style>
    div.stButton > button {
        width: 100% !important;
        height: 350px !important;
        font-size: 40px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        border-radius: 20px !important;
        border: 5px solid #FFFFFF !important;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3) !important;
    }
    
    .css-home div.stButton > button { background-color: #1E3A8A !important; }
    .css-waiting div.stButton > button { background-color: #DC2626 !important; }
    .css-ready div.stButton > button { background-color: #16A34A !important; }
    </style>
""", unsafe_allow_html=True)

# --- 게임 로직 제어 ---

# 1. 시작 화면
if st.session_state.stage == "home":
    st.markdown('<div class="css-home">', unsafe_allow_html=True)
    if st.button("시작하려면 클릭 (파란색)"):
        st.session_state.stage = "waiting"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 대기 화면 (빨간불)
elif st.session_state.stage == "waiting":
    st.markdown('<div class="css-waiting">', unsafe_allow_html=True)
    if st.button("아직 누르지 마세요! (빨간색)"):
        st.session_state.stage = "foul"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 랜덤 대기 (2초 ~ 4초)
    delay = random.uniform(2.0, 4.0)
    time.sleep(delay)
    
    # 초록불로 전환
    st.session_state.stage = "ready"
    st.session_state.start_time = time.time()
    st.rerun()

# 3. 초록불 화면 (클릭!)
elif st.session_state.stage == "ready":
    st.markdown('<div class="css-ready">', unsafe_allow_html=True)
    if st.button("지금 클릭하세요!!! (초록색)"):
        end_time = time.time()
        reaction_time = (end_time - st.session_state.start_time) * 1000
        st.session_state.reaction_time = int(reaction_time)
        st.session_state.stage = "result"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 결과 화면
elif st.session_state.stage == "result":
    st.markdown(f"## 🎯 결과: **{st.session_state.reaction_time} ms**")
    
    if st.session_state.reaction_time < 200:
        st.balloons()
        st.success("🏃‍♂️ 인간계를 초월한 속도입니다!")
    elif st.session_state.reaction_time < 300:
        st.info("👍 평균 이상! 아주 빠릅니다.")
    else:
        st.warning("🐢 조금 더 집중해 볼까요?")

    if st.button("🔄 다시 도전하기"):
        st.session_state.stage = "waiting"
        st.rerun()

# 5. 부정 클릭 화면
elif st.session_state.stage == "foul":
    st.error("⚠️ 너무 빨랐습니다! 초록색 불이 켜지면 누르세요.")
    if st.button("🔄
