import matplotlib.pyplot as plt

def plot_metrics(hit, precision, recall):
    metrics = ["Hit Ratio", "Precision", "Recall"]
    values = [hit, precision, recall]

    plt.figure()
    plt.bar(metrics, values)
    plt.ylim(0, 1)
    plt.title("Prefetching Performance Metrics")
    plt.show()
