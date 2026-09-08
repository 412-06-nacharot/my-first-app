import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
# ✏️ [จุดที่ 1] เพิ่ม session_state สำหรับข้อ 3 และ 4
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    # ✏️ [จุดที่ 2] เคลียร์ค่าช่องข้อ 3 และ 4
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):  # ✏️ [จุดที่ 3] เพิ่มรับพารามิเตอร์ ans3, ans4
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [จุดที่ 3] เพิ่มการตรวจข้อ 3 และ 4
    if u_ans3 == "dog":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "book":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    # ปรับเงื่อนไขชนะเป็น 4 คะแนน
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        # เรียก Dialog พร้อมส่งค่าทั้ง 4 ข้อเมื่อหมดเวลา
        show_result_dialog(
            st.session_state.ans1_val,
            st.session_state.ans2_val,
            st.session_state.ans3_val,
            st.session_state.ans4_val,
        )

st.divider()

# 3. ช่องรับคำตอบ
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
    key="ans1_val",
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
    key="ans2_val",
)

# ✏️ [จุดที่ 4] เพิ่มช่องรับคำตอบข้อ 3 และ 4
ans3 = st.text_input(
    "ข้อ 3: A `d _ g` is man's best friend. 🐶",
    value=st.session_state.ans3_val,
    key="ans3_val",
)
ans4 = st.text_input(
    "ข้อ 4: I like to read a `b _ _ k` before sleeping. 📚",
    value=st.session_state.ans4_val,
    key="ans4_val",
)
