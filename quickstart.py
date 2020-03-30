#created a quickstart.py file to create container, blobs and test files in the blob . Wrote "Hello World" in that test file using this python program

import os
import uuid
import random
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlockBlobService
from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient

try:
    #Accessing Azure account using Account name and Account key
    
    block_blob_service = BlockBlobService(account_name='mcloudmesh', account_key='yo86DzS1cZaV1DHzFyjpMkwIeW2a4LbSnQREJTRdTstjaLrOubU5iaDCmuiX7xsF5jcI1iNWFpLpquA6mu1T+w==')
    print("Azure Blob storage v12 - Python quickstart sample")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "quickstart3" +  str(uuid.uuid4())
    container_client = blob_service_client.create_container(container_name)
   
    # Create a file in local Documents directory to upload and download
    
    local_path = "c:/users/hp/quickstart/data"
    local_file_name = "quickstart3" + str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()
    print("Temp file = " + upload_file_path)
    print("\nUploading to Blob storage as blob" + local_file_name)

    # Create a blob client using the local file name as the name for the blob
    
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    
    # Upload the created file
    
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)
    upload_data = b"Hello World"
    container_client.upload_blob(name="blob1", data=upload_data)
    container_client.upload_blob(name="blob2", data=upload_data)
    container_client.upload_blob(name="blob3", data=upload_data)
    
    # List the blobs in the container
    
    print("\nListing blobs...")
    generator = block_blob_service.list_blobs(container_name)
    for blob in generator:
        print("\t" + blob.name)
        
    # Download the blob to a local file
    
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
    print("\nDownloading blob to \n\t" + download_file_path)
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    print("Done")

except Exception as ex:
    print('Exception:')
    print(ex)
