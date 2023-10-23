import list_tasks as LT

def menu_and_input():
    print("Please select a direction:")
    steps = LT.directions()

    for index in range(0, len(steps), 1):
        print(f"{index+1} - {steps[index]}")
    print()
    usr_response = int(input()) - 1
    return steps[usr_response]

def run_task4():
    route = []
    print("Working out escape route...")
    for i in range(5):
        route.append(menu_and_input())
    print(f"Escape route:{route}")

if __name__ == "__main__":
    run_task4()

