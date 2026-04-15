import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import {
  ThemeProvider,
  createTheme,
  CssBaseline,
  Box,
  AppBar,
  Toolbar,
  Typography,
  Container,
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  ListItemButton,
  IconButton,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Divider,
  Alert,
} from '@mui/material';
import {
  Menu as MenuIcon,
  Dashboard as DashboardIcon,
  Receipt,
  Send,
  BarChart,
  AccountBalance,
} from '@mui/icons-material';
import { useNavigate, useLocation } from 'react-router-dom';

import Dashboard from './components/Dashboard';
import TransactionList from './components/TransactionList';
import TransferForm from './components/TransferForm';
import Analytics from './components/Analytics';
import apiService from './services/api';

// Create Material-UI theme with green color scheme
const theme = createTheme({
  palette: {
    primary: {
      main: '#2E7D32',
      light: '#4CAF50',
      dark: '#1B5E20',
    },
    secondary: {
      main: '#66BB6A',
    },
    success: {
      main: '#4CAF50',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h4: {
      fontWeight: 600,
    },
    h5: {
      fontWeight: 600,
    },
  },
});

const drawerWidth = 240;

const menuItems = [
  { text: 'Dashboard', icon: <DashboardIcon />, path: '/dashboard' },
  { text: 'Transactions', icon: <Receipt />, path: '/transactions' },
  { text: 'Transfer', icon: <Send />, path: '/transfer' },
  { text: 'Analytics', icon: <BarChart />, path: '/analytics' },
];

// Mock customers - in production, this would come from API
const customers = [
  { id: 1, name: 'Alice Johnson' },
  { id: 2, name: 'Bob Smith' },
  { id: 3, name: 'Charlie Brown' },
];

function AppContent() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [customerId, setCustomerId] = useState(1);
  const [customerName, setCustomerName] = useState('Alice Johnson');
  const [balance, setBalance] = useState(0);
  const [refreshKey, setRefreshKey] = useState(0);
  
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    loadBalance();
  }, [customerId, refreshKey]);

  const loadBalance = async () => {
    try {
      const data = await apiService.getBalance(customerId);
      if (data.success && data.result_data && data.result_data.length > 0) {
        setBalance(data.result_data[0].balance);
      }
    } catch (err) {
      console.error('Failed to load balance:', err);
    }
  };

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const handleCustomerChange = (event) => {
    const newCustomerId = event.target.value;
    setCustomerId(newCustomerId);
    const customer = customers.find(c => c.id === newCustomerId);
    setCustomerName(customer?.name || 'Customer');
  };

  const handleTransferComplete = () => {
    setRefreshKey(prev => prev + 1);
  };

  const drawer = (
    <Box>
      <Toolbar sx={{ bgcolor: 'primary.main', color: 'white' }}>
        <AccountBalance sx={{ mr: 2 }} />
        <Typography variant="h6" noWrap>
          Savings Bank
        </Typography>
      </Toolbar>
      <Divider />
      <List>
        {menuItems.map((item) => (
          <ListItem key={item.text} disablePadding>
            <ListItemButton
              selected={location.pathname === item.path}
              onClick={() => {
                navigate(item.path);
                setMobileOpen(false);
              }}
            >
              <ListItemIcon sx={{ color: location.pathname === item.path ? 'primary.main' : 'inherit' }}>
                {item.icon}
              </ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      
      {/* App Bar */}
      <AppBar
        position="fixed"
        sx={{
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          ml: { sm: `${drawerWidth}px` },
        }}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: 'none' } }}
          >
            <MenuIcon />
          </IconButton>
          
          <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
            Bank 1 - Savings Bank
          </Typography>

          {/* Customer Selector */}
          <FormControl variant="outlined" size="small" sx={{ minWidth: 200, bgcolor: 'white', borderRadius: 1 }}>
            <InputLabel>Customer</InputLabel>
            <Select
              value={customerId}
              onChange={handleCustomerChange}
              label="Customer"
            >
              {customers.map((customer) => (
                <MenuItem key={customer.id} value={customer.id}>
                  {customer.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Toolbar>
      </AppBar>

      {/* Drawer */}
      <Box
        component="nav"
        sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
      >
        <Drawer
          variant="temporary"
          open={mobileOpen}
          onClose={handleDrawerToggle}
          ModalProps={{ keepMounted: true }}
          sx={{
            display: { xs: 'block', sm: 'none' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
        >
          {drawer}
        </Drawer>
        <Drawer
          variant="permanent"
          sx={{
            display: { xs: 'none', sm: 'block' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
          open
        >
          {drawer}
        </Drawer>
      </Box>

      {/* Main Content */}
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          mt: 8,
        }}
      >
        <Container maxWidth="lg">
          <Routes>
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route 
              path="/dashboard" 
              element={<Dashboard customerId={customerId} customerName={customerName} />} 
            />
            <Route 
              path="/transactions" 
              element={<TransactionList customerId={customerId} />} 
            />
            <Route 
              path="/transfer" 
              element={
                <TransferForm 
                  customerId={customerId} 
                  currentBalance={balance}
                  onTransferComplete={handleTransferComplete}
                />
              } 
            />
            <Route 
              path="/analytics" 
              element={<Analytics customerId={customerId} />} 
            />
          </Routes>
        </Container>
      </Box>
    </Box>
  );
}

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <AppContent />
      </Router>
    </ThemeProvider>
  );
}

// Made with Bob
