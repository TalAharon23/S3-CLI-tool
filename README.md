# S3-CLI-tool

## Introduction:
This project is a CLI tool for S3 operations 
It made in order to enable execution of quick commands without having to go to the AWS website and designed for an accessible replacement for other CLIs.

## What the CLI contain?
•	Three S3 operations on objects and buckets: add, list and delete.
  In addition: Help menu (`--help` command). Exit option (`exit` command).
     
•	Checking if bucket or object was found in S3 directory and notify user if not.

•	Detecting errors from boto3 library if occurred during the execute of the operations by using try/except to handling the error.

•	Handling small details that may cause errors or inconvenience to the user:
-	Changing the left slashes into right slashes at the add command (boto 3 requirement).
-	Delete spaces in the command input.

## Running steps:
Step 1: Get your aws-s3 bucket credentials.

Here's what you'll need:
-	Access Key
-	Secret key
-	Endpoint URL

Step 2: follow those marks:

1) Install boto3 if does not installed on your work environment:
  * Open the Terminal and run:  `pip install boto3`

2) Configure your AWS account by using the step 1 credentials:
  * Open the Terminal and run: `aws configure`

Step 3:  Use the CLI as your wish.
