# Frames-to-Story-Agent

**A Python-based framework that transforms image frames into coherent narratives leveraging spatial understanding and the multimodal capability of the Gemini.**


## Overview

The **Frames-to-Story-Agent** project automates the process of converting image sequences into structured stories.

This repository takes a **directory path as input**, which should contain images named in a particular order. The workflow processes the images by extracting metadata from images and leveraging language models, it generates narratives that describe the sequence's content and context.


### Requirements

- **API_KEY**: You will need an API key from Google AI Studio to run the agent. Get a free API key from [AI Studio](https://aistudio.google.com/app/apikey) and add it in the .env file


## Installation

Clone the repository:

```bash
git clone https://github.com/Nerththiga/frames-to-story-agent.git
cd frames-to-story-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```


## Usage

To run the agent with a specific directory of images:

```bash
python main.py /path/to/images
```

If no directory path is provided, the agent will use the path defined in the `.env` file.


## Project Structure

- `frames2story_agent.py`: Core workflow definition.
- `llm_client.py`: Interface for interacting with language models.
- `metadata_extractor.py`: Extracts metadata from images and saves JSON.
- `story_generator.py`: Generates a coherent story using the extracted metadata list.
- `main.py`: Initiates the workflow with a directory path.
- `.env`: Environment variables for configuration.
- `requirements.txt`: Lists Python dependencies.
