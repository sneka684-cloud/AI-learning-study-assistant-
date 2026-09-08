import streamlit as st

st.title("🤖 AI Learning & Study Assistant")

st.write("Welcome to your personal AI Learning Assistant!")

question = st.text_input("Ask your study question:")

if question:
    st.subheader("🤖 AI Answer")

    if "python" in question.lower():
        st.write(
            "Python is a high-level programming language. "
            "It is easy to learn and widely used in AI, data science, "
            "web development and automation."
        )

    elif "ai" in question.lower():
        st.write(
            "Artificial Intelligence (AI) is a technology that enables "
            "computers to perform tasks that normally require human intelligence."
        )

    else:
        st.write(
            "I received your question. An AI-generated answer will appear here."
        )

st.subheader("🛠️ Study Tools")

if st.button("Create Study Plan"):
    st.subheader("📚 Your Study Plan")
    st.write("1. Choose your subject")
    st.write("2. Study the important topics")
    st.write("3. Practice questions")
    st.write("4. Revise what you learned")
    st.success("Study plan created successfully! ✅")

if st.button("Generate Quiz"):
    st.subheader("📝 Practice Quiz")

    st.write("*1. What is Python?*")
    st.write("A) Programming Language")
    st.write("B) Operating System")
    st.write("C) Database")
    st.write("D) Browser")

    answer = st.radio("Select your answer:", ["A", "B", "C", "D"])

    if st.button("Submit Answer"):
        if answer == "A":
            st.success("Correct Answer! 🎉")
        else:
            st.error("Wrong Answer. Try again!")
st.subheader("📊 Study Progress")

progress = st.slider(
    "How much have you completed?",
    0,
    100,
    0
)

st.progress(progress)

if progress == 100:
    st.success("🎉 Study completed!")
else:
    st.info(f"You have completed {progress}% of your study.")
st.subheader("📝 My Notes")

notes = st.text_area("Write your study notes here:")

if st.button("Save Notes"):
    if notes:
        st.success("Notes saved successfully! ✅")
    else:
        st.warning("Please enter some notes first.")