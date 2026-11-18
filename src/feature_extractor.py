import numpy as np
from collections import Counter
from sklearn.feature_extraction import DictVectorizer

class FeatureExtractor:
    def extract(self, df):
        session_groups = df.groupby(["user_id", "session_id"])

        features = []
        sessions = []

        for _, group in session_groups:
            urls = group["url"].tolist()
            times = group["timestamp"].tolist()

            counter = Counter(urls)
            session_length = len(urls)

            time_gaps = [
                (times[i+1] - times[i]).seconds
                for i in range(len(times)-1)
            ]
            avg_gap = np.mean(time_gaps) if time_gaps else 0

            feature = dict(counter)
            feature["session_length"] = session_length
            feature["avg_gap"] = avg_gap

            features.append(feature)
            sessions.append(urls)

        # 🔥 CRITICAL FIX: Vectorize dict features
        vectorizer = DictVectorizer(sparse=False)
        X = vectorizer.fit_transform(features)

        return X, sessions
