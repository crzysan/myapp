#!/bin/bash

# NOTE: you need Docker, KinD and Kubectl installed on your machine!!!

# CREATE KIND CLUSTER
echo "========== DEPLOY CLUSTER ============="
kind create cluster --name prod --image kindest/node:v1.22.1 --config kind-cluster.yml
kind create cluster --name dev --image kindest/node:v1.22.1 --config kind-cluster-dev.yml

# DEPLOY RESOURCES DB AND APPLICATION
echo " "
echo "=========== DEV RESOURCES ============="
kubectl config use-context kind-prod
kubectl apply -f db-template.yml
kubectl apply -f myapp-template.yml
echo " "
kubectl get svc,configmap,secret,deploy --namespace playground

echo " "
echo "=========== PROD RESOURCES ============="
kubectl config use-context kind-dev
kubectl apply -f db-template.yml
kubectl apply -f myapp-template.yml
echo " "
kubectl get svc,configmap,secret,deploy --namespace playground

echo " "
echo "=========== SETUP COMPLETED ============"

