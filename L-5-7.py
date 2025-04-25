# Stack implementation using a list
stack = []

# Menu-driven interface
while True:
    print("\nStack Operations Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if stack is empty")
    print("5. Display stack")
    print("6. Exit")
    
    # L-5-7
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = int(input("Enter the item to push: "))
        stack.append(item)  
        print(f"{item} has been pushed to the stack.")
    
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty. Cannot pop.")
        else:
            item = stack.pop()  
            print(f"{item} has been popped from the stack.")
    
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print(f"Top element of the stack is: {stack[-1]}")  
    
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
    
    elif choice == 5:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements:", stack)  
    
    elif choice == 6:
        print("Exiting the program.")
        break  
    
    else:
        print("Invalid choice! Please try again.")
