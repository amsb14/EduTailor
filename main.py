import streamlit as st
import teacher
import student

st.markdown("<h2 style='text-align: center; color: black;'>AI-Powered Personalized Academic Aid</h2>", unsafe_allow_html=True)

# Add an input field for the API key
openai_api_key = st.text_input("Enter your OpenAI API key")

# Check if 'role' is in the session state
if 'role' not in st.session_state:
    # If not, present the selection box
    st.session_state['role'] = st.selectbox("Select Your Role", ["Teacher", "Student"])
elif st.session_state['role'] == "Teacher":
    # If 'role' is in the session state and is "Teacher", present the selection box
    st.session_state['role'] = st.selectbox("Select Your Role", ["Teacher", "Student"])
else:
    # If 'role' is "Student", don't present the selection box and display the role
    st.write(f"Role: {st.session_state['role']}")

# Store the API key in session state
st.session_state['openai_api_key'] = openai_api_key

if st.session_state['role'] == "Teacher":
    if openai_api_key:
        teacher.teacher_actions(openai_api_key)
    else:
        st.warning("Please enter your OpenAI API key to proceed.")

elif st.session_state['role'] == "Student":
    student.student_actions()
