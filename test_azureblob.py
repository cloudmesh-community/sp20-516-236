# created a test file to access the cloudmesh credentials from Provider.py

import cloudmesh.storage.provider.parellelazureblob.Provider as Provider
from azure.storage.blob import BlockBlobService
from Provider import Provider
p=Provider(service="azure", config="c:/users/hp/.cloudmesh/cloudmesh.yaml")
print(p.credentials)

#This successfully printed all the azure credentials from the yaml file


