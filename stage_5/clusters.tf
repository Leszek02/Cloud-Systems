resource "google_service_account" "k8s_service_account" {
  account_id   = "service-account-id"
  display_name = "A service account to manage applications within the k8s cluster"
}

resource "google_container_cluster" "primary" {
  name     = "cloud-systems-cluster"
  location = "eu-east-5"

  remove_default_node_pool = true
  initial_node_count       = 0
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-node-pool"
  location   = "eu-east-5"
  cluster    = google_container_cluster.primary.name
  node_count = 1


  node_config {
    preemptible  = true
    machine_type = "n1-standard-2"
    spot       = true
    service_account = google_service_account.default.email
  }
}