# Banking Demo - Modern Banking Application

## 🏦 Overview

A **production-ready demonstration** of modern banking applications showcasing real-world DevOps practices, cloud deployment, and full-stack development. This project features two distinct banking applications with different architectures and deployment options.

### Key Highlights

- 🎨 **Bank 1 (Savings)**: Modern React + Material-UI frontend with Flask backend
- 📊 **Bank 2 (Investment)**: Traditional Flask application with server-side rendering
- ☁️ **Dual Deployment**: Local Docker or Azure Cloud deployment
- 🔧 **DevOps Integration**: Terraform + Ansible working together
- 🔒 **Enterprise Security**: Audit trails, parameterized queries, data isolation
- 📈 **Analytics**: Interactive Plotly visualizations and spending insights

## 🚀 Quick Start

### One-Command Deployment

```bash
# Clone repository
git clone <repository-url>
cd banking-demo

# Deploy locally (requires Docker, Terraform, Ansible)
./deploy.sh

# Or deploy to Azure
./deploy.sh --cloud azure
```

**Access the applications:**
- Bank 1 (Savings): http://localhost:5001
- Bank 2 (Investment): http://localhost:5002

### What You Get

After deployment, you'll have:
- ✅ Two fully functional banking applications
- ✅ Persistent data storage
- ✅ Inter-bank transfer capability
- ✅ Monitoring and backup scripts
- ✅ Health check endpoints
- ✅ Audit trail logging

## 📚 Documentation

### 🎯 Start Here

- **[Quick Start Guide](docs/guides/QUICKSTART.md)** - Get running in 5 minutes
- **[Documentation Index](docs/README.md)** - Complete documentation map

### 👨‍💼 For IT Operations

- **[Deployment Overview](docs/operations/DEPLOYMENT_OVERVIEW.md)** - Deployment options and workflows
- **[Local Deployment Guide](docs/guides/LOCAL_DEPLOYMENT.md)** - Deploy with Docker locally
- **[Azure Deployment Guide](docs/guides/AZURE_DEPLOYMENT.md)** - Deploy to Azure cloud
- **[Terraform & Ansible Guide](docs/guides/TERRAFORM_ANSIBLE.md)** - Tool integration

### 🏗️ For Architects & Developers

- **[System Architecture](docs/architecture/SYSTEM_ARCHITECTURE.md)** - Bank 1 vs Bank 2 architecture
- **[API Reference](docs/reference/API_REFERENCE.md)** - Complete API documentation
- **[Banking Features](docs/reference/BANKING_FEATURES.md)** - Feature documentation
- **[Testing Guide](docs/reference/TESTING.md)** - Testing strategies

### 🔧 For Troubleshooting

- **[Troubleshooting Guide](docs/reference/TROUBLESHOOTING.md)** - Common issues and solutions

## 🏗️ Architecture Overview

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Banking Demo System                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌────────────────────┐         ┌────────────────────┐      │
│  │   Bank 1 (Savings) │         │ Bank 2 (Investment)│      │
│  │                    │◄───────►│                    │      │
│  │  React Frontend    │         │  Flask Traditional │      │
│  │  Flask Backend     │         │  Server-side HTML  │      │
│  │  Material-UI       │         │  Simple Forms      │      │
│  │  Port 5001         │         │  Port 5002         │      │
│  └────────────────────┘         └────────────────────┘      │
│                                                               │
│  Deployment Options:                                         │
│  • Local: Docker Desktop/Rancher                            │
│  • Cloud: Azure Container Instances                         │
│                                                               │
│  Orchestration:                                              │
│  • Terraform: Infrastructure provisioning                    │
│  • Ansible: Application configuration                        │
└─────────────────────────────────────────────────────────────┘
```

### Bank 1 vs Bank 2

| Feature | Bank 1 (Savings) | Bank 2 (Investment) |
|---------|------------------|---------------------|
| **Frontend** | React + Material-UI | Traditional HTML |
| **User Experience** | Modern, interactive | Simple, functional |
| **Build Process** | Multi-stage Docker | Single-stage Docker |
| **Container Size** | ~200MB | ~150MB |
| **Use Case** | Modern web app demo | Traditional app demo |

See [System Architecture](docs/architecture/SYSTEM_ARCHITECTURE.md) for detailed comparison.

## 🎯 Project Evolution

This project has evolved through four phases:

1. **Phase 1**: Two Python Flask banks with basic features
2. **Phase 2**: Terraform + Ansible integration for deployment
3. **Phase 3**: Bank 1 upgraded to modern React UI
4. **Phase 4**: Azure cloud deployment option added

## 💻 Key Features

### Banking Capabilities

- ✅ **Customer Accounts**: Multiple customers with separate accounts
- ✅ **Balance Management**: Real-time balance tracking
- ✅ **Transactions**: Deposits, withdrawals, transfers
- ✅ **Inter-Bank Transfers**: Seamless transfers between banks
- ✅ **Transaction History**: Complete audit trail
- ✅ **Analytics**: Spending/investment insights with charts
- ✅ **Audit Logging**: Immutable JSONL logs with SHA-256 hashing

### Security Features

- ✅ **Parameterized Queries**: SQL injection prevention
- ✅ **Data Isolation**: Customer data separation
- ✅ **Schema Validation**: Post-execution data validation
- ✅ **Audit Trail**: Comprehensive logging for compliance
- ✅ **Transaction Rollback**: Automatic rollback on failure

### DevOps Features

- ✅ **Infrastructure as Code**: Terraform for provisioning
- ✅ **Configuration Management**: Ansible for setup
- ✅ **Persistent Storage**: Docker volumes or Azure File Shares
- ✅ **Health Checks**: Automated health monitoring
- ✅ **Backup System**: Automated backup scripts
- ✅ **Log Rotation**: Prevents disk space issues

## 🛠️ Technology Stack

### Bank 1 (Savings Bank)
- **Frontend**: React 18, Material-UI, Vite
- **Backend**: Python Flask 3.0
- **Database**: SQLite
- **Visualization**: Plotly
- **Container**: Docker (multi-stage build)

### Bank 2 (Investment Bank)
- **Backend**: Python Flask 3.0
- **Templates**: Jinja2
- **Database**: SQLite
- **Visualization**: Plotly
- **Container**: Docker (single-stage build)

### Infrastructure & DevOps
- **Orchestration**: Terraform 1.0+
- **Configuration**: Ansible 2.9+
- **Containers**: Docker
- **Cloud**: Azure (optional)
- **Networking**: Docker Bridge / Azure VNet
- **Storage**: Docker Volumes / Azure File Shares

## 📊 Deployment Options

### Local Deployment
- **Platform**: Docker Desktop or Rancher Desktop
- **Cost**: Free (uses local resources)
- **Use Case**: Development, testing, demos
- **Access**: localhost only
- **Tools**: Terraform + Ansible

### Azure Deployment
- **Platform**: Azure Container Instances
- **Cost**: ~$66/month
- **Use Case**: Production, public demos
- **Access**: Public internet
- **Tools**: Terraform only

See [Deployment Overview](docs/operations/DEPLOYMENT_OVERVIEW.md) for detailed comparison.

## 💻 Usage Examples

### API Testing

```bash
# Get customer balance
curl -X POST http://localhost:5001/api/balance \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1}'

# View transactions
curl -X POST http://localhost:5001/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "limit": 10}'

# Transfer between banks
curl -X POST http://localhost:5001/api/transfer \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "amount": 500.0}'
```

### Management Operations

```bash
# Monitor health (created by Ansible)
/tmp/monitor_bank1.sh
/tmp/monitor_bank2.sh

# Create backups
/tmp/backup_banks.sh

# Rotate logs
/tmp/rotate_logs.sh

# View container logs
docker logs bank1-savings
docker logs bank2-investment

# View Terraform state
cd terraform && terraform show

# Re-run Ansible configuration
cd ansible && ansible-playbook playbook.yml
```

### Cleanup

```bash
# Destroy all infrastructure
cd terraform && terraform destroy -auto-approve
```

## 🎓 Learning Objectives

This project demonstrates:

1. **Modern Web Development**: React + Material-UI frontend
2. **Full-Stack Architecture**: Frontend/backend separation
3. **Infrastructure as Code**: Terraform for provisioning
4. **Configuration Management**: Ansible for setup
5. **Container Orchestration**: Docker networking and volumes
6. **Cloud Deployment**: Azure Container Instances
7. **DevOps Integration**: Terraform + Ansible working together
8. **Security Best Practices**: Parameterized queries, audit trails
9. **API Design**: RESTful JSON APIs
10. **Database Design**: SQLite with proper schema

## 🐛 Troubleshooting

For common issues and solutions, see:
- **[Troubleshooting Guide](docs/reference/TROUBLESHOOTING.md)** - Comprehensive troubleshooting
- **[Quick Start Guide](docs/guides/QUICKSTART.md)** - Basic setup issues

Quick fixes:
```bash
# Docker not running
docker info || open -a Docker

# Port conflicts
lsof -i :5001
lsof -i :5002

# Terraform state issues
cd terraform && rm -rf .terraform && terraform init

# View logs
docker logs bank1-savings
docker logs bank2-investment
```

## 📝 Project Structure

```
banking-demo/
├── README.md                     # This file - Project overview
├── deploy.sh                     # Unified deployment script
│
├── docs/                         # 📚 Documentation
│   ├── README.md                # Documentation index
│   ├── operations/              # IT Operations guides
│   ├── architecture/            # System architecture
│   ├── guides/                  # Step-by-step guides
│   └── reference/               # Reference documentation
│
├── bank1-savings/               # Bank 1 - Modern React App
│   ├── app.py                  # Flask backend
│   ├── Dockerfile              # Multi-stage build
│   ├── requirements.txt        # Python dependencies
│   └── frontend/               # React frontend
│       ├── src/
│       │   ├── App.jsx
│       │   ├── components/
│       │   └── services/
│       └── package.json
│
├── bank2-investment/            # Bank 2 - Traditional Flask
│   ├── app.py                  # Flask application
│   ├── Dockerfile              # Single-stage build
│   └── requirements.txt        # Python dependencies
│
├── terraform/                   # Local deployment (Docker)
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── terraform-azure/             # Azure deployment (ACI)
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── ansible/                     # Configuration management
│   ├── playbook.yml
│   ├── requirements.yml
│   └── roles/
│
└── diagrams/                    # Architecture diagrams
    └── architecture.md          # Mermaid diagrams
```

## 🤝 Contributing

This is a demonstration project for learning purposes. Feel free to:
- Fork and experiment
- Add new features
- Improve documentation
- Share feedback
- Report issues

## 📄 License

This project is for educational and demonstration purposes.

## 🙏 Acknowledgments

- **Technologies**: React, Material-UI, Flask, SQLite, Plotly, Terraform, Ansible, Docker, Azure
- **Purpose**: Demonstrates real-world DevOps practices and modern web development
- **Audience**: Developers, DevOps engineers, architects, students

## 📞 Support

- **Documentation**: See [docs/README.md](docs/README.md) for complete documentation
- **Issues**: Check [Troubleshooting Guide](docs/reference/TROUBLESHOOTING.md)
- **Questions**: Review relevant documentation sections

---

**Ready to deploy?**

```bash
./deploy.sh              # Local deployment
./deploy.sh --cloud azure  # Azure deployment
```

**Explore the documentation**: [docs/README.md](docs/README.md)

🚀 **Happy Banking!**