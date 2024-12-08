def load_words(file_path):
    #read words from a file and make them a list
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]