import boto3

class S3Utility:
    # TODO: Add error handling if credentials are invalid
    def __init__(self, access_key_id, secret_access_key, region):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.region = region

        # Set AWS credentials and region 
        boto3.setup_default_session(
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key, 
            region_name=self.region
        )

        self.s3_client = boto3.client('s3')
    
    # TODO: Add error handling for if file does not exust etc.
    def upload_to_s3(self, file_path, bucket_name, object_key):
        # Upload file
        self.s3_client.upload_file(file_path, bucket_name, object_key)
        print("Uploading...")

        # Wait until the object exists in the bucket
        waiter = self.s3_client.get_waiter("object_exists")
        waiter.wait(Bucket=bucket_name, Key=object_key)
        print("Upload complete!")

        # Construct and return the URL of the uploaded file
        url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"
        return url

    # TODO: Add error handling for if bucket / file doesn't exist
    def generate_signed_url(self, bucket_name, object_key, expiration_time=180):
        print("Generating signed URL...")
        # Generate and return signed URL
        signed_url = self.s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=expiration_time
        )
        return signed_url