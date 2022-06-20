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

## Running examples:
#### Help: `--help`
![image](https://user-images.githubusercontent.com/82831070/174570726-ce103bf3-abf5-435c-a402-db2e9aad65ec.png)

#### Add buckets/objects: `add`
##### Buckets:
###### My buckets list (empty):
![image](https://user-images.githubusercontent.com/82831070/174571282-30e78921-95b7-480e-8053-688fb559f780.png)
###### After following the commands (and a lot of time to get unique name for my bucket):
![image](https://user-images.githubusercontent.com/82831070/174573392-6a169e19-71d9-4919-8be7-b64f94865100.png)
###### My current buckets list:
![image](https://user-images.githubusercontent.com/82831070/174573582-ce9ac6c5-a814-44cb-b05b-0a4c1dc8a029.png)
##### Objects:
###### My objects list (empty):
![image](https://user-images.githubusercontent.com/82831070/174574074-df843b70-85ba-4b93-8a8c-3e1c140405ac.png)
###### After following the commands:
![image](https://user-images.githubusercontent.com/82831070/174574801-b94da18e-6378-4fa0-acc3-6b8aa0d200ab.png)
###### My current objects list:
![image](https://user-images.githubusercontent.com/82831070/174574881-9a8836ad-86b1-4f05-8c59-a1331a44b6d5.png)

#### List buckets/objects: `list`
![image](https://user-images.githubusercontent.com/82831070/174579210-21f665e1-4afc-4984-9ef1-3c308f559168.png)

#### Delete buckets/objects: `delete`
![image](https://user-images.githubusercontent.com/82831070/174579686-92ead5c5-9aba-42ca-9315-9ee4c5e9f49b.png)



