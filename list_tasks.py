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

if __name__ == "__main__":
    run_task1()
