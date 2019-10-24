class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_file(self):
        handle = open(r''+self.file_name, 'r')
        data = handle.read()
        handle.close()
        return data

    def update_file(self, text_data):
        data = self.read_file()
        handle = open(r''+self.file_name, 'w')
        handle.write(data+text_data)
        handle.close()