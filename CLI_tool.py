import os  # using for manipulating the path address.

import boto3  # AWS SDK - to create, configure, and manage AWS services such as S3.
from botocore.exceptions import ClientError  # using for handling exceptions in boto3

# Boto3 needs to know which services will be used
s3 = boto3.resource('s3')
client = boto3.client('s3')


# ----------Functions----------
def printHelp():
    print("add           Adding new bucket/object to bucket")
    print("delete        Deleting an existing bucket/object")
    print("list          Listing all buckets/objects")
    print("exit          Exit the CLI")


def getTypeInput():
    # Handling user input for the command type (bucket or object)
    print("Would you like to run the command on bucket or object?")
    print(">>>", end="")
    type_input = input()
    type_input = type_input.strip().lower()
    while (type_input != 'bucket') and (type_input != 'object'):
        print("Type 'bucket' or 'object' ")
        print(">>>", end="")
        type_input = input()
        type_input = type_input.strip().lower()

    return type_input


# ----------Buckets Operations Functions----------
def addBucket():
    print("Enter the new bucket name: (Attention: if bucket's name is already exist, the bucket will not be created!)")
    new_bucket_name = input()
    try:
        result = s3.create_bucket(Bucket=new_bucket_name)
        print(f"{new_bucket_name} has been successfully created!")
    except Exception as e:
        raise Exception(e.__str__())


def listAllBuckets():
    print("All buckets in your S3 directory are:")
    for bucket in s3.buckets.all():
        print("• " + bucket.name)


def deleteBucket():
    delete_bucket_name = getBucketName()
    try:
        response = s3.Bucket(delete_bucket_name).delete()
        print(f"{delete_bucket_name} has been successfully deleted!")
    except Exception as e:
        raise Exception(e.__str__())


def getBucketName():
    is_bucket_not_found = True
    while is_bucket_not_found:
        print("Enter the bucket name:")
        print(">>>", end="")
        bucket_name = input()
        if isBucketInS3(bucket_name):
            is_bucket_not_found = False
        else:
            print("This bucket was not found, try again\n")

    return bucket_name


def isBucketInS3(i_bucket_name):
    for curr_bucket in s3.buckets.all():
        if i_bucket_name == curr_bucket.name:
            return True

    return False


# ----------Objects Operations Functions----------
def isObjectInBucket(i_object_key, i_bucket):
    for curr_object in i_bucket.objects.all():
        if i_object_key == curr_object.key:
            return True

    return False


def addObject(i_curr_bucket):
    print("Enter the new object path (full address to the file, with it's extension type):")
    print(">>>", end="")
    new_object_path = input()  # e.g C:/Users/tal/OneDrive/photos/Screenshot (1).png
    new_object_path = new_object_path.replace('\\', '/')  # switching all \ to / like the example above.
    new_object_name = os.path.basename(new_object_path)  # extracting the file name with his extension
    # (e.g: Screenshot (1).png)

    try:
        result = s3.Bucket(i_curr_bucket.name).upload_file(new_object_path, new_object_name)
        print(f"{new_object_name} has been successfully added to {i_curr_bucket.name} bucket!")
    except Exception as e:
        raise Exception(e.__str__())


def listObjects(i_curr_bucket):
    print(f"All objects in {i_curr_bucket.name} are:")
    for curr_bucket_object in i_curr_bucket.objects.all():
        print("• " + curr_bucket_object.key)


def deleteObject(i_curr_bucket):
    flag = True
    while flag:
        print("Enter the object key(path) which inside the bucket:")
        print(">>>", end="")
        object_name = input()

        if isObjectInBucket(object_name, i_curr_bucket):
            try:
                result = client.delete_object(
                    Bucket=i_curr_bucket.name,
                    Key=object_name,
                )
            except ClientError as e:
                raise Exception(e.__str__())
            except Exception as e:
                raise Exception(e.__str__())

            print(f"{object_name} has been successfully deleted from {i_curr_bucket.name} bucket")
            flag = False
        else:
            print("Object file does not found! try again...\n")


# ----------"Main"----------
print("\nWelcome to Tal's S3 CLI \nFor seeing all S3 buckets operations commands type --help \n")
s3_operations = {'add', 'list', 'delete'}

runFlag = True
while runFlag:  # CLI running till command 'exit' typed.
    print(">>>", end="")
    user_command_input = input()
    user_command_input = user_command_input.strip().lower()  # strip to ignoring white spaces at the start/end of the input string.

    if user_command_input == "":
        continue
    if user_command_input == '--help':
        printHelp()
    elif user_command_input == 'exit':
        runFlag = False
    elif user_command_input in s3_operations:
        user_type_input = getTypeInput()
        if user_type_input == 'object':
            currBucket = s3.Bucket(getBucketName())  # e.g bucket_name = "mybucket-tal-test2323423422"
        try:
            if user_command_input == 'add':
                addBucket() if user_type_input == 'bucket' else addObject(currBucket)

            elif user_command_input == 'list':
                listAllBuckets() if user_type_input == 'bucket' else listObjects(currBucket)

            elif user_command_input == 'delete':
                deleteBucket() if user_type_input == 'bucket' else deleteObject(currBucket)

        except Exception as e:
            pass  # avoid from close the program.
            print("Command Failed with the exception: " + e.__str__())
    else:
        print("Command does not exist!\n")
