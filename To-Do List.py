print("Welcome to your To-Do List, here's what you have to do:")
count = 1

with open ("to-do.txt", "r") as file:
    for line in file:
        print(str(count) + ". " + line.strip())
        count+=1


print ("What would you like to add (Enter 'q' to exit)?: ")
num = 1
with open ("to-do.txt", "w") as file:
    while True:
        line = input(str(num) + ": ")
        
        if line == 'q':
            break

        file.write(line + "\n")
        num+=1
    print("Successfully written to file!")