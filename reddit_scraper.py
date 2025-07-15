# code for Reddit Scraper

import praw
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def scrape_reddit_user(username: str, limit: int = 50):
    try:
        user = reddit.redditor(username)
        posts = []
        comments = []

        print(f"Fetching posts and comments for u/{username}...")

        for submission in tqdm(user.submissions.new(limit=limit), desc="Posts"):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "url": submission.url,
                "subreddit": submission.subreddit.display_name
            })

        for comment in tqdm(user.comments.new(limit=limit), desc="Comments"):
            comments.append({
                "body": comment.body,
                "subreddit": comment.subreddit.display_name,
                "link": f"https://www.reddit.com{comment.permalink}"
            })

        print(f"Retrieved {len(posts)} posts and {len(comments)} comments.")
        return posts, comments

    except Exception as e:
        print(f"Error: {e}")
        return [], []
