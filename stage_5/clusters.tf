resource "google_service_account" "k8s_service_account" {
  project      = var.project_id
  account_id   = "node-pool-sa-21371"
  display_name = "A service account to manage applications within the k8s cluster"
}

resource "google_container_cluster" "cloud-systems-cluster" {
  name     = "cloud-systems-cluster"
  project  = var.project_id
  location = local.location

  remove_default_node_pool = true
  initial_node_count       = 1
  deletion_protection      = false

  node_config {
    boot_disk {
      size_gb = 20
    }
    spot = true
  }
  cluster_autoscaling {
    auto_provisioning_defaults {
      disk_size = 20
    }
  }
}

resource "google_container_node_pool" "cloud-systems-node-pool" {
  name     = "cloud-systems-node-pool"
  project  = var.project_id
  location = local.location
  cluster  = google_container_cluster.cloud-systems-cluster.id

  node_config {
    machine_type    = "n1-standard-2"
    spot            = true
    service_account = google_service_account.k8s_service_account.email
    disk_size_gb    = 20
  }
  autoscaling {
    min_node_count = 0
    max_node_count = 2
  }
}

