from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score

class SessionClustering:
    def __init__(self, method="dbscan", eps=2.5, min_samples=20, k=8):
        self.method = method
        self.eps = eps
        self.min_samples = min_samples
        self.k = k
        self.model = None

    def fit(self, X):
        if self.method == "dbscan":
            self.model = DBSCAN(
                eps=self.eps,
                min_samples=self.min_samples
            )
            labels = self.model.fit_predict(X)

        elif self.method == "kmeans":
            self.model = KMeans(
                n_clusters=self.k,
                n_init=10,
                random_state=42
            )
            labels = self.model.fit_predict(X)

        else:
            raise ValueError("Unknown clustering method")

        return labels

    def evaluate(self, X, labels):
        # Ignore noise for DBSCAN
        if len(set(labels)) > 1 and -1 not in labels:
            return silhouette_score(X, labels)
        return None
