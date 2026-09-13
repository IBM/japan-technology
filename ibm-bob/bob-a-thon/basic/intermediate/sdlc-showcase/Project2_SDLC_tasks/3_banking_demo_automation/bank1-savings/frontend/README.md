# Bank 1 - Savings Bank Frontend

## React + Material-UI Frontend

A modern, professional banking interface built with React and Material-UI.

## Features

- 📊 **Dashboard** - Account overview with balance cards
- 💳 **Transactions** - Detailed transaction history with filtering
- 💸 **Transfers** - Easy inter-bank transfers to Investment Bank
- 📈 **Analytics** - Spending insights with interactive charts

## Tech Stack

- **React 18** - Modern React with hooks
- **Material-UI (MUI)** - Professional UI components
- **Recharts** - Beautiful, responsive charts
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **Vite** - Fast build tool and dev server

## Development

### Prerequisites

- Node.js 18+ and npm
- Bank 1 Flask backend running on port 5001

### Install Dependencies

```bash
npm install
```

### Run Development Server

```bash
npm run dev
```

The app will be available at http://localhost:3000

The Vite dev server proxies API requests to the Flask backend at http://localhost:5001

### Build for Production

```bash
npm run build
```

This creates an optimized production build in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Dashboard.jsx    # Main dashboard
│   │   ├── TransactionList.jsx
│   │   ├── TransferForm.jsx
│   │   └── Analytics.jsx
│   ├── services/
│   │   └── api.js          # API service layer
│   ├── App.jsx             # Main app with routing
│   └── main.jsx            # Entry point
├── index.html              # HTML template
├── package.json            # Dependencies
└── vite.config.js          # Vite configuration
```

## API Integration

The frontend communicates with the Flask backend through the API service layer (`src/services/api.js`).

All API calls are proxied through Vite during development:
- `/api/*` → `http://localhost:5001/api/*`
- `/health` → `http://localhost:5001/health`

## Available Routes

- `/dashboard` - Account overview
- `/transactions` - Transaction history
- `/transfer` - Transfer funds
- `/analytics` - Spending analytics

## Customization

### Theme

The Material-UI theme is defined in `src/App.jsx`. The primary color is green (#2E7D32) to match the Savings Bank branding.

### API Endpoint

To change the backend API endpoint, update `vite.config.js`:

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://your-backend-url',
      changeOrigin: true,
    }
  }
}
```

## Deployment

The production build can be served by:
1. Flask (static files)
2. Nginx
3. Any static file server

The Flask backend is configured to serve the React build from the `dist/` directory.