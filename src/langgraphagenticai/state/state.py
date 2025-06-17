from typing_extensions import TypedDict
from typing import Annotated, Literal, Optional, List
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """

    messages: Annotated[list, add_messages]