# Queue implementation using a list
queue = []

# Menu-driven interface
while True:
    print("\nQueue Operations Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if queue is empty")
    print("5. Display queue")
    print("6. Exit")
    
    # L-5-8
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = int(input("Enter the item to enqueue: "))
        queue.append(item)  
        print(f"{item} has been added to the queue.")
    
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty. Cannot dequeue.")
        else:
            item = queue.pop(0)  
            print(f"{item} has been dequeued from the queue.")
    
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print(f"Front element of the queue is: {queue[0]}")  
    
    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue is not empty.")
    
    elif choice == 5:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", queue)  
    
    elif choice == 6:
        print("Exiting the program.")
        break  
    
    else:
        print("Invalid choice! Please try again.")
