import streamlit as st
from meta_ai_api import MetaAI
from streamlit_option_menu import option_menu

header = st.container()
ai = MetaAI()

# Giao diện chatbot
def streamlit_ui():
    with st.sidebar:
        choice = option_menu('Solar can help you with:',["Essay Samples","Grading Essay"])

    if choice == 'Essay Samples':
        with header: 
            st.markdown(''':orange[Solar] :sunny: &mdash; :rainbow[A great mentor on your IELTS Writing journey.]''')
            st.markdown("""Out of ideas :sparkles: and don't know where to start? Let Solar give you some templates and examples :page_facing_up:""")
            Essay_Samples()
            
    elif choice == 'Grading Essay':
        with header:
            st.markdown(''':orange[Solar] :sunny: &mdash; :rainbow[A great mentor on your IELTS Writing journey.]''')
            st.markdown("""Wanna know your current band? :laughing: Let Solar help you mark that essay :100:""")
            Grading_Essay()
            
def Essay_Samples():
    mission = "Give me a template and an example to do this IELTS Writting Task 2 topic"

    chat_history1 = []
    # Initialize lịch sử chat 
    if "messages" not in st.session_state:
        st.session_state.messages1 =[]
    
    # Màn hình hỏi đáp
    st.markdown(""":green[IETLS Writting] :blue[Task 2] :violet[topic] : """)
    if topic := st.chat_input("Enter your topic here:"):
        topic = f"Topic: \"{topic}\""
        # Hiển thi câu hỏi của người dùng
        st.chat_message("user").markdown(topic)
        # Thêm câu hỏi của người dùng vào lịch sử chat
        st.session_state.messages1.append({"role":"user","context":topic})

        # Xử lý câu hỏi bằng LLM
        message_to_chatbot = f"{mission}:\n{topic}\""
        response = ai.prompt(message=message_to_chatbot)
        answer = [value for key, value in response.items() if key == "message"][0]
        
        with open("AI_response/essay_output.txt", "a") as f:
            f.write(answer)
        
        # Hiển thị câu trả lời của chatbot
        with st.chat_message("assistant"):
            st.markdown(answer)
        # Thêm câu hỏi của chatbot vào lịch sử chat
        st.session_state.messages1.append({'role':"assistant", "content":response})
        chat_history1.append({topic,answer})

def Grading_Essay():
    mission = "Help me to grade this IELTS Writting Task 2 Essay"

    chat_history2 = []
    # Initialize lịch sử chat 
    if "messages" not in st.session_state:
        st.session_state.messages2 =[]
    
    # Màn hình hỏi đáp
    st.markdown(""":green[IETLS Writting] :blue[Task 2] :violet[topic] : """)
    if topic := st.text_input("Enter your topic here:"):
        topic = f"Topic: \"{topic}\""
        print(topic)
        st.markdown(""":orange[Your] :red[essay] : """)

        if essay := st.chat_input("Enter your essay here:"):
            essay = f"Essay: \"{essay}\""
            print(essay)
            user_promp = f"{topic}\n{essay}"

            # Hiển thi câu hỏi của người dùng
            st.chat_message("user").markdown(user_promp)
            # Thêm câu hỏi của người dùng vào lịch sử chat
            st.session_state.messages2.append({"role":"user","context":user_promp})

            # Xử lý câu hỏi bằng LLM
            message_to_chatbot = f"{mission}:\n{user_promp}"
            # print(message_to_chatbot)
            # message_to_chatbot = "1+1=?"
            response = ai.prompt(message=message_to_chatbot)
            answer = [value for key, value in response.items() if key == "message"][0]
            
            with open("AI_response/grade_output.txt", "a") as f:
                f.write(answer)
            
            # Hiển thị câu trả lời của chatbot
            with st.chat_message("assistant"):
                st.markdown(answer)
            # Thêm câu hỏi của chatbot vào lịch sử chat
            st.session_state.messages2.append({'role':"assistant", "content":response})
            chat_history2.append({topic,answer})

streamlit_ui()
