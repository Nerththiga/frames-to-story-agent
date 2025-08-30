from llm_client import get_response
from datetime import datetime, timezone
from google.genai import types
import json
import os

scene_metadata_schema = {
    "type": "object",
    "title": "Scene Metadata",
    "properties": {
        "frame_id": {
            "type": "string",
            "description": "Filename of the image"
        },
        "timestamp": {
            "type": "string",
            "description": "UTC timestamp in ISO 8601 format"
        },
        "objects_detected": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of detected objects/characters"
        },
        "scene_description": {
            "type": "string",
            "description": "Description of what's happening in the scene"
        }
    },
    "required": ["frame_id", "timestamp", "objects_detected", "scene_description"]
}


# def get_metadata(dir_path = DIR_PATH):
def get_metadata(state):
    dir_path = state["dir_path"]
    metadata_list = []

    ims = sorted(os.listdir(dir_path))
    print(f"Image list: {ims}")

    for im in ims:
        img_path = os.path.join(dir_path, im)
        print(f"Processing: {img_path}")
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        prompt = f"""
        Your task is to extract key characters/objects and describe the scene event in one line from the given image.
        "frame_id": "{im}",
        "timestamp": "{timestamp}"
        """

        with open(img_path, 'rb') as f:
            img2_bytes = f.read()

        contents = [
            prompt,
            types.Part.from_bytes(
                data=img2_bytes,
                mime_type='image/png'
            )
        ]
        
        metadata = get_response(contents, scene_metadata_schema)
        metadata_list.append(metadata)

    metadata_json = f"metadata\{os.path.basename(os.path.normpath(dir_path))}.json"
    with open(metadata_json, 'w') as f:
        json.dump(metadata_list, f, indent=2)

    return {"metadata": metadata_list}

# get_metadata(DIR_PATH)