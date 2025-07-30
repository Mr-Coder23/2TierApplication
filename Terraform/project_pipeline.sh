#!/bin/bash

echo "🔰 Stage 1: Create Infra"
terraform init
terraform plan -out=tfplan
terraform apply tfplan

# Extract instance IPs using terraform outputs
FRONTEND_IP=$(terraform output -raw frontend_public_ip)

echo "✅ Infra created. Frontend Public IP: $FRONTEND_IP"
echo

echo "🚀 Stage 2: Deploy Apps"
echo "Running frontend.sh and backend.sh via Terraform provisioners..."

# Provisioners already embedded in main.tf will auto-trigger on apply,
# so this stage assumes frontend and backend apps are installed via those scripts

echo "✅ Containers deployed. Verifying..."
ssh -o StrictHostKeyChecking=no -i ~/.ssh/id_rsa ubuntu@$FRONTEND_IP "docker ps"

echo

echo "🔍 Stage 3: Test Solution"
echo "Curling frontend at $FRONTEND_IP:3000"
curl http://$FRONTEND_IP:3000

echo
echo "✨ All stages completed. Manual testing next!"

