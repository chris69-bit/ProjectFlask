#!/bin/bash
echo "Deploying application..."

# Use kustomize for deploying environment-specific configs
kubectl apply -k ./deploy/environment/dev

echo "Deployment complete."
