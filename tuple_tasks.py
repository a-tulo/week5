def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods)

def likelihood_min_max():
    likelihoods = (50,38,27,99,4)
    min_likelihood = min(likelihoods)
    max_likelihood = max(likelihoods)
    return (min_likelihood,max_likelihood)

def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods

def run_task1():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value}% ")
def run_task2():
    likelihoods = likelihood_min_max()
    print(f"Minimum likelihood of falling: {likelihoods[0]}%")
    print(f"Maximum likelihood of falling: {likelihoods[1]}%")

def run_task3():
    likelihoods = steps()
    good_steps = []
    bad_steps = []

    for item in likelihoods:
        if item[1] >= 50:
            bad_steps.append(item)
        else:
            good_steps.append(item)

    print(f"Good steps: {len(good_steps)} , Bad steps: {len(bad_steps)}")
if __name__ == "__main__":
    run_task3()
