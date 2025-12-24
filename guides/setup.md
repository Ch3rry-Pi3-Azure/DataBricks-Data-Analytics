# Project Setup Guide

This project provisions Azure resources for Databricks using Terraform and includes helper scripts.

## Prerequisites
- Azure CLI (`az`) installed and authenticated
- Terraform installed (>= 1.5)
- Python (for running the helper scripts)

## Azure CLI
Check your Azure CLI and login status:

```powershell
az --version
az login
az account show
```

## Project Structure
- `terraform/`: Infrastructure as code (Azure resource group and future resources)
- `scripts/`: Helper scripts to deploy/destroy Terraform resources
- `data/`: Project data files
- `notebooks/`: Jupyter notebooks (`.ipynb`)

## Configure Terraform
Edit `terraform/terraform.tfvars` to set the resource group name and location:

```hcl
resource_group_name = "rg-databricks-analytics-dev"
location            = "eastus"
```

## Deploy Resources
From the repo root or `scripts/` folder, run:

```powershell
python scripts\deploy.py
```

This runs `terraform init` and `terraform apply` against the `terraform/` directory.

## Destroy Resources
To tear down resources:

```powershell
python scripts\destroy.py
```

## Notes
- Resource group names must be unique within your Azure subscription.
- Follow a consistent naming convention (e.g., `rg-databricks-analytics-dev-eastus`).
