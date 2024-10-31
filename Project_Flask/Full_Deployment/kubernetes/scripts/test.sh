#!/bin/bash
echo "Running tests..."

# Example of a simple readiness check
kubectl wait --for=condition=ready pod -l app=my-app --timeout=60s

# Run specific integration or unit tests
curl http://localhost:8080/health

echo "Tests completed."
