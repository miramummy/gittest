from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st
st.title("디지털 정보창 " + chat_model.model)
subject =st.text_input("알고 싶은것 입력해 주세요")

if st.button("궁금증 해결해줘~", type="primary", icon="🚨"):  
    with st.spinner("Wait for it...", show_time=False):
        response = chat_model.invoke(subject + "에 대해서 설명해줘")
        st.write("완료")
        st.write(response.content)    
