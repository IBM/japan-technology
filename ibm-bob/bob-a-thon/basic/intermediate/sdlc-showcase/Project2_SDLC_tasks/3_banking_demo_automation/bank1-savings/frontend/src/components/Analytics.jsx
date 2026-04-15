import { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  CircularProgress,
  Alert,
  Paper,
} from '@mui/material';
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Legend,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from 'recharts';
import { TrendingUp } from '@mui/icons-material';
import apiService from '../services/api';

const COLORS = ['#2E7D32', '#4CAF50', '#66BB6A', '#81C784', '#A5D6A7', '#C8E6C9'];

export default function Analytics({ customerId }) {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadAnalytics();
  }, [customerId]);

  const loadAnalytics = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await apiService.getAnalytics(customerId);
      
      if (data.success && data.result_data) {
        setAnalytics(data.result_data);
      } else {
        setError('No analytics data available');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Failed to load analytics');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Card>
        <CardContent>
          <Box display="flex" justifyContent="center" alignItems="center" minHeight="400px">
            <CircularProgress size={60} />
          </Box>
        </CardContent>
      </Card>
    );
  }

  if (error) {
    return (
      <Card>
        <CardContent>
          <Alert severity="error">{error}</Alert>
        </CardContent>
      </Card>
    );
  }

  // Prepare data for charts
  const categoryData = analytics?.by_category?.map(item => ({
    name: item.category || 'Other',
    value: Math.abs(item.total),
    count: item.count
  })) || [];

  const monthlyData = analytics?.monthly?.map(item => ({
    month: item.month || 'Unknown',
    amount: Math.abs(item.total),
    count: item.transaction_count
  })) || [];

  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <Paper sx={{ p: 2 }}>
          <Typography variant="body2" fontWeight="bold">
            {payload[0].name}
          </Typography>
          <Typography variant="body2" color="primary">
            Amount: ${payload[0].value.toFixed(2)}
          </Typography>
          {payload[0].payload.count && (
            <Typography variant="caption" color="text.secondary">
              Transactions: {payload[0].payload.count}
            </Typography>
          )}
        </Paper>
      );
    }
    return null;
  };

  return (
    <Box>
      <Box display="flex" alignItems="center" mb={3}>
        <TrendingUp sx={{ fontSize: 32, mr: 2, color: 'primary.main' }} />
        <Typography variant="h5" fontWeight="bold" color="primary">
          Spending Analytics
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* Spending by Category - Pie Chart */}
        <Grid item xs={12} md={6}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom fontWeight="bold">
                Spending by Category
              </Typography>
              {categoryData.length > 0 ? (
                <ResponsiveContainer width="100%" height={300}>
                  <PieChart>
                    <Pie
                      data={categoryData}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="value"
                    >
                      {categoryData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip content={<CustomTooltip />} />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              ) : (
                <Alert severity="info">No category data available</Alert>
              )}
            </CardContent>
          </Card>
        </Grid>

        {/* Monthly Spending - Bar Chart */}
        <Grid item xs={12} md={6}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom fontWeight="bold">
                Monthly Spending
              </Typography>
              {monthlyData.length > 0 ? (
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={monthlyData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="month" />
                    <YAxis />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="amount" fill="#2E7D32" />
                  </BarChart>
                </ResponsiveContainer>
              ) : (
                <Alert severity="info">No monthly data available</Alert>
              )}
            </CardContent>
          </Card>
        </Grid>

        {/* Summary Statistics */}
        <Grid item xs={12}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom fontWeight="bold">
                Summary Statistics
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={4}>
                  <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'success.light' }}>
                    <Typography variant="body2" color="white">
                      Total Categories
                    </Typography>
                    <Typography variant="h4" fontWeight="bold" color="white">
                      {categoryData.length}
                    </Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={4}>
                  <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'info.light' }}>
                    <Typography variant="body2" color="white">
                      Total Transactions
                    </Typography>
                    <Typography variant="h4" fontWeight="bold" color="white">
                      {categoryData.reduce((sum, item) => sum + (item.count || 0), 0)}
                    </Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={4}>
                  <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'primary.light' }}>
                    <Typography variant="body2" color="white">
                      Total Spending
                    </Typography>
                    <Typography variant="h4" fontWeight="bold" color="white">
                      ${categoryData.reduce((sum, item) => sum + (item.value || 0), 0).toFixed(2)}
                    </Typography>
                  </Paper>
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Info Box */}
      <Box mt={3}>
        <Alert severity="info" variant="outlined">
          <Typography variant="caption">
            Analytics are updated in real-time based on your transaction history. 
            Data is aggregated by category and month for better insights into your spending patterns.
          </Typography>
        </Alert>
      </Box>
    </Box>
  );
}

// Made with Bob
