from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

google_auth = GoogleAuth()
drive_app = GoogleDrive(google_auth)

upload_list = ['1.txt','2.txt','3.txt']

for file_to_upload in upload_list:
    file = drive_app.CreateFile({'parents': [{'id': ""}]})
    file.SetContentFile(file_to_upload)
    file.Upload()

