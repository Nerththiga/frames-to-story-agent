from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

from metadata_extractor import get_metadata
from story_generator import get_story

class Frames2Story(TypedDict):
    dir_path: str
    metadata: list

frames2story_generator = StateGraph(Frames2Story)
frames2story_generator.add_node("metadata_extractor", get_metadata)
frames2story_generator.add_node("story_generator", get_story)
frames2story_generator.add_edge(START, "metadata_extractor")
frames2story_generator.add_edge("metadata_extractor", "story_generator")
frames2story_generator.add_edge("story_generator", END)

frames2story_agent = frames2story_generator.compile()