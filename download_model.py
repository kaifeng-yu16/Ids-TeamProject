
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("138e1521041148988d66818c8d3cc053", path="model", dst_path=".")
print(f"Placed model in: {my_model}")
