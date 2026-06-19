import streamlit as st
from src.langgraphagenticai.ui.streamlit.loadui import LoadUI


def load_langgraph_agentic_ai_ui():
    """
    Loads and runs the langgraph AgenticAI applications with Streamlit UI
    This function initializes the UI, handles user input, congigures the LLM model,
    sets up the graph based on the selected use case, and display the output while
    implementing exception handling for robustness
    """

    # Load UI
    ui = LoadUI()
    userInput = ui.load_streamlit_ui()

    if not userInput:
        st.error("❗Error: Failed to load user input from the UI.")
        return
    
    userMessage = st.chat_input("Enter your message")