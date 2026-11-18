from src.feature_extractor import FeatureExtractor
from src.clustering import SessionClustering
from src.predictor import MarkovPredictor
from src.prefetch_simulator import PrefetchSimulator
from src.baseline_simulator import BaselineSimulator
from src.evaluation import (
    plot_metrics,
    plot_comparison,
    plot_latency
)
from src.traffic_simulator import TrafficSimulator
import os

# --------------------------------------------------
# SETUP
# --------------------------------------------------
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# 1. GENERATE HIGH-TRAFFIC WEB LOGS
# --------------------------------------------------
print("🚀 Generating high-traffic logs...")

logs = TrafficSimulator(
    users=10000,
    pages=50,
    sessions_per_user=5
).generate()

# --------------------------------------------------
# 2. SESSIONIZATION
# --------------------------------------------------
logs.sort_values(["user_id", "timestamp"], inplace=True)
logs["session_id"] = logs.groupby("user_id").cumcount() // 5

print(f"✅ Total requests generated: {len(logs)}")

# --------------------------------------------------
# 3. FEATURE EXTRACTION
# --------------------------------------------------
features, sessions = FeatureExtractor().extract(logs)
print(f"✅ Total sessions created: {len(sessions)}")

# --------------------------------------------------
# 4. CLUSTERING (DBSCAN)
# --------------------------------------------------
clusterer = SessionClustering(
    method="dbscan",
    eps=1.5,
    min_samples=10
)

labels = clusterer.fit(features)

total_clusters = len(set(labels)) - (1 if -1 in labels else 0)
noise_sessions = list(labels).count(-1)

print(f"✅ Clusters found: {total_clusters}")
print(f"⚠️ Noise sessions: {noise_sessions}")

# --------------------------------------------------
# 5. TRAIN CLUSTER-AWARE MARKOV PREDICTOR
# --------------------------------------------------
predictor = MarkovPredictor()
predictor.train(sessions, labels)

print("✅ Cluster-aware Markov predictor trained")

# --------------------------------------------------
# 6. BASELINE SIMULATION (NO PREFETCHING)
# --------------------------------------------------
baseline = BaselineSimulator()

for session in sessions:
    for i in range(len(session) - 1):
        baseline.request(session[i + 1])

baseline_hit_ratio, baseline_latency = baseline.metrics()

print("\n--- Baseline Performance ---")
print(f"Hit Ratio       : {baseline_hit_ratio:.3f}")
print(f"Avg Latency (ms): {baseline_latency:.1f}")

# --------------------------------------------------
# 7. PREFETCH SIMULATION (CLUSTER-BASED)
# --------------------------------------------------
sim = PrefetchSimulator(prefetch_enabled=True)

for session, label in zip(sessions, labels):
    for i in range(len(session) - 1):
        predicted = predictor.predict_next(
            current_page=session[i],
            cluster_label=label
        )
        sim.request(session[i + 1], predicted)

# 🔥 IMPORTANT: unpack ALL returned metrics
hit_ratio, precision, recall, avg_latency, bandwidth = sim.metrics()

print("\n--- Prefetching Performance ---")
print(f"Cache Hit Ratio : {hit_ratio:.3f}")
print(f"Precision       : {precision:.3f}")
print(f"Recall          : {recall:.3f}")
print(f"Avg Latency (ms): {avg_latency:.1f}")
print(f"Bandwidth Overhead: {bandwidth:.3f}")

# --------------------------------------------------
# 8. SAVE & DISPLAY RESULTS
# --------------------------------------------------
print("📊 Saving and displaying charts...")

plot_metrics(
    hit_ratio,
    precision,
    recall,
    save_path="results/prefetch_metrics.png"
)

plot_comparison(
    baseline_hit_ratio,
    hit_ratio,
    save_path="results/hit_ratio_comparison.png"
)

plot_latency(
    baseline_latency,
    avg_latency,
    save_path="results/latency_comparison.png"
)

print("✅ All results saved to /results folder")
