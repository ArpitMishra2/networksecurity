import os
import mlflow

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/ArpitMishra2/networksecurity.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "ArpitMishra2"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "32da7f47bdf1f4c8441548e6c500604e907ed303"

with mlflow.start_run(run_name="test_run_auth") as run:
    mlflow.log_param("test_param", 1)
    mlflow.log_metric("test_metric", 0.95)

print("✅ Auth successful, run created!")
