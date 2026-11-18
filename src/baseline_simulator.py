class BaselineSimulator:
    def __init__(self):
        self.total_requests = 0
        self.hits = 0
        self.latencies = []

    def request(self, page):
        """
        Baseline: no prefetching, no cache
        """
        self.total_requests += 1

        # All requests are cache misses
        base_latency = 200  # ms
        self.latencies.append(base_latency)

    def metrics(self):
        hit_ratio = 0.0  # no cache
        avg_latency = sum(self.latencies) / len(self.latencies) if self.latencies else 0.0
        return hit_ratio, avg_latency
