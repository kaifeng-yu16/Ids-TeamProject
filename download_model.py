
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("6295d5a5af704769ac898c7e84de1d89", path="model", dst_path=".")
print(f"Placed model in: {my_model}")
