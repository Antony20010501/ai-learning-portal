import streamlit as st

st.set_page_config(page_title="AI Learning Portal", page_icon="📘")
st.title("📘 AI Learning Portal")

uploaded_file = st.file_uploader("Upload a lecture file", type=["pdf", "docx", "txt"])

if uploaded_file:
    st.success(f"File uploaded: {uploaded_file.name}")
    
    quiz_type = st.radio("Choose question type", ["MCQ", "Short Answer"])
    num_questions = st.slider("How many questions do you want?", 1, 10, 5)
    flashcards_option = st.checkbox("Generate Flashcards")

    if st.button("Generate"):
        st.write("---")
        st.subheader("Generated Questions")
        for i in range(num_questions):
            if quiz_type == "MCQ":
                st.markdown(f"**Q{i+1}:** What is a sample MCQ question?")
                st.markdown("- Option A\n- Option B\n- Option C\n- Option D")
            else:
                st.markdown(f"**Q{i+1}:** What is a sample short answer question?")

        if flashcards_option:
            st.subheader("🃏 Flashcards")
            for i in range(num_questions):
                st.markdown(f"**Card {i+1}:**")
                st.markdown(f"Front: Sample Flashcard Q{i+1}")
                st.markdown(f"Back: Sample Flashcard A{i+1}")
