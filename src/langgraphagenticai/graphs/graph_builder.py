from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph = StateGraph(State)

    def graph_builder(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """


        self.graph.add_node("chatbot", "")
        
        self.graph.set_entry_point("chatbot")
        self.graph.add_edge("chatbot", END)

        