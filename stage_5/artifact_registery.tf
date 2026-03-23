resource "google_artifact_registry_repository" "cloud-systems-registry" {
  project       = var.project_id
  location      = local.location
  repository_id = "cloud-systems-registry-21315"
  description   = "Registry to store images used for Cloud System project"
  format        = "DOCKER"
}

resource "google_artifact_registry_repository_iam_binding" "binding" {
  project    = var.project_id
  location   = local.location
  repository = google_artifact_registry_repository.cloud-systems-registry.name
  role       = "roles/artifactregistry.reader"
  members = [
    "serviceAccount:${google_service_account.k8s_service_account.email}"
  ]
}