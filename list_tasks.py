def directions():
    list = []
    list.append("Move Forward")
    list.append("Move Backward")
    list.append("Turn Left")
    list.append("Turn Right")
    return list
def run_task1():
    list = directions()
    print(list)

def run_task2():
    print("Moving...")
    path = movements()
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")

def run_task3():
    menu()
def movements():
    path = ["Move Forward", 10 , "Move Backward" , 5 ,"Move Left", 3 , "Move Right", 1]
    return path

def menu():
    print("Please select a direction")
    steps = directions()
    for i in range(0,len(steps), 1):
        print(f"{i+1} - {steps[i]}")


if __name__ == "__main__":
    run_task3()

    # for index in range(len(path)):
    #     posit = path[index]
    #     print(f"{posit} is at index {index}")
