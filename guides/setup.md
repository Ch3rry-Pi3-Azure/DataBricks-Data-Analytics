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
- `terraform/01_resource_group`: Azure resource group
- `terraform/02_databricks`: Azure Databricks workspace
- `scripts/`: Helper scripts to deploy/destroy Terraform resources
- `data/`: Project data files
- `notebooks/`: Jupyter notebooks (`.ipynb`)

## Configure Terraform
Edit `terraform/01_resource_group/terraform.tfvars` to set the resource group name and location:

```hcl
resource_group_name = "rg-databricks-analytics-dev"
location            = "eastus"
```

Edit `terraform/02_databricks/terraform.tfvars` to set Databricks inputs:

```hcl
resource_group_name           = "rg-databricks-analytics-dev"
location                      = "eastus"
workspace_name_prefix         = "dbw-databricks-analytics"
public_network_access_enabled = true
```

If `workspace_name` is not provided, a random animal name is appended to the prefix. The managed resource group name will follow the same pattern with `_managed` appended.

## Deploy Resources
From the repo root or `scripts/` folder, run:

```powershell
python scripts\deploy.py
```

This runs `terraform init` and `terraform apply` against `terraform/01_resource_group` and `terraform/02_databricks` in order.

Optional flags:

```powershell
python scripts\deploy.py --rg-only
python scripts\deploy.py --databricks-only
```

## Destroy Resources
To tear down resources:

```powershell
python scripts\destroy.py
```

Optional flags:

```powershell
python scripts\destroy.py --rg-only
python scripts\destroy.py --databricks-only
```

## Notes
- Resource group names must be unique within your Azure subscription.
- Follow a consistent naming convention (e.g., `rg-databricks-analytics-dev-eastus`).
- Azure Databricks creates a separate managed resource group in the same subscription.
