from matplotlib import pyplot as plt

def plot_helper(data, **kwargs):
    plt.plot(data, **kwargs)
    plt.grid()
    plt.title('My Graph')
    plt.show()
    
plot_helper([1, 3, 2], lw=10)