#!/bin/bash

kubectl apply -f ticket-submitter-deployment.yaml
kubectl apply -f ticket-submitter-service.yaml
kubectl apply -f mongodb-deployment.yaml
kubectl apply -f mongodb-service.yaml
