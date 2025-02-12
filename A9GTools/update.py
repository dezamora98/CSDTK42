import os
import argparse
from git import Repo
from utils import Spinner

def fetch_repo(repo, spinner):
    try:
        spinner.start()
        repo.remotes.origin.fetch()
    except Exception as e:
        print(f"\nFailed to fetch: {e}")
        raise
    finally:
        spinner.stop()

def merge_changes(repo, spinner):
    try:
        spinner.start()
        repo.git.merge("origin/master")
    except Exception as e:
        print(f"\nFailed to merge: {e}")
        raise
    finally:
        spinner.stop()

def update(repo_path):
    spinner = Spinner()
    try:
        repo = Repo(repo_path)
        assert not repo.bare

        print("Checking for updates...")
        fetch_repo(repo, spinner)  # Fetch con spinner

        commits_behind = len(list(repo.iter_commits("HEAD..origin/master")))
        if commits_behind:
            print(f"\nFound {commits_behind} new changes.")
            user_input = input("Do you want to update? (y/n): ").lower()
            if user_input in ["y", "yes"]:
                print("Merging changes...")
                merge_changes(repo, spinner)  # Merge con el mismo spinner
                print("\nUpdate completed successfully!")
            else:
                print("Update cancelled.")
        else:
            print("Already up to date.")

    except Exception as e:
        print(f"\nError: {e}")

def main():
    parser = argparse.ArgumentParser(description="Update tool for A9GTools")
    parser.add_argument("-p", "--path", default=os.getenv("GPRS_CSDTK42_PATH"), help="Path to repository")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("Invalid repository path!")
        return

    update(args.path)

if __name__ == "__main__":
    main()
