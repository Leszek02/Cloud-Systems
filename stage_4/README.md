## Setup

- Create files `patch-backend.yml` & `patch-frontend.yml` in `./overlays/prod`
- Define path to your backend and frontend images in those file, example:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloud-backend
  namespace: backend
spec:
  template:
    spec:
      containers:
      - name: cloud-backend
        image: <some/cool/path/to/my/registry:here>
```
- Connect kubectl with your cluster and run `kubectl apply -k ./overlays/prod` 