import sys
import time
import os

def clear_screen():
    # Clears terminal for Windows (nt) or Linux/macOS (posix)
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, delay=0.03):
    """Prints text character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # New line at the end

def git_tutor():
    clear_screen()
    
    typewriter_print("--- Git Conceptual Tutor ---")
    typewriter_print("Goal: Understand the workflow of getting code from your PC to GitHub.")
    print("-" * 30)

    # Step 1: Initialization
    typewriter_print("\nSCENARIO 1: You have a folder full of code, but Git isn't 'watching' it yet.")
    typewriter_print("You need to create the hidden '.git' folder that tracks your history.")
    
    while True:
        answer = input("\nWhat command initializes a new repository?\n> ").strip().lower()
        if "git init" in answer:
            typewriter_print("CORRECT. You just turned a regular folder into a Git Repository.")
            break
        else:
            typewriter_print("Hint: It starts with 'git' and ends with a word meaning 'start' or 'initialize'.")

    # Step 2: The Staging Area
    typewriter_print("\nSCENARIO 2: You've edited 3 files. You only want to save 2 of them for now.")
    typewriter_print("Before you 'save' a snapshot, you must move files to the 'Staging Area'.")
    
    

    while True:
        answer = input("\nWhat command 'adds' files to the staging area?\n> ").strip().lower()
        if "git add" in answer:
            typewriter_print("EXACTLY. Think of 'git add' as putting items in a box before you tape it shut.")
            break
        else:
            typewriter_print("Hint: You are 'adding' files to the index.")

    # Step 3: The Commit
    typewriter_print("\nSCENARIO 3: Your box is packed (staged). Now you need to tape it shut and label it.")
    typewriter_print("This creates a permanent snapshot in your project's history.")
    
    while True:
        answer = input("\nHow do you 'commit' your changes with a message?\n> ").strip().lower()
        if "git commit" in answer and "-m" in answer:
            typewriter_print("SUCCESS. The '-m' stands for message. Without a label, you'd never find this version again!")
            break
        else:
            typewriter_print("Hint: You need 'git commit' and the flag '-m' followed by your message in quotes.")

    # Step 4: The Remote
    typewriter_print("\nSCENARIO 4: Your snapshots are safe on your laptop, but your laptop could break.")
    typewriter_print("You want to link your local folder to a repository on GitHub.")
    typewriter_print("We call this remote link 'origin' by default.")
    
    typewriter_print("\nCommand: git remote add origin <URL>")
    input("\n(Press Enter once you've visualized 'origin' as a bridge to GitHub...)")

    # Step 5: The Push
    typewriter_print("\nFINAL SCENARIO: Time to send your local snapshots across that bridge.")
    
    while True:
        answer = input("\nWhat command 'pushes' your work to GitHub?\n> ").strip().lower()
        if "git push" in answer:
            typewriter_print("\n--- TUTORIAL COMPLETE ---")
            typewriter_print("You now have the fundamental 'Golden Path':")
            typewriter_print("1. init   -> Create the repo")
            typewriter_print("2. add    -> Pick the changes")
            typewriter_print("3. commit -> Save the snapshot")
            typewriter_print("4. push   -> Share with the world")
            break
        else:
            typewriter_print("Hint: You are 'pushing' the code up to the server.")

if __name__ == "__main__":
    git_tutor()