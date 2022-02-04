from os import access
import dropbox

class CloudStorage():
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, source, destination):
        dbx = dropbox.Dropbox(self.access_token)
        s = open(source,'rb')
        dbx.files_upload(s.read(),destination)

def main():
    access_token = "rvsMo7oI5eIAAAAAAAAAAR_RD9xBLDEocxa9ilj1WuE31CU2ZZMhP2hRbjOQydY1"
    transferData = CloudStorage(access_token)
    source = input("enter the file you want to transfer: ")
    destination = input("enter the path to upload to dropbox: ")

    transferData.uploadFiles(source, destination)

    print("file has been uploaded successfully!")

main()