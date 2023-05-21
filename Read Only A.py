with open('sample.txt', 'r') as file:
    for line in file:
        if line.startswith('A'):
            print(line.strip()) 
