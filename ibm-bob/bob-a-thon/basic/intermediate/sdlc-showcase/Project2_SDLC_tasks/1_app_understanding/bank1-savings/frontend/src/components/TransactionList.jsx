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
import apiService from '../services/api';
import {
  formatJapaneseDate,
  translateCategory,
  translateDescription,
  translateTransactionType,
} from '../utils/labels';

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
        setError('取引データがありません');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || '取引履歴の取得に失敗しました');
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
    return formatJapaneseDate(dateString);
  };

  const formatAmount = (amount, type) => {
    const absAmount = Math.abs(amount);
    const sign = amount >= 0 || type?.toLowerCase() === 'deposit' ? '+' : '-';
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
            最新の取引履歴
          </Typography>
          <Tooltip title="再読み込み">
            <IconButton onClick={loadTransactions} color="primary">
              <Refresh />
            </IconButton>
          </Tooltip>
        </Box>

        {transactions.length === 0 ? (
          <Alert severity="info">取引履歴がありません</Alert>
        ) : (
          <TableContainer component={Paper} variant="outlined">
            <Table>
              <TableHead>
                <TableRow sx={{ backgroundColor: 'primary.light' }}>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>種別</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>カテゴリ</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>説明</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }} align="right">金額</TableCell>
                  <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>日時</TableCell>
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
                          label={translateTransactionType(transaction.transaction_type)}
                          size="small"
                          color={getTransactionColor(transaction.transaction_type)}
                        />
                      </Box>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2">
                        {translateCategory(transaction.category)}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2">
                        {translateDescription(transaction.description)}
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
            最新 {transactions.length} 件の取引を表示しています
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
}

// Made with Bob
