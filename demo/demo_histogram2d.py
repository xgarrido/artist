import numpy as np

from artist import GraphArtist


def main():

    x_edges = np.arange(5)
    y_edges = np.arange(5)
    H = np.random.random_sample((len(x_edges)-1, len(y_edges)-1))

    # make graph
    graph = GraphArtist()

    # graph histogram
    graph.histogram2d(H, x_edges, y_edges)

    # set labels and limits
    graph.set_xlabel("value")
    graph.set_ylabel("count")

    # save graph to file
    graph.save('histogram-2d')

if __name__ == '__main__':
    main()
