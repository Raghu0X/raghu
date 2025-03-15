with open('output.txt', 'a') as file:
    user_input = input("Enter text to append to the file: ")
    
    file.write(user_input + '\n')  

print("Your input has been appended to 'output.txt'.")
