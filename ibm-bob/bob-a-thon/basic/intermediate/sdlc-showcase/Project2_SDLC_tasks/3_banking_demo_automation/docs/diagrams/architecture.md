# Banking Demo - Architecture Diagrams

> **Note**: This file contains the original architecture diagrams with improved readability.
> For comprehensive architecture documentation, see [System Architecture](../architecture/SYSTEM_ARCHITECTURE.md).

## System Architecture

```mermaid
graph TB
    subgraph "MacBook Host / Azure Cloud"
        subgraph "Docker Environment / Azure Container Instances"
            Network[Docker Network / Azure VNet<br/>banking-network<br/>172.20.0.0/16]
            
            subgraph "Bank 1 Container"
                B1[Bank 1 - Savings<br/>React Frontend + Flask API<br/>Port 5001]
                B1Data[(SQLite Database<br/>Customers, Accounts<br/>Transactions, Audit Log)]
            end
            
            subgraph "Bank 2 Container"
                B2[Bank 2 - Investment<br/>Flask API (Traditional)<br/>Port 5002]
                B2Data[(SQLite Database<br/>Customers, Accounts<br/>Transactions, Audit Log)]
            end
        end
        
        subgraph "Deployment Tools"
            TF[Terraform<br/>Infrastructure as Code]
            AN[Ansible<br/>Configuration Management<br/>Local Only]
        end
    end
    
    User[User/Browser] -->|HTTP :5001| B1
    User -->|HTTP :5002| B2
    B1 <-->|Inter-Bank Transfer API| B2
    B1 -.-> B1Data
    B2 -.-> B2Data
    B1 -.-> Network
    B2 -.-> Network
    TF -.->|Provisions| Network
    TF -.->|Deploys| B1
    TF -.->|Deploys| B2
    AN -.->|Configures Local| B1
    AN -.->|Configures Local| B2
    
    style B1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style B2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Network fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
    style TF fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style AN fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style B1Data fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B2Data fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style User fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
```

## Transfer Flow

```mermaid
sequenceDiagram
    participant User
    participant Bank1 as Bank 1 (Savings)<br/>Port 5001
    participant Bank2 as Bank 2 (Investment)<br/>Port 5002
    
    User->>Bank1: POST /transfer<br/>{user_id: "user1", amount: 500}
    
    activate Bank1
    Bank1->>Bank1: Validate user exists
    Bank1->>Bank1: Check balance >= 500
    Bank1->>Bank1: Deduct $500 from user1
    
    Bank1->>Bank2: POST /receive<br/>{user_id: "user1", amount: 500}
    activate Bank2
    Bank2->>Bank2: Validate user exists
    Bank2->>Bank2: Add $500 to user1
    Bank2-->>Bank1: Success response
    deactivate Bank2
    
    Bank1-->>User: Transfer successful<br/>New balance: $4,500
    deactivate Bank1
    
    Note over Bank1,Bank2: If Bank 2 fails, Bank 1 rolls back
```

## Deployment Flow - Terraform

```mermaid
flowchart TD
    Start([Start Deployment]) --> Init[terraform init<br/>Download providers]
    Init --> Plan[terraform plan<br/>Preview changes]
    Plan --> Apply[terraform apply<br/>Execute deployment]
    
    Apply --> Network[Create Docker Network<br/>banking-network]
    Network --> BuildB1[Build Bank 1 Image<br/>bank1-savings:latest]
    Network --> BuildB2[Build Bank 2 Image<br/>bank2-investment:latest]
    
    BuildB1 --> DeployB1[Deploy Bank 1 Container<br/>Port 5001]
    BuildB2 --> DeployB2[Deploy Bank 2 Container<br/>Port 5002]
    
    DeployB1 --> Health1[Health Check<br/>Bank 1]
    DeployB2 --> Health2[Health Check<br/>Bank 2]
    
    Health1 --> Complete{All Healthy?}
    Health2 --> Complete
    
    Complete -->|Yes| Success([Deployment Complete])
    Complete -->|No| Fail([Deployment Failed])
    
    style Start fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Success fill:#66BB6A,stroke:#1B5E20,stroke-width:3px,color:#000
    style Fail fill:#EF5350,stroke:#B71C1C,stroke-width:3px,color:#fff
    style Network fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
    style BuildB1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style BuildB2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style DeployB1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style DeployB2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Health1 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style Health2 fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style Complete fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
```

## Deployment Flow - Ansible

```mermaid
flowchart TD
    Start([Start Playbook]) --> Check[Check Docker Status]
    Check --> Network[Create Docker Network]
    
    Network --> Build[Build Docker Images]
    Build --> BuildB1[Build Bank 1 Image]
    Build --> BuildB2[Build Bank 2 Image]
    
    BuildB1 --> Deploy[Deploy Containers]
    BuildB2 --> Deploy
    
    Deploy --> DeployB1[Deploy Bank 1<br/>with environment vars]
    Deploy --> DeployB2[Deploy Bank 2<br/>with environment vars]
    
    DeployB1 --> Wait1[Wait for Health Check<br/>Bank 1]
    DeployB2 --> Wait2[Wait for Health Check<br/>Bank 2]
    
    Wait1 --> Verify{All Services<br/>Healthy?}
    Wait2 --> Verify
    
    Verify -->|Yes| Summary[Display Summary]
    Verify -->|No| Retry[Retry Health Checks]
    Retry --> Verify
    
    Summary --> Complete([Deployment Complete])
    
    style Start fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style Complete fill:#66BB6A,stroke:#1B5E20,stroke-width:3px,color:#000
    style Network fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
    style BuildB1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style BuildB2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style DeployB1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style DeployB2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Wait1 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style Wait2 fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style Verify fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style Check fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style Build fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style Deploy fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style Summary fill:#A5D6A7,stroke:#1B5E20,stroke-width:2px,color:#000
    style Retry fill:#FFAB91,stroke:#BF360C,stroke-width:2px,color:#000
```

## Container Communication

```mermaid
graph LR
    subgraph "Host Network"
        Host[localhost]
    end
    
    subgraph "Docker Network: banking-network"
        B1[bank1-savings<br/>172.20.0.2:5000]
        B2[bank2-investment<br/>172.20.0.3:5000]
    end
    
    Host -->|Port 5001| B1
    Host -->|Port 5002| B2
    B1 -->|Internal DNS<br/>bank2-investment:5000| B2
    
    style Host fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style B1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style B2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
```

## API Endpoints

```mermaid
graph TD
    subgraph "Bank 1 API (Port 5001)"
        B1Root[GET /<br/>Welcome & Info]
        B1Users[GET /users<br/>List all users]
        B1User[GET /user/:id<br/>Get user details]
        B1Transfer[POST /transfer<br/>Transfer to Bank 2]
        B1Deposit[POST /deposit<br/>Add funds]
        B1Health[GET /health<br/>Health check]
    end
    
    subgraph "Bank 2 API (Port 5002)"
        B2Root[GET /<br/>Welcome & Info]
        B2Users[GET /users<br/>List all users]
        B2User[GET /user/:id<br/>Get user details]
        B2Receive[POST /receive<br/>Receive from Bank 1]
        B2Withdraw[POST /withdraw<br/>Remove funds]
        B2Health[GET /health<br/>Health check]
    end
    
    B1Transfer -.->|HTTP POST| B2Receive
    
    style B1Root fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B1Users fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B1User fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B1Transfer fill:#29B6F6,stroke:#01579B,stroke-width:3px,color:#000
    style B1Deposit fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B1Health fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    
    style B2Root fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style B2Users fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style B2User fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style B2Receive fill:#FF9800,stroke:#E65100,stroke-width:3px,color:#000
    style B2Withdraw fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style B2Health fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
```

## Data Model

```mermaid
erDiagram
    BANK1_USER {
        string user_id PK
        string name
        float balance
    }
    
    BANK2_USER {
        string user_id PK
        string name
        float balance
    }
    
    TRANSFER {
        string user_id FK
        float amount
        timestamp created_at
        string status
    }
    
    BANK1_USER ||--o{ TRANSFER : initiates
    BANK2_USER ||--o{ TRANSFER : receives
```

## Technology Stack

```mermaid
graph TB
    subgraph "Application Layer"
        Flask[Python Flask 3.0<br/>REST API Framework]
        Requests[Requests Library<br/>HTTP Client]
    end
    
    subgraph "Container Layer"
        Docker[Docker<br/>Container Runtime]
        Network[Docker Network<br/>Bridge Driver]
    end
    
    subgraph "Infrastructure Layer"
        Terraform[Terraform<br/>IaC Provisioning]
        Ansible[Ansible<br/>Configuration Management]
    end
    
    subgraph "Base Layer"
        Python[Python 3.9<br/>Runtime]
        Linux[Linux Container<br/>python:3.9-slim]
    end
    
    Flask --> Python
    Requests --> Python
    Docker --> Linux
    Network --> Docker
    Terraform --> Docker
    Ansible --> Docker
    
    style Flask fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style Requests fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style Docker fill:#64B5F6,stroke:#0D47A1,stroke-width:2px,color:#000
    style Network fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
    style Terraform fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Ansible fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style Python fill:#FFD54F,stroke:#F57F17,stroke-width:2px,color:#000
    style Linux fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
```

## Cleanup Process

```mermaid
flowchart TD
    Start([Cleanup Initiated]) --> Stop1[Stop Bank 1 Container]
    Start --> Stop2[Stop Bank 2 Container]
    
    Stop1 --> Remove1[Remove Bank 1 Container]
    Stop2 --> Remove2[Remove Bank 2 Container]
    
    Remove1 --> Image1[Remove Bank 1 Image]
    Remove2 --> Image2[Remove Bank 2 Image]
    
    Image1 --> Network[Remove Docker Network]
    Image2 --> Network
    
    Network --> Complete([Cleanup Complete])
    
    style Start fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style Complete fill:#66BB6A,stroke:#1B5E20,stroke-width:3px,color:#000
    style Stop1 fill:#FFAB91,stroke:#BF360C,stroke-width:2px,color:#000
    style Stop2 fill:#FFAB91,stroke:#BF360C,stroke-width:2px,color:#000
    style Remove1 fill:#FF7043,stroke:#BF360C,stroke-width:2px,color:#fff
    style Remove2 fill:#FF7043,stroke:#BF360C,stroke-width:2px,color:#fff
    style Image1 fill:#EF5350,stroke:#B71C1C,stroke-width:2px,color:#fff
    style Image2 fill:#EF5350,stroke:#B71C1C,stroke-width:2px,color:#fff
    style Network fill:#E57373,stroke:#B71C1C,stroke-width:2px,color:#fff
```

## Viewing These Diagrams

These diagrams are written in Mermaid syntax and can be viewed in:

1. **GitHub** - Automatically renders Mermaid diagrams
2. **VS Code** - Install "Markdown Preview Mermaid Support" extension
3. **Online** - https://mermaid.live/
4. **Documentation sites** - GitBook, Docusaurus, etc.

## Diagram Legend

- 🔵 Blue boxes: Bank 1 (Savings) components
- 🟠 Orange boxes: Bank 2 (Investment) components
- 🟣 Purple boxes: Network infrastructure
- 🟢 Green boxes: Terraform components
- 🟡 Yellow boxes: Ansible components
- Solid lines: Direct communication
- Dashed lines: Management/configuration