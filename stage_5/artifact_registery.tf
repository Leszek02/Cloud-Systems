resource "google_artifact_registry_repository" "cloud-systems-registry" {
  project = var.project_id
  location      = local.location
  repository_id = "cloud-systems-registry-21315"
  description   = "Registry to store images used for Cloud System project"
  format        = "DOCKER"
}