class LatencyModel:
    def __init__(self, hit_latency=20, miss_latency=200):
        self.hit_latency = hit_latency
        self.miss_latency = miss_latency

    def get_latency(self, hit):
        return self.hit_latency if hit else self.miss_latency
