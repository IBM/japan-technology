import { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  CircularProgress,
  Alert,
  Chip,
} from '@mui/material';
import {
  AccountBalance,
  TrendingUp,
  SwapHoriz,
  Security,
} from '@mui/icons-material';
import apiService from '../services/api';

export default function Dashboard({ customerId, customerName }) {
  const [balance, setBalance] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadBalance();
  }, [customerId]);

  const loadBalance = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await apiService.getBalance(customerId);
      
      if (data.success && data.result_data && data.result_data.length > 0) {
        setBalance(data.result_data[0]);
      } else {
        setError('No balance data available');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Failed to load balance');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="400px">
        <CircularProgress size={60} />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error" sx={{ mb: 3 }}>
        {error}
      </Alert>
    );
  }

  return (
    <Box>
      {/* Welcome Header */}
      <Box mb={4}>
        <Typography variant="h4" gutterBottom fontWeight="bold" color="primary">
          Welcome back, {customerName}!
        </Typography>
        <Typography variant="body1" color="text.secondary">
          Here's your account overview
        </Typography>
      </Box>

      {/* Balance Cards */}
      <Grid container spacing={3}>
        {/* Main Balance Card */}
        <Grid item xs={12} md={6}>
          <Card 
            elevation={3}
            sx={{ 
              background: 'linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%)',
              color: 'white',
              height: '100%'
            }}
          >
            <CardContent>
              <Box display="flex" alignItems="center" mb={2}>
                <AccountBalance sx={{ fontSize: 40, mr: 2 }} />
                <Typography variant="h6">
                  Savings Account
                </Typography>
              </Box>
              <Typography variant="h3" fontWeight="bold" mb={1}>
                ${balance?.balance?.toFixed(2) || '0.00'}
              </Typography>
              <Typography variant="body2" sx={{ opacity: 0.9 }}>
                Available Balance
              </Typography>
              <Box mt={2}>
                <Chip 
                  label={balance?.account_type?.toUpperCase() || 'SAVINGS'} 
                  size="small"
                  sx={{ 
                    backgroundColor: 'rgba(255,255,255,0.2)',
                    color: 'white',
                    fontWeight: 'bold'
                  }}
                />
              </Box>
            </CardContent>
          </Card>
        </Grid>

        {/* Account Info Card */}
        <Grid item xs={12} md={6}>
          <Card elevation={3} sx={{ height: '100%' }}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={2}>
                <Security sx={{ fontSize: 40, mr: 2, color: 'primary.main' }} />
                <Typography variant="h6" color="primary">
                  Account Information
                </Typography>
              </Box>
              <Box mt={3}>
                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Account Holder
                </Typography>
                <Typography variant="h6" mb={2}>
                  {balance?.name || customerName}
                </Typography>
                
                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Email
                </Typography>
                <Typography variant="body1" mb={2}>
                  {balance?.email || 'N/A'}
                </Typography>
                
                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Account Type
                </Typography>
                <Typography variant="body1">
                  {balance?.account_type || 'Savings'}
                </Typography>
              </Box>
            </CardContent>
          </Card>
        </Grid>

        {/* Quick Stats */}
        <Grid item xs={12} md={4}>
          <Card elevation={2}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={1}>
                <TrendingUp sx={{ color: 'success.main', mr: 1 }} />
                <Typography variant="subtitle2" color="text.secondary">
                  Account Status
                </Typography>
              </Box>
              <Typography variant="h6" color="success.main">
                Active & Healthy
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card elevation={2}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={1}>
                <SwapHoriz sx={{ color: 'info.main', mr: 1 }} />
                <Typography variant="subtitle2" color="text.secondary">
                  Transfer Available
                </Typography>
              </Box>
              <Typography variant="h6" color="info.main">
                To Investment Bank
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card elevation={2}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={1}>
                <Security sx={{ color: 'primary.main', mr: 1 }} />
                <Typography variant="subtitle2" color="text.secondary">
                  Security
                </Typography>
              </Box>
              <Typography variant="h6" color="primary.main">
                Fully Protected
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Compliance Disclaimer */}
      <Box mt={4}>
        <Alert severity="info" variant="outlined">
          <Typography variant="caption">
            This banking information is provided for informational purposes only. 
            All transactions are subject to verification and regulatory compliance. 
            Customer data is protected under applicable privacy laws.
          </Typography>
        </Alert>
      </Box>
    </Box>
  );
}

// Made with Bob
