import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadUI:
    def __init__(self):
        self.config = Config()
        self.userControls = {}


    def load_streamlit_ui(self):
        st.set_page_config(page_title=f"🤖 {self.config.get_page_title()}", layout='wide')
        st.header(f"🤖 {self.config.get_page_title()}")



        with st.sidebar:
            llm_options = self.config.get_llm_options()

            self.userControls["LLM_OPTION"] = st.selectbox("SELECT LLM", llm_options)

            if self.userControls["LLM_OPTION"] == "Groq":
                model_options = self.config.get_llm_models()
                self.userControls["MODEL_OPTIONS"] = st.selectbox("SELECT MODEL", model_options)
                self.userControls["GROQ_API_KEY"] = st.text_input("API KEY", type="password")
                if not self.userControls["GROQ_API_KEY"]:
                    st.warning("⚠️ To get an API KEY, visit https://console.groq.com. ")

            
            self.userControls["USECASE"] = st.selectbox("SELECT USECASE", self.config.get_usecase_options())

        return self.userControls