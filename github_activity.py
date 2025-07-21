import sys

def main():
    if len(sys.argv) < 2:
        print("❗ Usage: python github_activity.py <github_username>")
        return

    username = sys.argv[1]
    print(f"🔍 You entered GitHub username: {username}")

if __name__ == "__main__":
    main()
