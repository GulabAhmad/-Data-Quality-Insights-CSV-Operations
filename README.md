# Sales Data Quality & CSV Operations

Student name: Gulab Ahmad (confirm before submission)
Training ID: **ADD YOUR TRAINING ID**
GitHub repository: **ADD YOUR ACTUAL REPOSITORY URL**

## Run

Keep the supplied CSV beside `sales_assignment.ipynb`. Open the notebook in Jupyter and run all cells from top to bottom with Python 3. Install dependencies with `pip install -r requirements.txt` if needed. In Google Colab, upload `sales_raw.csv` to the session's working directory before running the notebook. All data paths are relative.

The notebook contains both marked parts, displayed inspection results, cleaning explanations, two charts, two findings, and checks of the saved outputs. The original CSV is preserved. Running all cells regenerates the output CSVs, charts, summaries, and findings.

Cleaning removes exact duplicates and rows with invalid/missing dates or nonpositive/missing numeric sales fields. Text is standardized; missing region becomes Unknown. The unusual 10,000 price is retained with its effect disclosed in the findings. No currency was specified.

Part B reloads the cleaned CSV, adds 5% tax, increases Books prices by 10%, recalculates revenue and tax, deletes transaction 1002 to demonstrate row removal, creates then drops review_status, and saves and reloads sales_updated.csv.

## Submission

Replace the training ID and repository URL above, confirm your name, and maintain meaningful commits in your own GitHub repository. Repackage the required files after updating this README, rename the archive to your actual `StudentName_TrainingID.zip`, and upload the ZIP before your portal deadline. The current ZIP filename is a placeholder. No repository has been created or uploaded by this assignment script.
