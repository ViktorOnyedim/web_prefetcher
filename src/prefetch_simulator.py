class PrefetchSimulator:
    def __init__(self, prefetch_enabled=True):
        self.prefetch_enabled = prefetch_enabled
        self.cache = set()
        self.total_requests = 0
        self.hits = 0
        self.prefetch_count = 0
        self.latencies = []

    def request(self, actual, predicted):
        base_latency = 300  # ms

        if self.prefetch_enabled:
            for p in predicted:
                if p not in self.cache:
                    self.prefetch_count += 1
                self.cache.add(p)

        self.total_requests += 1

        if actual in self.cache:
            self.hits += 1
            self.latencies.append(base_latency * 0.3)
        else:
            self.latencies.append(base_latency)

    def metrics(self):
        hit_ratio = self.hits / self.total_requests
        avg_latency = sum(self.latencies) / len(self.latencies)
        bandwidth = self.prefetch_count / self.total_requests

        precision = hit_ratio
        recall = hit_ratio

        return hit_ratio, precision, recall, avg_latency, bandwidth
