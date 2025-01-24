from ftplib import FTP

SERVER_IP = '127.0.0.1'
SERVER_PORT = 21

# TODO Create a user that have only upload permissions
FTP_USER = 'dori'
FTP_PASSWORD = 'avmybaby'


def upload_file(file_path: str):
    ftp = FTP()
    ftp.connect(SERVER_IP, SERVER_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)

    local_file = file_path
    remote_file = 'file.txt'  # ??

    with open(local_file, 'rb') as f:
        ftp.storbinary(f"STOR {remote_file}", f)

    print(f"File '{local_file}' uploaded successfully.")

    ftp.quit()
