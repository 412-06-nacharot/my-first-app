import streamlit as st

st.title("📝 เกมเติมคำศัพท์ภาษาอังกฤษ")

# 1. กำหนดค่าเริ่มต้นสำหรับเก็บคำตอบใน session_state
for i in range(1, 5):
    if f"ans{i}" not in st.session_state:
        st.session_state[f"ans{i}"] = ""

# 📌 ฟังก์ชันสำหรับเริ่มใหม่ (เคลียร์ค่าทุกช่อง)
def reset_game():
    for i in range(1, 5):
        st.session_state[f"ans{i}"] = ""


# ----------------------------------------------------
# 📌 ฟังก์ชัน แสดงผลสรุปคะแนน (Dialog / Pop-up)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการตรวจคำตอบ")
def show_result_dialog():
    st.balloons()
    score = 0

    # คลังเฉลยคำตอบ
    answers = {
        "ans1": ("apple", "ข้อ 1"),
        "ans2": ("fish", "ข้อ 2"),
        "ans3": ("dog", "ข้อ 3"),
        "ans4": ("banana", "ข้อ 4"),
    }

    # ตรวจทีละข้อ
    for key, (correct_ans, title) in answers.items():
        user_ans = st.session_state[key].strip().lower()
        if user_ans == correct_ans:
            st.success(f"✅ {title}: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ {title}: ยังไม่ถูกต้อง (คุณตอบ '{user_ans}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 เก่งมาก! ตอบถูกทั้งหมด")
    else:
        st.warning("💪 พยายามอีกนิดนะ!")


# ----------------------------------------------------
# 2. ช่องรับคำตอบ (เติมคำ)
# ----------------------------------------------------
st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    key="ans1",
)
st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    key="ans2",
)
st.text_input(
    "ข้อ 3: A `d _ g` is man's best friend. 🐶",
    key="ans3",
)
st.text_input(
    "ข้อ 4: Monkeys like to eat `b _ n _ n _`. 🍌",
    key="ans4",
)

st.divider()

# ----------------------------------------------------
# 3. ปุ่มควบคุม (ตรวจคำตอบ / เริ่มใหม่)
# ----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("📩 ตรวจคำตอบ", type="primary", use_container_width=True):
        show_result_dialog()

with col2:
    st.button("🔄 เคลียร์คำตอบ", on_click=reset_game, use_container_width=True)
