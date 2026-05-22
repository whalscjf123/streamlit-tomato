import pandas as pd
import streamlit as st
import joblib

# 임의의 모델 로드 또는 정의 (기존에 정의된 rf_model이 있다고 가정합니다)
# import pickle
rf_model = joblib.load("tomato_model.pkl")

# 웹 페이지 제목 설정
st.title("🌱 착과율 예측 프로그램")
st.write("외부 온도, 지온, 내부 온도를 입력하여 착과율을 예측하세요.")

st.divider()  # 시각적인 구분선

# 1. 사용자 입력 받기 (Streamlit 사이드바 또는 메인 화면에 배치 가능)
st.subheader("📊 데이터 입력")

ext_temp = st.number_input(
    "외부 온도 입력 (°C)", value=20.0, step=0.1, format="%.1f"
)
soil_temp = st.number_input(
    "지온 입력 (°C)", value=15.0, step=0.1, format="%.1f"
)
int_temp = st.number_input(
    "내부 온도 입력 (°C)", value=22.0, step=0.1, format="%.1f"
)

st.divider()

# 2. DataFrame으로 변환 (2차원 배열 형태로 입력)
input_data = pd.DataFrame(
    [[ext_temp, soil_temp, int_temp]],
    columns=["외부온도", "지온", "내부온도"],
)

# 3. 예측 및 결과 출력
# 사용자가 버튼을 눌렀을 때만 예측이 실행되도록 설정합니다.
if st.button("🔮 착과율 예측하기", type="primary"):
    try:
        # 예측 진행
        predicted = rf_model.predict(input_data)

        # 결과 출력 (성공 메시지 박스 형태)
        st.success(f"### 🎉 예측 착과율 : **{predicted[0]:.1f}%**")

    except NameError:
        st.error(
            "rf_model이 정의되지 않았습니다. 모델 로드 코드를 상단에 추가해주세요."
        )