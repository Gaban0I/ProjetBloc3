
import os
import subprocess
import sys

def run_command(command):
    """Runs a command, prints its output, and checks for errors."""
    print(f"\nExecuting: {' '.join(command)}")
    # Use Popen to stream output in real-time
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
    
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            
    if process.returncode != 0:
        print(f"\n--- ERROR: Command failed with exit code {process.returncode} ---", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to run the entire data science pipeline.
    It executes the data preparation script and then the Jupyter notebooks in order.
    """
    print("--- Starting the project pipeline ---")

    # --- Step 1: Prepare Data ---
    print("\n>>> Step 1: Running data preparation script <<<")
    prepare_script_path = os.path.join("src", "prepare_data.py")
    run_command([sys.executable, prepare_script_path])
    print(">>> Data preparation complete <<<")

    # --- Step 2: Run Notebooks ---
    notebooks = [
        os.path.join("notebooks", "1_-_Analyse_Exploratoire.ipynb"),
        os.path.join("notebooks", "2_-_Feature_Engineering.ipynb"),
        os.path.join("notebooks", "3_-_Modelisation.ipynb"),
        os.path.join("notebooks", "4_-_Presentation_des_Resultats.ipynb")
    ]

    print("\n>>> Step 2: Executing Jupyter notebooks <<<")
    for notebook in notebooks:
        run_command([
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute", notebook,
            "--inplace",
            "--allow-errors" # Continue even if a cell fails, but the script will still exit on command failure
        ])
        print(f">>> Finished executing: {notebook} <<<")

    print("\n--- Pipeline finished successfully! ---")


if __name__ == "__main__":
    # Check if jupyter is installed/available
    try:
        run_command(["jupyter", "--version"])
    except FileNotFoundError:
        print("Error: 'jupyter' command not found.", file=sys.stderr)
        print("Please ensure Jupyter is installed and in your system's PATH.", file=sys.stderr)
        sys.exit(1)

    main()
