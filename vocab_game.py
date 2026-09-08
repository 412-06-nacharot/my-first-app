import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ให้ครบ 4 ข้อ
if "ans1" not in st.session_state:
    st.session_state.ans1 = ""
if "ans2" not in st.session_state:
    st.session_state.ans2 = ""
if "ans3" not in st.session_state:
    st.session_state.ans3 = ""
if "ans4" not in st.session_state:
    st.session_state.ans4 = ""
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1 = ""
    st.session_state.ans2 = ""
    st.session_state.ans3 = ""
    st.session_state.ans4 = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# 📌 ฟังก์ชันจบเกมเมื่อกดปุ่มส่งคำตอบ
def submit_game():
    st.session_state.is_ended = True


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog) สรุปผล
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง (`apple`)")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}') | เฉลย: `apple`")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง (`fish`)")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}') | เฉลย: `fish`")

    # ตรวจข้อ 3
    if u_ans3 == "dog":
        st.success("✅ ข้อ 3: ถูกต้อง (`dog`)")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}') | เฉลย: `dog`")

    # ตรวจข้อ 4
    if u_ans4 == "banana":
        st.success("✅ ข้อ 4: ถูกต้อง (`banana`)")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}') | เฉลย: `banana`")

    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. ส่วนควบคุมเวลาและการนับถอยหลัง (60 วินาที)
if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบแบบเติมคำสั้นๆ (ไม่มีประโยคภาษาอังกฤษ)
ans1 = st.text_input(
    "ข้อ 1: `a _ _ l e` 🍎",
    key="ans1",
    disabled=st.session_state.get("is_ended", False),
)
ans2 = st.text_input(
    "ข้อ 2: `f _ s h` 🐟",
    key="ans2",
    disabled=st.session_state.get("is_ended", False),
)
ans3 = st.text_input(
    "ข้อ 3: `d _ g` 🐶",
    key="ans3",
    disabled=st.session_state.get("is_ended", False),
)
ans4 = st.text_input(
    "ข้อ 4: `b _ n _ n _` 🍌",
    key="ans4",
    disabled=st.session_state.get("is_ended", False),
)

# 4. ปุ่มส่งคำตอบ (แสดงเมื่อเริ่มเล่นแล้ว และยังไม่จบเกม)
if "start" in st.session_state and not st.session_state.is_ended:
    st.button("📩 ส่งคำตอบ", on_click=submit_game, type="primary")

# 5. เรียก Dialog แสดงผลลัพธ์เมื่อกดส่งหรือหมดเวลา
if st.session_state.get("is_ended", False):
    show_result_dialog(
        st.session_state.ans1,
        st.session_state.ans2,
        st.session_state.ans3,
        st.session_state.ans4,
    )
elif "start" in st.session_state:
    time.sleep(1)
    st.rerun()
