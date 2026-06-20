from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot import BasicChatBot



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph = StateGraph(State)

    def basic_graph_builder(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot = BasicChatBot(self.llm)

        self.graph.add_node("chatbot", self.basic_chatbot.process)
        
        self.graph.add_edge(START, "chatbot")
        self.graph.add_edge("chatbot", END)

        

    def setup_graph(self, usecase:str):
        """
        Call the function specific to use case
        E.g.
        Basic Chatbot -> graph_builder
        """
        if usecase == "Basic Chatbot":
            self.basic_graph_builder()

        return self.graph.compile()