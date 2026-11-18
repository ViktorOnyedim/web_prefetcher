import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


def plot_metrics(hit, precision, recall, save_path=None):
    metrics = ["Hit Ratio", "Precision", "Recall"]
    values = [hit, precision, recall]

    plt.figure()
    plt.bar(metrics, values)
    plt.ylim(0, 1)
    plt.title("Prefetching Performance Metrics")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def plot_comparison(baseline_hit, prefetch_hit, save_path=None):
    labels = ["No Prefetching", "Clustering Prefetching"]
    values = [baseline_hit, prefetch_hit]

    plt.figure()
    plt.bar(labels, values)
    plt.ylim(0, 1)
    plt.title("Cache Hit Ratio Comparison")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def plot_latency(baseline_latency, prefetch_latency, save_path=None):
    labels = ["No Prefetching", "Prefetching"]
    values = [baseline_latency, prefetch_latency]

    plt.figure()
    plt.bar(labels, values)
    plt.ylabel("Average Latency (ms)")
    plt.title("Latency Reduction")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()
def plot_latency(baseline, prefetch, save_path=None):
    plt.figure()
    plt.bar(["No Prefetch", "Prefetch"], [baseline, prefetch])
    plt.ylabel("Average Latency (ms)")
    plt.title("Latency Reduction with Prefetching")

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()
def plot_algorithm_comparison(dbscan_hit, kmeans_hit, save_path=None):
    plt.figure()
    plt.bar(["DBSCAN", "K-Means"], [dbscan_hit, kmeans_hit])
    plt.ylabel("Cache Hit Ratio")
    plt.title("Clustering Algorithm Comparison")

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()
def plot_latency_multi(baseline, dbscan, kmeans, save_path=None):
    plt.figure()
    plt.bar(
        ["Baseline", "DBSCAN", "K-Means"],
        [baseline, dbscan, kmeans]
    )
    plt.ylabel("Average Latency (ms)")
    plt.title("Latency Reduction Comparison")

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()
