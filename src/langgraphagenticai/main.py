import streamlit as st
from src.langgraphagenticai.ui.streamlit.loadui import LoadUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graphs.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlit.display_results import DisplayResultStreamlitUI


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

    if userMessage:
        try:
            # LLM Model 
            groq_llm = GroqLLM(userInput)
            model = groq_llm.get_llm_model()
            if not model:
                st.error("Failed to load the model")
                return 
            
            # Use Case 
            usecase = userInput.get("USECASE")
            if not usecase:
                st.error("Use Case not defiled")
                return 
            
            # Graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlitUI(usecase, graph, userMessage).display_result_on_ui()
            
            except Exception as e:
                st.error(f"Error: Graph set up failed in graph builder{e}")
                return 

        except Exception as e:
            st.error(f"Error: Graph set up failed user message block{e}")
            return 
