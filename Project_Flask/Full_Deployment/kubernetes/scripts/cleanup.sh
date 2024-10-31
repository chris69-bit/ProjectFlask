#!/bin/bash
echo "Cleaning up resources..."

# Example cleanup commands
kubectl delete deployment my-app-deployment
kubectl delete service my-app-service

echo "Cleanup complete."
