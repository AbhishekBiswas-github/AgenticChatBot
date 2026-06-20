from src.langgraphagenticai.state.state import State


class BasicChatBot:
    """
    Basic Chatbot login implementation
    """

    def __init__(self, model):
        self.llm_model = model

    
    def process(self, state:State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """

        return {"messages": self.llm_model.invoke(state["messages"])}