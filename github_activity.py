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
    print(f"✅ Total events fetched: {len(events)}")

if __name__ == "__main__":
    main()
