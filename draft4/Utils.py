import os
# """ Library that contains helper functions """

class FileReader():
    # """Library of util functions to handle files being transferred through the network"""
    def __init__(self, filename):
        self.filename = filename
        self.filepath = os.path.abspath(self.filename);

    def get_file_size(self):
    # """Takes in a file name and returns the size in bytes"""
        file_size = os.path.getsize(self.filepath);
        return file_size


    def get_file_bytes(self):
    # """Returns a bytes array of the file that can be sent"""
        byteContent = b""
        with open(self.filepath,'rb') as file:
            byteContent += file.read()
        return byteContent

class DirectoryReader():
    # """Helper library to handle the directories linked to the P2P network"""
    def __init__(self, shared_dir):
        self.shared_dir = shared_dir

    def list_file_names(self):
        file_NameList = os.listdir(self.shared_dir)
        return file_NameList
