from file_manager import FileManager

print(FileManager("/home/grzegorz/aplikacje-www/pythontut2/plik.txt").read_file())
FileManager("/home/grzegorz/aplikacje-www/pythontut2/plik.txt").update_file(" i tyle")
print(FileManager("/home/grzegorz/aplikacje-www/pythontut2/plik.txt").read_file())