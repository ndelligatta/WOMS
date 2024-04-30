from s3_util import S3Utility
from azure_util import AzureUtility
from data_util import DataUtility as util
from cloud_util import CloudUtility


if __name__ == "__main__":
    ## Step 1

    # Connect to AWS
    aws_access_key_id = "xxxxxxxxxxxxxxxx"
    aws_secret_access_key = "xxxxxxxxxxxx"
    aws_region = "us-west-1"
    s3_client = S3Utility(aws_access_key_id, aws_secret_access_key, aws_region)

    # Connect to Azure AI Reader
    endpoint = "xxxxxxxxxxxxxxx"
    key = "xxxxxxxxxxxxxx"
    azure_client = AzureUtility(endpoint, key)

    # Send file and read
    file_name = "/Users/nolandelligatta/Downloads/test_spread.pdf"
    bucket_name = "womsdataa"
    object_key = "DEMO_TEST.pdf"
    cloud = CloudUtility(azure_client, s3_client)
    file = cloud.send_and_read(file_name, bucket_name, object_key)
    print(file)

    ## Preview of Step 2
    result = util.deserialize_object(f"/Users/nolandelligatta/Documents/Mike's Program/{file}")
    table = result.tables[0]
    df = util.get_dataframe(table)
    print(df)