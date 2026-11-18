from collections import defaultdict

class MarkovPredictor:
    def __init__(self, min_confidence=0.2):
        self.models = defaultdict(
            lambda: defaultdict(lambda: defaultdict(int))
        )
        self.min_confidence = min_confidence

    def train(self, sessions, labels):
        for session, label in zip(sessions, labels):
            for i in range(len(session) - 1):
                self.models[label][session[i]][session[i + 1]] += 1

    def predict_next(self, current_page, cluster_label, top_k=3):
        transitions = self.models[cluster_label].get(current_page, {})
        total = sum(transitions.values())

        if total == 0:
            return []

        ranked = []
        for page, count in transitions.items():
            prob = count / total
            if prob >= self.min_confidence:
                ranked.append((page, prob))

        ranked.sort(key=lambda x: x[1], reverse=True)

        return [page for page, _ in ranked[:top_k]]
