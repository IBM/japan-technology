# Banking Demo - Documentation Index

Welcome to the Banking Demo documentation! This guide will help you find the information you need.

## 📚 Documentation Structure

```
docs/
├── README.md                          # This file - Documentation index
├── operations/                        # IT Operations guides
│   └── DEPLOYMENT_OVERVIEW.md        # Deployment options and workflows
├── architecture/                      # System architecture documentation
│   └── SYSTEM_ARCHITECTURE.md        # Bank 1 vs Bank 2 architecture
├── guides/                           # Step-by-step guides
│   ├── LOCAL_DEPLOYMENT.md           # Local deployment guide
│   ├── AZURE_DEPLOYMENT.md           # Azure deployment guide
│   ├── TERRAFORM_ANSIBLE.md          # Terraform & Ansible integration
│   ├── QUICKSTART.md                 # Quick start guide
│   ├── RANCHER_DESKTOP.md            # Rancher Desktop setup guide
│   └── REACT_FRONTEND_GUIDE.md       # React frontend development guide
└── reference/                        # Reference documentation
    ├── API_REFERENCE.md              # API endpoints reference
    ├── BANKING_FEATURES.md           # Banking features documentation
    ├── TESTING.md                    # Testing guide
    ├── TROUBLESHOOTING.md            # Troubleshooting guide
    └── PDF_GENERATION.md             # PDF generation guide
```

## 🎯 Quick Navigation

### For IT Operations Teams
Start here if you're deploying or managing the infrastructure:

1. **[Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)** - Understand deployment options (local vs Azure)
2. **[Local Deployment Guide](guides/LOCAL_DEPLOYMENT.md)** - Deploy locally with Docker
3. **[Azure Deployment Guide](guides/AZURE_DEPLOYMENT.md)** - Deploy to Azure cloud
4. **[Terraform & Ansible Guide](guides/TERRAFORM_ANSIBLE.md)** - How the tools work together

### For Architects & Developers
Start here if you're understanding or extending the system:

1. **[System Architecture](architecture/SYSTEM_ARCHITECTURE.md)** - Bank 1 vs Bank 2 architecture
2. **[Banking Features](reference/BANKING_FEATURES.md)** - Feature documentation
3. **[API Reference](reference/API_REFERENCE.md)** - API endpoints and usage
4. **[Testing Guide](reference/TESTING.md)** - How to test the system

### For Quick Start
Just want to get it running?

1. **[Quick Start Guide](guides/QUICKSTART.md)** - Get running in 5 minutes
2. **[Troubleshooting](reference/TROUBLESHOOTING.md)** - Common issues and solutions

## 📖 Document Descriptions

### Operations Documentation

#### [Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)
**Audience**: IT Operations, DevOps Engineers  
**Purpose**: Comprehensive overview of deployment options, workflows, and tool integration

**Topics Covered**:
- Deployment architecture diagrams
- Local vs Azure comparison
- Terraform & Ansible integration
- Management operations
- Cost analysis
- Security considerations

### Architecture Documentation

#### [System Architecture](architecture/SYSTEM_ARCHITECTURE.md)
**Audience**: Architects, Senior Developers  
**Purpose**: Deep dive into system architecture and design decisions

**Topics Covered**:
- Project evolution (4 phases)
- Bank 1 (React + Flask) architecture
- Bank 2 (Flask only) architecture
- Feature comparison matrix
- Inter-bank communication
- Data flows and security
- Performance characteristics
- Technology decisions

### Deployment Guides

#### [Local Deployment Guide](guides/LOCAL_DEPLOYMENT.md)
**Audience**: Developers, QA Engineers  
**Purpose**: Step-by-step guide for local deployment

**Topics Covered**:
- Prerequisites and setup
- Docker Desktop/Rancher configuration
- Terraform deployment
- Ansible configuration
- Verification and testing
- Management scripts

#### [Azure Deployment Guide](guides/AZURE_DEPLOYMENT.md)
**Audience**: Cloud Engineers, DevOps  
**Purpose**: Step-by-step guide for Azure deployment

**Topics Covered**:
- Azure prerequisites
- Container Registry setup
- Azure Container Instances
- Storage configuration
- Networking and security
- Cost management
- Monitoring and logs

#### [Terraform & Ansible Integration](guides/TERRAFORM_ANSIBLE.md)
**Audience**: Infrastructure Engineers  
**Purpose**: Understanding how Terraform and Ansible work together

**Topics Covered**:
- Why use both tools
- Terraform responsibilities (WHAT)
- Ansible responsibilities (HOW)
- Integration patterns
- Best practices
- Troubleshooting

#### [Quick Start Guide](guides/QUICKSTART.md)
**Audience**: Everyone
**Purpose**: Get running quickly

**Topics Covered**:
- Prerequisites check
- One-command deployment
- Basic testing
- Cleanup

#### [Rancher Desktop Guide](guides/RANCHER_DESKTOP.md)
**Audience**: Developers using Rancher Desktop
**Purpose**: Setup and configuration for Rancher Desktop

**Topics Covered**:
- Rancher Desktop installation
- Configuration for banking demo
- Troubleshooting Rancher-specific issues

#### [React Frontend Guide](guides/REACT_FRONTEND_GUIDE.md)
**Audience**: Frontend Developers
**Purpose**: Understanding and developing Bank 1's React frontend

**Topics Covered**:
- React application structure
- Material-UI components
- Frontend development workflow
- Building and deployment

### Reference Documentation

#### [API Reference](reference/API_REFERENCE.md)
**Audience**: Developers, API Consumers  
**Purpose**: Complete API documentation

**Topics Covered**:
- Bank 1 API endpoints
- Bank 2 API endpoints
- Request/response formats
- Error handling
- Authentication (future)

#### [Banking Features](reference/BANKING_FEATURES.md)
**Audience**: Product Managers, Developers  
**Purpose**: Feature documentation and capabilities

**Topics Covered**:
- Bank 1 features (React UI)
- Bank 2 features (Traditional)
- Security features
- Audit trail
- Analytics capabilities
- Database schema

#### [Testing Guide](reference/TESTING.md)
**Audience**: QA Engineers, Developers  
**Purpose**: Testing strategies and procedures

**Topics Covered**:
- Unit testing
- Integration testing
- API testing
- Load testing
- Test automation

#### [Troubleshooting Guide](reference/TROUBLESHOOTING.md)
**Audience**: Everyone  
**Purpose**: Solutions to common problems

**Topics Covered**:
- Docker issues
- Terraform issues
- Ansible issues
- Azure issues
- Network issues
- Container issues

#### [PDF Generation](reference/PDF_GENERATION.md)
**Audience**: Documentation Maintainers  
**Purpose**: Generate PDF documentation

**Topics Covered**:
- PDF generation tools
- Mermaid diagram rendering
- Document compilation
- Distribution

## 🚀 Getting Started Paths

### Path 1: Developer (Local Development)
```
1. Quick Start Guide
2. Local Deployment Guide
3. API Reference
4. Testing Guide
```

### Path 2: DevOps Engineer (Production Deployment)
```
1. Deployment Overview
2. System Architecture
3. Azure Deployment Guide
4. Terraform & Ansible Guide
5. Troubleshooting Guide
```

### Path 3: Architect (System Understanding)
```
1. System Architecture
2. Deployment Overview
3. Banking Features
4. API Reference
```

### Path 4: QA Engineer (Testing)
```
1. Quick Start Guide
2. Testing Guide
3. API Reference
4. Troubleshooting Guide
```

## 📊 Diagram Locations

All architecture diagrams use Mermaid syntax and are embedded in the documentation:

- **Deployment workflows**: [Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)
- **System architecture**: [System Architecture](architecture/SYSTEM_ARCHITECTURE.md)
- **Data flows**: [System Architecture](architecture/SYSTEM_ARCHITECTURE.md)
- **Network diagrams**: [Deployment Overview](operations/DEPLOYMENT_OVERVIEW.md)

### Viewing Diagrams

Diagrams are written in Mermaid and can be viewed in:
- **GitHub**: Automatically renders Mermaid
- **VS Code**: Install "Markdown Preview Mermaid Support" extension
- **Online**: https://mermaid.live/
- **Documentation sites**: GitBook, Docusaurus, etc.

## 🔄 Document Maintenance

### Version History
- **v1.0** (2025-11-21): Initial organized documentation structure
  - Reorganized from root-level files
  - Added comprehensive diagrams
  - Separated operations, architecture, guides, and reference docs

### Contributing
When updating documentation:
1. Keep diagrams up to date with code changes
2. Update the relevant section (operations/architecture/guides/reference)
3. Update this index if adding new documents
4. Maintain consistent formatting and style

### Document Owners
- **Operations**: IT Operations Team
- **Architecture**: Architecture Team
- **Guides**: DevOps Team
- **Reference**: Development Team

## 📞 Support

For questions or issues:
1. Check the [Troubleshooting Guide](reference/TROUBLESHOOTING.md)
2. Review relevant documentation section
3. Check GitHub issues
4. Contact the appropriate team (see Document Owners above)

## 🔗 External Resources

- **Terraform Documentation**: https://www.terraform.io/docs
- **Ansible Documentation**: https://docs.ansible.com
- **Docker Documentation**: https://docs.docker.com
- **Azure Documentation**: https://docs.microsoft.com/azure
- **React Documentation**: https://react.dev
- **Flask Documentation**: https://flask.palletsprojects.com

---

**Last Updated**: 2025-11-21  
**Documentation Version**: 1.0