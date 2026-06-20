import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_control_inputs):
        self.user_control_inputs = user_control_inputs


    def load_llm(self):
        try:
            api_key = self.user_control_inputs["GROQ_API_KEY"]
            llm_model = self.user_control_inputs["MODEL_OPTIONS"]
            if api_key == "" or os.environ["GROQ_API_KEY"] == "":
                st.error("Please enter the API KEY")

            llm = ChatGroq(
                api_key=api_key,
                model=llm_model
            )

        except Exception as e:
            raise ValueError(f"Error occured with exception {e}")
        
        return llm 