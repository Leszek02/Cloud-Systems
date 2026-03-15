## Setup

- Create file `project.tfvars`
- Define your project id in this file like this:
```
    project_id  = "Froggies-1239"
```
- run `terraform plan -var-file="project.tfvars" -out ./plan` & \
      `terraform apply ./plan`