import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            events = json.loads(data)
            return events
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"❌ URL Error: {e.reason}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    return []

def main():
    if len(sys.argv) < 2:
        print("❗ Usage: python github_activity.py <github_username>")
        return

    username = sys.argv[1]
    print(f"📡 Fetching activity for GitHub user: {username}...")

    events = fetch_github_activity(username)
    if not events:
        print("😕 No public activity found or an error occurred.")
        return

    print("📋 Recent Activity:")
    for event in events:
        type = event["type"]
        repo = event["repo"]["name"]

        if type == "PushEvent":
            commits = event["payload"]["commits"]
            print(f"📌 Pushed {len(commits)} commit(s) to {repo}")

        elif type == "IssuesEvent":
            action = event["payload"]["action"]
            print(f"🐛 {action.capitalize()} issue in {repo}")

        elif type == "IssueCommentEvent":
            print(f"💬 Commented on issue in {repo}")

        elif type == "WatchEvent":
            print(f"⭐ Starred {repo}")

        elif type == "PullRequestEvent":
            action = event["payload"]["action"]
            print(f"🔀 {action.capitalize()} pull request in {repo}")

        elif type == "CreateEvent":
            ref_type = event["payload"]["ref_type"]
            print(f"📁 Created new {ref_type} in {repo}")

        else:
            print(f"📦 {type} in {repo}")


if __name__ == "__main__":
    main()
