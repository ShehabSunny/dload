import ftplib
import socket
import glob
import os

def main():
    host = "localhost"
    port = 1026
    FILENAME = 'README'
    try:
        ftp = ftplib.FTP(source_address=(host, port))
        ftp.login()  
    except Exception as e:  
        print(f"could not connect {str(e)}")
    else:
        print("connected")
    # with ftplib.FTP(source_address=(host, port), FTP_LOGIN, FTP_PASSWD) as ftp:

    # try:
    #     ftp.cwd('CV Select')
    # except ftplib.error_perm: 
    #     print("can not cd into dir")
    # else:
    #     print("cd done")
    for image in glob.glob(os.path.join('/home/sunny/Downloads/p')):
        with open(image, 'wb') as f:
            ftp.storbinary('RETR ' + FILENAME, f.write)
    ftp.quit()

if __name__ == "__main__":
    main()