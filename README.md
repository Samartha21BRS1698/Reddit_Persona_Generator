# Reddit_Persona_Generator

A Python project that scrapes public Reddit user data (posts and comments) and uses a local open-source language model (flan-t5-large) to generate a psychological persona for that user.

## Features
 Scrapes up to 50 Reddit posts and 50 comments from a public Reddit user

 Uses a locally run HuggingFace model (distilgpt2) to generate the user's persona

 Works fully offline (after initial model download)

 Outputs structured data with insights like:

Name, Age, Occupation

Behaviors, Goals, Frustrations

Archetype, Tier, Motivations, Personality

## Project Structure

```bash
Reddit_Persona_Generator/
├── main.py
├── reddit_scraper.py
├── llm_persona_generator.py
├── prompts/
│   └── persona_prompt.txt
├── output/
│   └── {username}_raw_data.txt
│   └── {username}_persona.txt
├── .env
├── requirements.txt
└── README.md 
```

## Installation

1. Clone the repo
```bash
git clone https://github.com/yourusername/Reddit_Persona_Generator.git
cd Reddit_Persona_Generator
```
2. Create a virtual environment
```bash

python -m venv venv
venv\Scripts\activate  # on Windows
# OR
source venv/bin/activate  # on macOS/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```


## Configuration
Create a .env file in the root directory:
```bash
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=RedditPersonaGen/0.0.1
```
Get these credentials by registering an app at https://www.reddit.com/prefs/apps

## Usage
```bash
python main.py
```
When prompted, enter a Reddit profile URL like:

```bash
https://www.reddit.com/user/kojied/
```
The script will:

-> Fetch their public posts and comments

-> Save raw data to output/{username}_raw_data.txt

-> Generate a structured persona with LLM and save it to output/{username}_persona.txt


##  Persona Template

```text 
Based on the following Reddit posts and comments, generate a structured user persona including:

- Name
- Age
- Occupation
- Status
- Location
- Tier
- Archetype
- Behaviors & Habits
- Goals & Needs
- Motivations
- Frustrations
- Personality

Here is the data:
{REDDIT_DATA}
```

##  Example Output
## Input:
https://www.reddit.com/user/Ok_Remote_3322/

## Output
 in output/Ok_Remote_3322_persona.txt:

**Name:** CheongSeon  
**Age:** ~25  
**Occupation:** Early professional  
**Status:** (undisclosed)  
**Location:** India  

---

### 🧠 Behaviors & Habits
- Active in cricket discussions  
- Enjoys gym workouts and music  
- Shares insights and emotional stories

...

### 🧬 Personality
- Emotional, passionate, community-oriented  
- Balanced between fitness and leisure


##  Technologies Used
Python 3.x

PRAW (Reddit API Wrapper)

Transformers (Hugging Face)

DistilGPT2

Torch (PyTorch)

dotenv

## FAQ
 • Can I change the LLM?
Yes. Just modify the model in llm_persona_generator.py. You can try gpt2, gpt2-medium, or fine-tuned LLMs too.

 • Can I run this without internet?
Yes. Once the HuggingFace model is downloaded, everything works offline.

 • Does it support multiple profiles in one run?
Currently no. It processes one user at a time.

## To-Do
 Add GUI with Streamlit

 Export persona to PDF

 Add support for OpenRouter or LM Studio

 Add sarcasm/tone classification

## Author

**Samartha**  
B.Tech student 
 
 MySQL • AI/ML • Data Science •  NLP • Google Cloud 
 
 [LinkedIn](https://www.linkedin.com/in/samartha-b0154a293) | [GitHub](https://github.com/Samartha21BRS1698)

## License
 MIT License © 2025 Samartha