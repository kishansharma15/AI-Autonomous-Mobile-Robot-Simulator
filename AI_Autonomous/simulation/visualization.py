import matplotlib.pyplot as plt

def visualize(grid,path):

    plt.imshow(grid,cmap="gray")

    if path:

        xs = [p[1] for p in path]
        ys = [p[0] for p in path]

        plt.plot(xs,ys,color="red")

    plt.title("Robot Path Planning")
    plt.show()