
resource "google_project_iam_binding" "project" {
  project = var.project_id
  role    = "roles/admin"

  members = [
    var.owner-email,
  ]
}
