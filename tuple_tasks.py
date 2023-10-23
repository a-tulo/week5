def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods)

def likelihood_min_max():
    likelihoods = (50,38,27,99,4)
    min_likelihood = min(likelihoods)
    max_likelihood = max(likelihoods)
    return (min_likelihood,max_likelihood)
def run_task1():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value}% ")

def run_task2():
    likelihoods = likelihood_min_max()
    print(f"Minimum likelihood of falling: {likelihoods[0]}%")
    print(f"Maximum likelihood of falling: {likelihoods[1]}%")

if __name__ == "__main__":
    run_task2()
