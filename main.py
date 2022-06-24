import os
import shutil

extensions = ['.jpg', '.png', '.jpeg', '.mp4', '.mp3', '.wav', '.zip', '.rar', '.xlsx', '.pptx', '.pdf']
SESSION = os.getlogin()
DESKTOP_PATH = f"C:/Users/{SESSION}/Desktop/"
DOWNLOAD_PATH = f"C:/Users/{SESSION}/Downloads"


def create_desktop_folder(desktop_path):
    file_path = desktop_path + 'Sorted Files'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    else:
        pass
    return file_path + '/'


class Delete_files():
    def __init__(self, extension):
        self.extension = extension


    def delete_files(self, file_path, DOWLOAD_PATH):
        path = file_path + self.extension + '/'
        if not os.path.exists(path):
            os.mkdir(path)

        for a in os.listdir(DOWLOAD_PATH):
            if a.endswith(self.extension):
                remove_path = '{}/{}'.format(DOWLOAD_PATH, a)
                a = '{}/{}'.format(DOWLOAD_PATH, a)
                shutil.move(a, path)
                try:
                    os.remove(remove_path)
                except Exception:
                    pass


if __name__ == '__main__':
    file_path = create_desktop_folder(DESKTOP_PATH)
    for a in range(len(extensions)):
        delete_files = Delete_files(extensions[a])
        delete_files.delete_files(file_path, DOWNLOAD_PATH)