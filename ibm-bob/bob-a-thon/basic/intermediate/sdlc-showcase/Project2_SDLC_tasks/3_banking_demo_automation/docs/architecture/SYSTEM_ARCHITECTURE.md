# System Architecture - Banking Applications

## Executive Summary

This document provides a comprehensive architectural overview of the Banking Demo system, focusing on the capabilities and differences between Bank 1 (Savings Bank) and Bank 2 (Investment Bank), their technical implementations, and data flows.

## System Evolution

The project has evolved through four distinct phases:

### Phase 1: Dual Python Banks
- Both banks implemented as Python Flask APIs
- Basic REST endpoints
- In-memory data storage
- Simple inter-bank transfers

### Phase 2: Terraform & Ansible Integration
- Terraform for infrastructure provisioning
- Ansible for application configuration
- Eliminated deployment duplication
- Introduced persistent storage

### Phase 3: Modern UI for Bank 1
- Bank 1 upgraded with React frontend
- Material-UI component library
- Modern dashboard and analytics
- Bank 2 remains traditional Flask

### Phase 4: Azure Cloud Deployment
- Added Azure deployment option
- Azure Container Instances
- Azure Container Registry
- Azure File Shares for persistence
- Maintained local deployment option

## High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        WebUser[Web Browser]
        APIUser[API Client]
    end
    
    subgraph "Application Layer"
        subgraph "Bank 1 - Savings Bank"
            B1Frontend[React Frontend<br/>Material-UI<br/>Vite Build]
            B1Backend[Flask Backend<br/>Python 3.9<br/>REST API]
        end
        
        subgraph "Bank 2 - Investment Bank"
            B2Backend[Flask Backend<br/>Python 3.9<br/>REST API<br/>Traditional HTML]
        end
    end
    
    subgraph "Data Layer"
        B1DB[(SQLite Database<br/>Customers<br/>Accounts<br/>Transactions)]
        B2DB[(SQLite Database<br/>Customers<br/>Accounts<br/>Transactions)]
        B1Audit[Audit Log<br/>JSONL Format]
        B2Audit[Audit Log<br/>JSONL Format]
    end
    
    WebUser -->|HTTP/HTTPS| B1Frontend
    WebUser -->|HTTP/HTTPS| B2Backend
    APIUser -->|REST API| B1Backend
    APIUser -->|REST API| B2Backend
    
    B1Frontend -->|API Calls| B1Backend
    B1Backend <-->|Inter-Bank Transfer| B2Backend
    
    B1Backend --> B1DB
    B1Backend --> B1Audit
    B2Backend --> B2DB
    B2Backend --> B2Audit
    
    style B1Frontend fill:#4FC3F7,stroke:#01579B,stroke-width:3px,color:#000
    style B1Backend fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style B2Backend fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style B1DB fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B2DB fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style B1Audit fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style B2Audit fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style WebUser fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
    style APIUser fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
```

## Bank 1 - Savings Bank (Modern Architecture)

### Technology Stack

```mermaid
graph TB
    subgraph "Frontend Stack"
        React[React 18<br/>Modern UI Framework]
        MUI[Material-UI<br/>Component Library]
        Router[React Router<br/>Client-side Routing]
        Vite[Vite<br/>Build Tool]
    end
    
    subgraph "Backend Stack"
        Flask[Flask 3.0<br/>Web Framework]
        SQLite[SQLite<br/>Database]
        Plotly[Plotly<br/>Analytics Charts]
    end
    
    subgraph "Infrastructure"
        Docker[Docker Container<br/>Multi-stage Build]
        Volume[Persistent Volume<br/>Data Storage]
    end
    
    React --> MUI
    React --> Router
    Vite --> React
    Flask --> SQLite
    Flask --> Plotly
    Docker --> Vite
    Docker --> Flask
    Volume --> SQLite
    
    style React fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style MUI fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style Flask fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style SQLite fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style Docker fill:#64B5F6,stroke:#0D47A1,stroke-width:2px,color:#000
```

### Key Features

#### Modern Web Interface
- **React-based SPA**: Single-page application with client-side routing
- **Material-UI Components**: Professional, responsive design
- **Dashboard View**: Real-time balance, recent transactions, quick actions
- **Transaction Management**: Searchable, filterable transaction history
- **Transfer Interface**: User-friendly form with validation
- **Analytics Dashboard**: Interactive charts and spending insights
- **Customer Selector**: Admin view to switch between customers

#### Frontend Capabilities
```javascript
// Component Structure
App.jsx
├── Dashboard.jsx          // Overview with balance and quick stats
├── TransactionList.jsx    // Paginated transaction history
├── TransferForm.jsx       // Inter-bank transfer interface
└── Analytics.jsx          // Spending analytics with charts
```

#### Backend API Endpoints

| Endpoint | Method | Purpose | Response |
|----------|--------|---------|----------|
| `/` | GET | Serve React app | HTML |
| `/health` | GET | Health check | JSON status |
| `/api/balance` | POST | Get customer balance | JSON with balance |
| `/api/transactions` | POST | Get transaction history | JSON array |
| `/api/analytics` | POST | Get spending analytics | JSON with charts |
| `/api/transfer` | POST | Transfer to Bank 2 | JSON result |
| `/api/deposit` | POST | Deposit funds | JSON result |
| `/api/custom_query` | POST | Natural language query | JSON result |
| `/api/audit_log` | GET | View audit trail | JSON array |

### Data Model

```mermaid
erDiagram
    CUSTOMERS ||--o{ ACCOUNTS : has
    CUSTOMERS ||--o{ TRANSACTIONS : makes
    ACCOUNTS ||--o{ TRANSACTIONS : records
    
    CUSTOMERS {
        int customer_id PK
        string name
        string email
        datetime created_at
    }
    
    ACCOUNTS {
        int account_id PK
        int customer_id FK
        string account_type
        float balance
        datetime created_at
    }
    
    TRANSACTIONS {
        int transaction_id PK
        int account_id FK
        int customer_id FK
        string transaction_type
        string category
        float amount
        string description
        datetime transaction_date
    }
```

### User Interface Flow

```mermaid
sequenceDiagram
    participant User
    participant React as React Frontend
    participant API as Flask Backend
    participant DB as SQLite Database
    
    User->>React: Open Dashboard
    React->>API: GET /api/balance
    API->>DB: SELECT balance WHERE customer_id = ?
    DB-->>API: Balance data
    API-->>React: JSON response
    React-->>User: Display dashboard
    
    User->>React: Click "Transfer"
    React->>React: Show transfer form
    User->>React: Enter amount & submit
    React->>API: POST /api/transfer
    API->>DB: BEGIN TRANSACTION
    API->>DB: UPDATE balance (deduct)
    API->>Bank2: POST /api/receive_transfer
    Bank2-->>API: Success
    API->>DB: COMMIT TRANSACTION
    API-->>React: Transfer successful
    React-->>User: Show success message
```

## Bank 2 - Investment Bank (Traditional Architecture)

### Technology Stack

```mermaid
graph TB
    subgraph "Backend Stack"
        Flask[Flask 3.0<br/>Web Framework]
        Jinja[Jinja2 Templates<br/>Server-side Rendering]
        SQLite[SQLite<br/>Database]
        Plotly[Plotly<br/>Analytics Charts]
    end
    
    subgraph "Infrastructure"
        Docker[Docker Container<br/>Single-stage Build]
        Volume[Persistent Volume<br/>Data Storage]
    end
    
    Flask --> Jinja
    Flask --> SQLite
    Flask --> Plotly
    Docker --> Flask
    Volume --> SQLite
    
    style Flask fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Jinja fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style SQLite fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style Docker fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#000
```

### Key Features

#### Traditional Web Interface
- **Server-side Rendering**: HTML generated by Flask/Jinja2
- **Form-based Interaction**: Traditional POST forms
- **Simple UI**: Functional, straightforward design
- **Blue Color Scheme**: Investment-focused branding

#### Backend API Endpoints

| Endpoint | Method | Purpose | Response |
|----------|--------|---------|----------|
| `/` | GET | Home page with forms | HTML |
| `/health` | GET | Health check | JSON status |
| `/api/balance` | POST | Get customer balance | JSON with balance |
| `/api/transactions` | POST | Get transaction history | JSON array |
| `/api/analytics` | POST | Get investment analytics | JSON with charts |
| `/api/receive_transfer` | POST | Receive from Bank 1 | JSON result |
| `/api/transfer_to_savings` | POST | Transfer to Bank 1 | JSON result |
| `/api/invest` | POST | Make investment | JSON result |
| `/api/withdraw` | POST | Withdraw funds | JSON result |
| `/api/custom_query` | POST | Natural language query | JSON result |
| `/api/audit_log` | GET | View audit trail | JSON array |

### Data Model

Same structure as Bank 1, but with investment-focused categories:
- **Transaction Categories**: stocks, bonds, mutual_funds, etf, crypto
- **Account Types**: investment, portfolio

## Comparison:
## Comparison: Bank 1 vs Bank 2

### Feature Comparison Matrix

| Feature | Bank 1 (Savings) | Bank 2 (Investment) |
|---------|------------------|---------------------|
| **Frontend** | React SPA | Server-rendered HTML |
| **UI Framework** | Material-UI | Basic HTML/CSS |
| **Routing** | Client-side (React Router) | Server-side (Flask) |
| **Build Process** | Multi-stage Docker (Vite + Flask) | Single-stage Docker (Flask only) |
| **User Experience** | Modern, interactive | Traditional, functional |
| **Dashboard** | Rich dashboard with widgets | Simple form-based interface |
| **Analytics** | Interactive Plotly charts | Server-rendered charts |
| **Mobile Support** | Responsive Material-UI | Basic responsive CSS |
| **API Design** | RESTful JSON API | RESTful JSON API |
| **Database** | SQLite with same schema | SQLite with same schema |
| **Security Features** | Parameterized queries, audit logs | Parameterized queries, audit logs |
| **Transaction Types** | Deposits, withdrawals, transfers | Investments, withdrawals, transfers |
| **Color Scheme** | Green (savings-focused) | Blue (investment-focused) |
| **Container Size** | ~200MB (includes Node.js build) | ~150MB (Python only) |
| **Startup Time** | ~5 seconds | ~3 seconds |
| **Resource Usage** | Higher (serves static files) | Lower (minimal frontend) |

### Architectural Differences

```mermaid
graph LR
    subgraph "Bank 1 Architecture"
        B1U[User] --> B1F[React Frontend]
        B1F --> B1A[Flask API]
        B1A --> B1D[(SQLite)]
    end
    
    subgraph "Bank 2 Architecture"
        B2U[User] --> B2A[Flask App]
        B2A --> B2D[(SQLite)]
    end
    
    style B1F fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style B1A fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style B2A fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style B1D fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style B2D fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
```

## Inter-Bank Communication

### Transfer Flow: Bank 1 → Bank 2

```mermaid
sequenceDiagram
    participant User
    participant B1 as Bank 1 (Savings)
    participant B1DB as Bank 1 Database
    participant B2 as Bank 2 (Investment)
    participant B2DB as Bank 2 Database
    
    User->>B1: POST /api/transfer<br/>{customer_id: 1, amount: 500}
    
    activate B1
    B1->>B1DB: BEGIN TRANSACTION
    B1->>B1DB: SELECT balance WHERE customer_id = 1
    B1DB-->>B1: balance = 5000
    
    alt Sufficient Balance
        B1->>B1DB: UPDATE accounts<br/>SET balance = balance - 500<br/>WHERE customer_id = 1
        B1->>B1DB: INSERT INTO transactions<br/>(type='withdrawal', amount=500)
        
        B1->>B2: POST /api/receive_transfer<br/>{customer_id: 1, amount: 500}
        activate B2
        B2->>B2DB: BEGIN TRANSACTION
        B2->>B2DB: UPDATE accounts<br/>SET balance = balance + 500<br/>WHERE customer_id = 1
        B2->>B2DB: INSERT INTO transactions<br/>(type='deposit', amount=500)
        B2->>B2DB: COMMIT TRANSACTION
        B2-->>B1: {success: true, new_balance: 500}
        deactivate B2
        
        B1->>B1DB: COMMIT TRANSACTION
        B1-->>User: {success: true, message: "Transfer complete"}
    else Insufficient Balance
        B1->>B1DB: ROLLBACK TRANSACTION
        B1-->>User: {success: false, error: "Insufficient funds"}
    end
    deactivate B1
    
    Note over B1,B2: If Bank 2 fails, Bank 1 rolls back
```

### Transfer Flow: Bank 2 → Bank 1

```mermaid
sequenceDiagram
    participant User
    participant B2 as Bank 2 (Investment)
    participant B2DB as Bank 2 Database
    participant B1 as Bank 1 (Savings)
    participant B1DB as Bank 1 Database
    
    User->>B2: POST /api/transfer_to_savings<br/>{customer_id: 1, amount: 300}
    
    activate B2
    B2->>B2DB: BEGIN TRANSACTION
    B2->>B2DB: SELECT balance WHERE customer_id = 1
    B2DB-->>B2: balance = 500
    
    alt Sufficient Balance
        B2->>B2DB: UPDATE accounts<br/>SET balance = balance - 300<br/>WHERE customer_id = 1
        B2->>B2DB: INSERT INTO transactions<br/>(type='withdrawal', amount=300)
        
        B2->>B1: POST /api/receive_transfer<br/>{customer_id: 1, amount: 300}
        activate B1
        B1->>B1DB: BEGIN TRANSACTION
        B1->>B1DB: UPDATE accounts<br/>SET balance = balance + 300<br/>WHERE customer_id = 1
        B1->>B1DB: INSERT INTO transactions<br/>(type='deposit', amount=300)
        B1->>B1DB: COMMIT TRANSACTION
        B1-->>B2: {success: true, new_balance: 4800}
        deactivate B1
        
        B2->>B2DB: COMMIT TRANSACTION
        B2-->>User: {success: true, message: "Transfer complete"}
    else Insufficient Balance
        B2->>B2DB: ROLLBACK TRANSACTION
        B2-->>User: {success: false, error: "Insufficient funds"}
    end
    deactivate B2
```

## Data Flow Architecture

### Request Processing Flow

```mermaid
flowchart TD
    Start([User Request]) --> Type{Request Type}
    
    Type -->|Bank 1 UI| React[React Frontend]
    Type -->|Bank 2 UI| Flask2[Flask Renders HTML]
    Type -->|API Call| API[API Endpoint]
    
    React --> APICall[API Call to Backend]
    APICall --> Validate[Validate Request]
    Flask2 --> Validate
    API --> Validate
    
    Validate --> Auth[Check Customer ID]
    Auth --> Query[Execute SQL Query]
    Query --> Schema[Validate Schema]
    Schema --> Audit[Log to Audit Trail]
    Audit --> Response[Generate Response]
    
    Response --> JSON{Response Type}
    JSON -->|Bank 1| ReactRender[React Renders UI]
    JSON -->|Bank 2| FlaskRender[Flask Renders HTML]
    JSON -->|API| APIResponse[JSON Response]
    
    ReactRender --> End([User Sees Result])
    FlaskRender --> End
    APIResponse --> End
    
    style Start fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style End fill:#66BB6A,stroke:#1B5E20,stroke-width:3px,color:#000
    style React fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style Flask2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Validate fill:#FFF176,stroke:#F57F17,stroke-width:2px,color:#000
    style Query fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style Audit fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
```

## Security Architecture

### Security Layers

```mermaid
graph TB
    subgraph "Application Security"
        Param[Parameterized Queries<br/>SQL Injection Prevention]
        Schema[Schema Validation<br/>Data Integrity]
        Isolation[Customer Data Isolation<br/>WHERE customer_id = ?]
    end
    
    subgraph "Audit & Compliance"
        Audit[Immutable Audit Trail<br/>JSONL with SHA-256]
        Logging[Comprehensive Logging<br/>All Operations]
        Disclaimer[Compliance Disclaimers<br/>Regulatory Requirements]
    end
    
    subgraph "Infrastructure Security"
        Network[Network Isolation<br/>Docker/Azure VNet]
        Storage[Encrypted Storage<br/>Azure File Shares]
        Registry[Private Registry<br/>Azure ACR]
    end
    
    style Param fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#000
    style Schema fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#000
    style Isolation fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#000
    style Audit fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Logging fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Disclaimer fill:#81C784,stroke:#1B5E20,stroke-width:2px,color:#000
    style Network fill:#A5D6A7,stroke:#1B5E20,stroke-width:2px,color:#000
    style Storage fill:#A5D6A7,stroke:#1B5E20,stroke-width:2px,color:#000
    style Registry fill:#A5D6A7,stroke:#1B5E20,stroke-width:2px,color:#000
```

### Security Features

#### Both Banks
- ✅ **Parameterized SQL Queries**: Prevents SQL injection
- ✅ **Schema Validation**: Post-execution data validation
- ✅ **Customer Data Isolation**: Enforced WHERE clauses
- ✅ **Immutable Audit Trail**: JSONL with SHA-256 hashing
- ✅ **Balance Constraints**: Database-level CHECK constraints
- ✅ **Transaction Rollback**: Automatic rollback on failure
- ⚠️ **No Authentication**: Demo environment (add for production)
- ⚠️ **No Rate Limiting**: Add for production
- ⚠️ **HTTP Only**: Add HTTPS for production

## Performance Characteristics

### Resource Usage

| Metric | Bank 1 (Savings) | Bank 2 (Investment) |
|--------|------------------|---------------------|
| **Container Image Size** | ~200 MB | ~150 MB |
| **Memory Usage (Idle)** | ~150 MB | ~100 MB |
| **Memory Usage (Active)** | ~300 MB | ~200 MB |
| **CPU Usage (Idle)** | ~5% | ~3% |
| **Startup Time** | ~5 seconds | ~3 seconds |
| **Response Time (avg)** | ~50ms | ~30ms |
| **Static File Serving** | Yes (React build) | No |

### Scalability Considerations

```mermaid
graph LR
    subgraph "Current Architecture"
        Single[Single Instance<br/>Per Bank]
        SQLite[SQLite Database<br/>File-based]
        Local[Local/Single Region]
    end
    
    subgraph "Production Scaling"
        Multi[Multiple Instances<br/>Load Balanced]
        Postgres[PostgreSQL<br/>Centralized DB]
        Global[Multi-Region<br/>Deployment]
    end
    
    Single -.->|Upgrade| Multi
    SQLite -.->|Migrate| Postgres
    Local -.->|Expand| Global
    
    style Single fill:#FFAB91,stroke:#BF360C,stroke-width:2px,color:#000
    style SQLite fill:#FFAB91,stroke:#BF360C,stroke-width:2px,color:#000
    style Local fill:#FFAB91,stroke:#BF360C,stroke-width:2px,color:#000
    style Multi fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#000
    style Postgres fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#000
    style Global fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#000
```

## Technology Decisions

### Why React for Bank 1?

**Advantages:**
- Modern, responsive user experience
- Component reusability
- Rich ecosystem of libraries
- Better mobile support
- Client-side routing (faster navigation)
- Easier to add real-time features

**Trade-offs:**
- Larger container size
- More complex build process
- Higher resource usage
- Requires JavaScript enabled

### Why Traditional Flask for Bank 2?

**Advantages:**
- Simpler architecture
- Smaller container size
- Lower resource usage
- Faster startup time
- Works without JavaScript
- Easier to maintain

**Trade-offs:**
- Less interactive UI
- Full page reloads
- Limited mobile optimization
- Harder to add real-time features

### Why SQLite?

**Advantages:**
- Zero configuration
- File-based (easy backups)
- ACID compliant
- Perfect for demo/development
- Low resource usage

**Trade-offs:**
- Single-writer limitation
- Not suitable for high concurrency
- Limited to single server
- Should migrate to PostgreSQL for production

## Deployment Architecture

### Container Build Process

#### Bank 1 (Multi-stage Build)

```dockerfile
# Stage 1: Build React frontend
FROM node:18 AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python backend with built frontend
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
COPY --from=frontend-build /app/frontend/dist ./static
EXPOSE 5000
CMD ["python", "app.py"]
```

#### Bank 2 (Single-stage Build)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
EXPOSE 5000
CMD ["python", "app.py"]
```

### Network Architecture

```mermaid
graph TB
    subgraph "External Access"
        User[Users/Clients]
    end
    
    subgraph "Application Network"
        LB[Load Balancer<br/>Optional]
        B1[Bank 1 Container<br/>Port 5001]
        B2[Bank 2 Container<br/>Port 5002]
    end
    
    subgraph "Data Network"
        Vol1[Bank 1 Volume<br/>SQLite + Logs]
        Vol2[Bank 2 Volume<br/>SQLite + Logs]
        Backup[Backup Volume<br/>Automated Backups]
    end
    
    User -->|HTTP/HTTPS| LB
    LB --> B1
    LB --> B2
    User -.->|Direct Access| B1
    User -.->|Direct Access| B2
    B1 <-->|Inter-Bank API| B2
    B1 --> Vol1
    B2 --> Vol2
    Vol1 -.->|Backup| Backup
    Vol2 -.->|Backup| Backup
    
    style User fill:#90CAF9,stroke:#0D47A1,stroke-width:2px,color:#000
    style B1 fill:#4FC3F7,stroke:#01579B,stroke-width:2px,color:#000
    style B2 fill:#FFB74D,stroke:#E65100,stroke-width:2px,color:#000
    style Vol1 fill:#B3E5FC,stroke:#01579B,stroke-width:2px,color:#000
    style Vol2 fill:#FFCC80,stroke:#E65100,stroke-width:2px,color:#000
    style Backup fill:#E0E0E0,stroke:#424242,stroke-width:2px,color:#000
    style LB fill:#CE93D8,stroke:#4A148C,stroke-width:2px,color:#000
```

## Future Enhancements

### Planned Improvements

1. **Authentication & Authorization**
   - JWT-based authentication
   - Role-based access control (RBAC)
   - OAuth2 integration

2. **Database Migration**
   - PostgreSQL for production
   - Database replication
   - Connection pooling

3. **Observability**
   - Prometheus metrics
   - Grafana dashboards
   - Distributed tracing (Jaeger)
   - Centralized logging (ELK stack)

4. **High Availability**
   - Multiple container instances
   - Load balancing
   - Health checks and auto-restart
   - Database failover

5. **Security Enhancements**
   - HTTPS/TLS encryption
   - API rate limiting
   - Input sanitization
   - CORS configuration
   - Security headers

6. **Performance Optimization**
   - Redis caching
   - CDN for static assets
   - Database query optimization
   - Connection pooling

## Related Documentation

- [Deployment Overview](../operations/DEPLOYMENT_OVERVIEW.md)
- [Banking Features](../reference/BANKING_FEATURES.md)
- [API Reference](../reference/API_REFERENCE.md)
- [Local Deployment Guide](../guides/LOCAL_DEPLOYMENT.md)
- [Azure Deployment Guide](../guides/AZURE_DEPLOYMENT.md)

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-21  
**Maintained By**: Architecture Team