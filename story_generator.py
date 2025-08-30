from llm_client import get_response

story_schema = {
    "type": "object",
    "title": "Generated Story",
    "properties": {
        "title": {
            "type": "string",
            "description": "An appropriate title suitable for the story"
        },
        "characters": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of main characters from objects_detected arrays"
        },
        "summary": {
            "type": "string",
            "description": "A 2-3 sentence summary based on scene descriptions"
        },
        "events": {
            "type": "array",
            "description": "Chronological sequence of story events mapped to frames",
            "items": {
                "type": "object",
                "properties": {
                    "frame": {
                        "type": "string",
                        "description": "The exact frame_id value (e.g., '1.png')"
                    },
                    "event": {
                        "type": "string",
                        "description": "Description of what happens in this frame based on scene_description"
                    }
                },
                "required": ["frame", "event"]
            }
        }
    },
    "required": ["title", "characters", "summary", "events"]
}


# def get_story(metadata):
def get_story(state):
    metadata = state["metadata"]
    print(f"Generating story with {len(metadata)} frames.")
    
    prompt = f"""
        You are a story generator. 
        Analyze this sequence of frames and create a coherent story.

        Frame Data:
        {metadata}

        Follow the chronological order of frames when writing the story."""

    contents = [
        prompt
    ]
    
    generated_story = get_response(contents, story_schema)


# metadata = [
#   {
#     "frame_id": "image_001",
#     "timestamp": "2024-07-30T12:35:10Z",
#     "objects_detected": [
#       "crow",
#       "food",
#       "tree trunk",
#       "tree branch",
#       "bushes",
#       "sky"
#     ],
#     "scene_description": "A black crow is depicted in mid-flight, holding a round, orange piece of food, possibly bread or a biscuit, in its beak. It is flying past a bare tree branch, with a clear blue sky in the background and green foliage visible at the bottom right."
#   },
#   {
#     "frame_id": "image_001",
#     "timestamp": "2024-05-15T12:00:00Z",
#     "objects_detected": [
#       "crow",
#       "fox",
#       "tree",
#       "bread",
#       "bush"
#     ],
#     "scene_description": "A crow is perched on a tree branch, holding a piece of bread in its beak. Below, a fox sits on the ground, looking up at the crow with its tongue out, appearing to desire the food. The setting is outdoors with a blue sky."
#   },
#   {
#     "frame_id": "image_001",
#     "timestamp": "2024-07-30T12:00:00Z",
#     "objects_detected": [
#       "crow",
#       "fox",
#       "tree",
#       "food",
#       "bush",
#       "grass"
#     ],
#     "scene_description": "A crow is perched on a tree branch, holding a piece of food in its beak. Below, a fox sits on the ground, looking up at the crow with one paw raised, seemingly trying to entice the crow to drop its food. The scene takes place outdoors with a blue sky and green foliage in the background."
#   },
#   {
#     "frame_id": "image_001",
#     "timestamp": "2024-05-23T12:00:00Z",
#     "objects_detected": [
#       "crow",
#       "tree",
#       "branch",
#       "food item"
#     ],
#     "scene_description": "A cartoon illustration shows a crow perched on a tree branch, dropping a food item from its open beak. The food item has motion lines around it, suggesting it is falling or has just been released. The background is a clear blue sky with a hint of green foliage on the bottom right."
#   },
#   {
#     "frame_id": "image_of_crow_fox_and_food_dropping",
#     "timestamp": "2023-10-27T10:00:00Z",
#     "objects_detected": [
#       "crow",
#       "fox",
#       "tree branch",
#       "food item"
#     ],
#     "scene_description": "A crow is perched on a tree branch, dropping a piece of food from its beak. Below, a fox looks up with an open mouth, appearing to try and catch the falling food."
#   },
#   {
#     "frame_id": "img_0001",
#     "timestamp": "2024-07-29T12:00:00Z",
#     "objects_detected": [
#       "fox",
#       "tree",
#       "grass",
#       "sky",
#       "path"
#     ],
#     "scene_description": "A cartoon fox is depicted mid-stride, running across a dirt path in a natural outdoor setting. A tree trunk is visible on the left, and green bushes or grass line the path under a blue sky."
#   }
# ]

# get_story(metadata)