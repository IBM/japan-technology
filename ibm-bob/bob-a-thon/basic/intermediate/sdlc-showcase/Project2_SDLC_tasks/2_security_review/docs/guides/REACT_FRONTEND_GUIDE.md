# React + Material-UI Frontend Guide

## Overview

Bank 1 (Savings) now features a **world-class React + Material-UI frontend** while Bank 2 (Investment) retains its original embedded HTML interface. This demonstrates how modern frontend frameworks can be integrated with existing Flask backends.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND ARCHITECTURE                     │
└─────────────────────────────────────────────────────────────┘

Bank 1 (Savings) - React + Material-UI
├── React 18 (Modern UI framework)
├── Material-UI (Professional components)
├── Recharts (Data visualization)
├── React Router (Client-side routing)
└── Axios (API communication)
    ↓
Flask REST API (Existing backend)
    ↓
SQLite Database

Bank 2 (Investment) - Original HTML
└── Embedded HTML/CSS/JavaScript
    ↓
Flask REST API (Existing backend)
    ↓
SQLite Database
```

## Why React + Material-UI?

### React Benefits
- ✅ **Component-Based**: Reusable UI components
- ✅ **Virtual DOM**: Fast, efficient updates
- ✅ **Rich Ecosystem**: Thousands of libraries
- ✅ **Industry Standard**: Used by Facebook, Netflix, Airbnb
- ✅ **Great Developer Experience**: Hot reload, debugging tools

### Material-UI Benefits
- ✅ **Professional Design**: Google's Material Design
- ✅ **Pre-built Components**: Cards, tables, forms, dialogs
- ✅ **Responsive**: Mobile-first design
- ✅ **Customizable**: Easy theming
- ✅ **Accessibility**: WCAG compliant

## Project Structure

```
bank1-savings/
├── frontend/                    # React application
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── Dashboard.jsx   # Account overview (200 lines)
│   │   │   ├── TransactionList.jsx  # Transaction history (197 lines)
│   │   │   ├── TransferForm.jsx     # Transfer interface (213 lines)
│   │   │   └── Analytics.jsx        # Charts & insights (223 lines)
│   │   ├── services/
│   │   │   └── api.js          # API service layer (90 lines)
│   │   ├── App.jsx             # Main app with routing (267 lines)
│   │   └── main.jsx            # Entry point (8 lines)
│   ├── index.html              # HTML template
│   ├── package.json            # Dependencies
│   ├── vite.config.js          # Build configuration
│   └── README.md               # Frontend documentation
└── app.py                      # Flask backend (unchanged)
```

## Components

### 1. Dashboard Component

**Purpose**: Account overview with balance cards

**Features**:
- Current balance display with gradient card
- Account information (name, email, type)
- Quick stats (status, transfer availability, security)
- Compliance disclaimer
- Real-time balance updates

**Key Technologies**:
- Material-UI Cards, Grid, Typography
- Custom gradient styling
- Responsive layout

### 2. Transaction List Component

**Purpose**: Display transaction history

**Features**:
- Sortable table with transaction details
- Color-coded transaction types (deposit, withdrawal, transfer)
- Icons for visual identification
- Date formatting
- Refresh functionality
- Hover effects

**Key Technologies**:
- Material-UI Table components
- date-fns for date formatting
- Chip components for categories

### 3. Transfer Form Component

**Purpose**: Inter-bank fund transfers

**Features**:
- Amount input with validation
- Current balance display
- Confirmation dialog
- Success/error messages
- Real-time validation
- Minimum/maximum checks

**Key Technologies**:
- Material-UI TextField, Dialog
- Form validation
- State management

### 4. Analytics Component

**Purpose**: Spending insights with visualizations

**Features**:
- Pie chart for spending by category
- Bar chart for monthly spending
- Summary statistics
- Interactive tooltips
- Responsive charts

**Key Technologies**:
- Recharts (PieChart, BarChart)
- Custom tooltips
- Data aggregation

## API Integration

### API Service Layer (`src/services/api.js`)

Centralized API communication with:
- Axios instance with default config
- Request/response interceptors
- Error handling
- Logging

**Available Methods**:
```javascript
apiService.getBalance(customerId)
apiService.getTransactions(customerId, limit)
apiService.getAnalytics(customerId)
apiService.transferToInvestment(customerId, amount)
apiService.getAuditLog()
apiService.getCustomers()
apiService.healthCheck()
apiService.customQuery(customerId, queryDescription)
```

### API Proxy Configuration

During development, Vite proxies API requests:
```javascript
// vite.config.js
server: {
  proxy: {
    '/api': 'http://localhost:5001',
    '/health': 'http://localhost:5001'
  }
}
```

## Routing

React Router provides client-side navigation:

| Route | Component | Description |
|-------|-----------|-------------|
| `/` | Redirect | Redirects to /dashboard |
| `/dashboard` | Dashboard | Account overview |
| `/transactions` | TransactionList | Transaction history |
| `/transfer` | TransferForm | Fund transfers |
| `/analytics` | Analytics | Spending insights |

## Theme & Styling

### Custom Theme

```javascript
const theme = createTheme({
  palette: {
    primary: {
      main: '#2E7D32',  // Green for Savings
      light: '#4CAF50',
      dark: '#1B5E20',
    },
    secondary: {
      main: '#66BB6A',
    },
  },
});
```

### Responsive Design

- Mobile-first approach
- Drawer navigation on mobile
- Grid system for layouts
- Breakpoints: xs, sm, md, lg, xl

## Development Workflow

### 1. Install Dependencies

```bash
cd bank1-savings/frontend
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

Access at: http://localhost:3000

### 3. Start Flask Backend

```bash
# In another terminal
cd bank1-savings
python app.py
```

Backend runs on: http://localhost:5001

### 4. Development Features

- **Hot Module Replacement**: Changes reflect instantly
- **API Proxy**: Seamless backend communication
- **Source Maps**: Easy debugging
- **Fast Refresh**: Preserves component state

## Production Build

### Build Process

```bash
cd bank1-savings/frontend
npm run build
```

Creates optimized build in `dist/` directory:
- Minified JavaScript
- Optimized CSS
- Compressed assets
- Source maps (optional)

### Serving Production Build

The Flask backend can serve the React build:

```python
# In app.py
from flask import send_from_directory

@app.route('/')
def serve_react():
    return send_from_directory('frontend/dist', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend/dist', path)
```

## Comparison: Bank 1 vs Bank 2

### Bank 1 (Savings) - React + Material-UI

**Pros**:
- ✅ Modern, professional UI
- ✅ Component reusability
- ✅ Better state management
- ✅ Easier to maintain and scale
- ✅ Rich ecosystem of libraries
- ✅ Better developer experience

**Cons**:
- ❌ Additional build step required
- ❌ Larger initial bundle size
- ❌ More complex setup

### Bank 2 (Investment) - Embedded HTML

**Pros**:
- ✅ Simple, no build process
- ✅ Smaller initial load
- ✅ Easy to understand
- ✅ No external dependencies

**Cons**:
- ❌ Harder to maintain as it grows
- ❌ Limited component reusability
- ❌ Manual DOM manipulation
- ❌ Less professional appearance

## Performance Optimization

### Code Splitting

React Router automatically splits code by route:
```javascript
// Each route loads only when accessed
<Route path="/dashboard" element={<Dashboard />} />
```

### Lazy Loading

For larger components:
```javascript
const Analytics = lazy(() => import('./components/Analytics'));
```

### Memoization

Prevent unnecessary re-renders:
```javascript
const MemoizedComponent = memo(Component);
```

## Testing

### Unit Tests (Future Enhancement)

```bash
npm install --save-dev @testing-library/react vitest
```

```javascript
// Dashboard.test.jsx
import { render, screen } from '@testing-library/react';
import Dashboard from './Dashboard';

test('renders balance', () => {
  render(<Dashboard customerId={1} customerName="Alice" />);
  expect(screen.getByText(/balance/i)).toBeInTheDocument();
});
```

## Deployment Options

### Option 1: Flask Serves React (Current)

Flask serves the React build as static files.

**Pros**: Single deployment, simple
**Cons**: Flask handles static file serving

### Option 2: Separate Deployment

React on CDN/Nginx, Flask as API only.

**Pros**: Better performance, scalability
**Cons**: CORS configuration needed

### Option 3: Docker Multi-Stage Build

```dockerfile
# Build React
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Flask with React build
FROM python:3.11
WORKDIR /app
COPY --from=frontend /app/frontend/dist ./frontend/dist
COPY requirements.txt app.py ./
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Future Enhancements

### Potential Additions

1. **Authentication**: JWT tokens, OAuth
2. **Real-time Updates**: WebSockets for live data
3. **Progressive Web App**: Offline support
4. **Advanced Charts**: More visualization options
5. **Dark Mode**: Theme switching
6. **Internationalization**: Multi-language support
7. **Accessibility**: Enhanced ARIA labels
8. **Performance Monitoring**: Analytics integration

## Troubleshooting

### Common Issues

**Issue**: API calls fail with CORS error
**Solution**: Ensure Vite proxy is configured correctly

**Issue**: Components not updating
**Solution**: Check React DevTools, verify state updates

**Issue**: Build fails
**Solution**: Clear node_modules, reinstall dependencies

**Issue**: Slow development server
**Solution**: Reduce number of open files, restart Vite

## Resources

### Documentation
- [React Docs](https://react.dev/)
- [Material-UI Docs](https://mui.com/)
- [Recharts Docs](https://recharts.org/)
- [Vite Docs](https://vitejs.dev/)

### Learning Resources
- [React Tutorial](https://react.dev/learn)
- [Material-UI Examples](https://mui.com/material-ui/getting-started/)
- [React Router Tutorial](https://reactrouter.com/en/main/start/tutorial)

## Summary

The React + Material-UI frontend for Bank 1 demonstrates:

1. **Modern Web Development**: Industry-standard tools and practices
2. **Professional UI**: Material Design components
3. **Maintainability**: Component-based architecture
4. **Scalability**: Easy to add new features
5. **Developer Experience**: Fast development with hot reload

This provides a stark contrast with Bank 2's embedded HTML, showcasing the benefits of modern frontend frameworks while maintaining backward compatibility with the existing Flask backend.