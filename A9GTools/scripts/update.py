import os
import sys
import subprocess
import argparse
import time
from git import Repo
from tqdm import tqdm # type: ignore
from itertools import cycle
from threading import Thread

class Spinner:
    def __init__(self):
        self.spinner = cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"])
        self.running = False
        self.thread = None

    def spin(self):
        while self.running:
            sys.stdout.write(next(self.spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")

    def start(self):
        self.running = True
        self.thread = Thread(target=self.spin)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write(" \b")

def fetch_repo(repo_path):
    """Realiza fetch y muestra progreso real usando la salida de git."""
    try:
        process = subprocess.Popen(
            ["git", "fetch", "origin", "master"],
            cwd=repo_path,
            stderr=subprocess.PIPE,
            text=True,
        )

        progress_bar = tqdm(desc="Downloading changes", unit="B", unit_scale=True)

        while True:
            output = process.stderr.readline()
            if not output and process.poll() is not None:
                break
            if "Receiving objects" in output:
                parts = output.split()
                for part in parts:
                    if "%" in part:
                        percent = int(part.split("%")[0])
                        progress_bar.n = percent
                        progress_bar.refresh()
            elif "MiB" in output: 
                parts = output.split()
                for part in parts:
                    if "MiB" in part and "/" in part:
                        received = float(part.split("MiB")[0])
                        total = 100  
                        progress_bar.n = received
                        progress_bar.total = total
                        progress_bar.refresh()

        progress_bar.close()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, "git fetch")

    except Exception as e:
        print(f"\nFailed to fetch: {e}")
        raise

def merge_changes(repo_path):
    """Realiza merge con un spinner para indicar actividad."""
    spinner = Spinner()
    try:
        spinner.start()
        repo = Repo(repo_path)
        repo.git.merge("origin/master")
    except Exception as e:
        print(f"\nFailed to merge: {e}")
        raise
    finally:
        spinner.stop()

def update(repo_path):
    try:
        repo = Repo(repo_path)
        assert not repo.bare

        print("Checking for updates...")
        fetch_repo(repo_path)  # Fetch con barra de progreso real

        commits_behind = len(list(repo.iter_commits("HEAD..origin/master")))
        if commits_behind:
            print(f"\nFound {commits_behind} new changes.")
            user_input = input("Do you want to update? (y/n): ").lower()
            if user_input in ["y", "yes"]:
                print("Merging changes...")
                merge_changes(repo_path)  # Merge con spinner
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