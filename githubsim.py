import sys

def git_tutor():
    print("--- Git Logic Tutor: From Local to GitHub ---")
    print("Scenario: You've created a new Python project in a folder called 'my-app'.")
    print("Type 'help' if you get stuck.\n")

    # Step 1: Initialization
    print("STAGING 1: You want to start tracking this folder with Git.")
    answer = input("What command 'starts' or 'initializes' a repository?\n> ").strip()
    
    while "init" not in answer:
        print("Hint: It's short for 'initialize'.")
        answer = input("> ")
    print("Success: A hidden .git folder is created. Git is now watching this folder.\n")

    # Step 2: Staging
    print("STAGING 2: You've written code. Now you want to pick which files to save.")
    print("This is like putting items in a box before taping it shut.")
    answer = input("What command 'adds' files to the staging area?\n> ").strip()

    while "add" not in answer:
        print("Hint: You are 'adding' files to a list. Use '.' to add everything.")
        answer = input("> ")
    print("Success: Files are staged and ready to be recorded.\n")

    # Step 3: Committing
    print("STAGING 3: Now you want to 'save' that box. You need to give it a label.")
    print("How do you save your changes with the message 'first version'?")
    answer = input("> ").strip()

    while "commit" not in answer or "-m" not in answer:
        print("Hint: Use 'git commit -m \"your message\"'.")
        answer = input("> ")
    print("Success: You've created a snapshot! You can now travel back in time to this point.\n")

    # Step 4: The Remote Connection
    print("STAGING 4: Your code is safe on your laptop, but you want it on GitHub.")
    print("You've created a repo on GitHub. Now you need to 'connect' them.")
    print("The command looks like: git remote add origin <URL>")
    input("Press Enter once you understand that 'origin' is just a nickname for your GitHub URL.")

    # Step 5: Pushing
    print("\nFINAL STEP: You are ready to send your local snapshots to the cloud.")
    answer = input("What command 'pushes' your code to the remote server?\n> ").strip()

    if "push" in answer:
        print("\n--- MISSION COMPLETE ---")
        print("Workflow Summary:")
        print("1. git init   (The Birth)")
        print("2. git add    (The Selection)")
        print("3. git commit (The Save)")
        print("4. git push   (The Share)")
    else:
        print("Almost! It's 'git push'.")

if __name__ == "__main__":
    git_tutor()