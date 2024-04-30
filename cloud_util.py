from azure_util import AzureUtility
from s3_util import S3Utility
from data_util import DataUtility
import os

class CloudUtility:
    def __init__(self, azure_client, s3_client):
        self.azure_client = azure_client
        self.s3_client = s3_client
    
    def send_and_read(self, file_name, bucket_name, object_key):
        self.s3_client.upload_to_s3(file_name, bucket_name, object_key)
        signed_url = self.s3_client.generate_signed_url(bucket_name, object_key)
        result = self.azure_client.read_document(signed_url)
        print("Document reading finished!")
        file = os.path.basename(file_name)
        file = file.replace(".", "")
        file = file.replace(" ", "")
        file += ".obj"
        success = DataUtility.serialize_object(result, file)
        # TODO: Return object file_name
        if success:
            return file
