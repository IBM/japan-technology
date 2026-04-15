import { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Chip,
  CircularProgress,
  Alert,
  IconButton,
  Tooltip,
} from '@mui/material';
import {
  Refresh,
  TrendingUp,
  TrendingDown,
  SwapHoriz,
} from '@mui/icons-material';
import { format } from 'date-fns';
import apiService from '../services/api';

export default function TransactionList({ customerId }) {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadTransactions();
  }, [customerId]);

  const loadTransactions = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await apiService.getTransactions(customerId, 20);
      
      if (data.success && data.result_data) {
        // Ensure we always have an array
        const transactionsArray = Array.isArray(data.result_data) ? data.result_data : [];
        setTransactions(transactionsArray);
      } else {
        setError('No transaction data available');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Failed to load transactions');
    } finally {
      setLoading(false);
    }
  };

  const getTransactionIcon = (type) => {
    switch (type?.toLowerCase()) {
      case 'deposit':
        return <TrendingUp color="success" />;
      case 'withdrawal':
        return <TrendingDown color="error" />;
      case 'transfer':
        return <SwapHoriz color="info" />;
      default:
        return <SwapHoriz color="action" />;
    }
  };

  const getTransactionColor = (type) => {
    switch (type?.toLowerCase()) {
      case 'deposit':
        return 'success';
      case 'withdrawal':
        return 'error';
      case 'transfer':
        return 'info';
      default:
        return 'default';
    }
  };

  const formatDate = (dateString) => {
    try {
      return format(new Date(dateString), 'MMM dd, yyyy HH:mm');
    } catch {
      return dateString;
    }
  };

  const formatAmount = (amount, type) => {
    const absAmount = Math.abs(amount);
    const sign = type?.toLowerCase() === 'deposit' ? '+' : '-';
    return `${sign}$${absAmount.toFixed(2)}`;
  };

  if (loading) {
    return (
      <Card>
        <CardContent>
          <Box display="flex" justifyContent="center" alignItems="center" minHeight="300px">
            <CircularProgress />
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

  return (
    <Card elevation={3}>
      <CardContent>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
          <Typography variant="h5" fontWeight="bold" color="primary">
            Recent Transactions
          </Typography>
          <Tooltip title="Refresh">
            <IconButton onClick={loadTransactions} color="primary">
              <Refresh />
            </IconButton>
          </Tooltip>
        </Box>

        {transactions.length === 0 ? (
          <Alert severity="info">No transactions found</Alert>
        ) : (
          <TableContainer component={Paper} variant="outlined">
            <Table>
              <TableHead>
                <TableRow sx={{ backgroundColor: 'primary.light' }}>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>Type</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>Category</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>Description</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }} align="right">Amount</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>Date</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {transactions.map((transaction, index) => (
                  <TableRow 
                    key={transaction.transaction_id || index}
                    hover
                    sx={{ 
                      '&:nth-of-type(odd)': { backgroundColor: 'action.hover' },
                      '&:hover': { backgroundColor: 'action.selected' }
                    }}
                  >
                    <TableCell>
                      <Box display="flex" alignItems="center" gap={1}>
                        {getTransactionIcon(transaction.transaction_type)}
                        <Chip 
                          label={transaction.transaction_type || 'N/A'}
                          size="small"
                          color={getTransactionColor(transaction.transaction_type)}
                        />
                      </Box>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2">
                        {transaction.category || 'General'}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2">
                        {transaction.description || 'No description'}
                      </Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography 
                        variant="body1" 
                        fontWeight="bold"
                        color={
                          transaction.transaction_type?.toLowerCase() === 'deposit' 
                            ? 'success.main' 
                            : 'error.main'
                        }
                      >
                        {formatAmount(transaction.amount, transaction.transaction_type)}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2" color="text.secondary">
                        {formatDate(transaction.transaction_date)}
                      </Typography>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}

        <Box mt={2}>
          <Typography variant="caption" color="text.secondary">
            Showing {transactions.length} most recent transactions
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
}

// Made with Bob
