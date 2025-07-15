# main.py

from reddit_scraper import scrape_reddit_user
from llm_persona_generator import call_llm
import os

def save_output(posts, comments, username):
    os.makedirs("output", exist_ok=True)
    raw_filename = f"output/{username}_raw_data.txt"
    
    with open(raw_filename, "w", encoding="utf-8") as f:
        f.write("USER POSTS:\n\n")
        for post in posts:
            f.write(f"Title: {post['title']}\nBody: {post['body']}\nSubreddit: {post['subreddit']}\nURL: {post['url']}\n---\n")

        f.write("\n\nUSER COMMENTS:\n\n")
        for comment in comments:
            f.write(f"Comment: {comment['body']}\nSubreddit: {comment['subreddit']}\nLink: {comment['link']}\n---\n")

    print(f"📄 Raw data saved to {raw_filename}")
    return raw_filename

def generate_persona(raw_file_path, username):
    with open("prompts/persona_prompt.txt", "r", encoding="utf-8") as f:
        base_prompt = f.read()

    with open(raw_file_path, "r", encoding="utf-8") as f:
        reddit_data = f.read()

    print(f"🧪 Reddit data length: {len(reddit_data)} characters")

    if len(reddit_data) > 3000:
        print("⚠️ Trimming Reddit content to 3000 characters for LLM...")
    final_prompt = base_prompt.replace("{REDDIT_DATA}", reddit_data[:3000])

    print("🧠 Generating persona using LLM...")
    persona_text = call_llm(final_prompt)

    print("\n📝 GENERATED PERSONA:\n", persona_text)

    output_file = f"output/{username}_persona.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(persona_text)
        print(f"✅ Persona saved to {output_file}")
    except Exception as e:
        print(f"❌ Could not save persona: {e}")

if __name__ == "__main__":
    reddit_profile_url = input("🔗 Enter Reddit profile URL (e.g., https://www.reddit.com/user/kojied/): ").strip()
    username = reddit_profile_url.rstrip("/").split("/")[-1]

    posts, comments = scrape_reddit_user(username)
    if posts or comments:
        raw_file = save_output(posts, comments, username)
        generate_persona(raw_file, username)
    else:
        print("⚠️ No data scraped.")
