import os
import sys
import subprocess
import argparse
from git import Repo
from tqdm import tqdm

def fetch_repo(repo):
    """Fetch updates from the remote repository."""
    try:
        origin = repo.remotes.origin
        origin.fetch()
    except Exception as e:
        print(f"Failed to fetch from origin: {e}")
        raise

def get_commits_behind(repo):
    """Get the number of commits that are behind the remote master branch."""
    try:
        return len(list(repo.iter_commits("HEAD..origin/master")))
    except Exception as e:
        print(f"Failed to get commits behind: {e}")
        raise

def pull_changes(repo_path):
    """Pull changes from the remote repository with a progress indicator."""
    try:
        # Start the git pull process
        process = subprocess.Popen(
            ["git", "pull", "origin", "master"],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Monitor the process and display progress
        with tqdm(total=100, desc="Updating", unit="%") as pbar:
            while process.poll() is None:  # While the process is running
                time.sleep(0.1)  # Simulate a small delay
                pbar.update(1)  # Increment the progress bar

        # Check the result of the process
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(f"Repository at {repo_path} has been updated successfully.")
        else:
            print(f"Failed to update the repository at {repo_path}. Error details:\n{stderr}")
    except Exception as e:
        print(f"Failed to update the repository at {repo_path}. Error details:\n{e}")
        raise

def update(repo_path):
    """Update the repository if there are new changes."""
    try:
        repo = Repo(repo_path)
        
        assert not repo.bare

        fetch_repo(repo)

        commits_behind = get_commits_behind(repo)

        if commits_behind:
            print(f"There are {commits_behind} new changes pending.")
            user_input = input("Do you want to update the repository? (y/n): ").strip().lower()
            if user_input in ["y", "yes"]:
                print("Updating the repository...")
                pull_changes(repo_path)
            else:
                print("Update cancelled by the user.")
        else:
            print("No changes to pull.")
    except Exception as e:
        print(f"Failed to update the repository at {repo_path}. Error: {e}")

def main():
    """Main function to handle command-line arguments and execute the update."""
    parser = argparse.ArgumentParser(
        description="A9GTools_Updater is a simple program to update A9Gtools through the https://github.com/dezamora98/CSDTK42"
    )
    parser.add_argument("-v", "--version", action="version", version="A9GTools_Updater BETA-0.0.1")
    parser.add_argument("-p", "--path", default=os.getenv("GPRS_CSDTK42_PATH"), help="Path to CSDTK directory")

    args = parser.parse_args(sys.argv[1:])

    if not os.path.exists(args.path) or args.path is None:
        print("CSDTK repository path is not correct")
        return
    update(args.path)

if __name__ == "__main__":
    main()