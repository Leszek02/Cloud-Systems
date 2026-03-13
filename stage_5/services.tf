locals {
  services = toset([
    "iam.googleapis.com",
    "compute.googleapis.com",
    "container.googleapis.com",
  ])
}

resource "google_project_service" "project" {
  for_each = local.services
  project  = var.project_id
  service  = each.value
}