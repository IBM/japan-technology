import { useState } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Alert,
  CircularProgress,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Divider,
} from '@mui/material';
import {
  Send,
  CheckCircle,
  Error as ErrorIcon,
} from '@mui/icons-material';
import apiService from '../services/api';

export default function TransferForm({ customerId, currentBalance, onTransferComplete }) {
  const [amount, setAmount] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const [confirmDialog, setConfirmDialog] = useState(false);

  const handleAmountChange = (e) => {
    const value = e.target.value;
    // Only allow numbers and decimal point
    if (value === '' || /^\d*\.?\d{0,2}$/.test(value)) {
      setAmount(value);
      setError(null);
    }
  };

  const validateAmount = () => {
    const numAmount = parseFloat(amount);
    
    if (!amount || numAmount <= 0) {
      setError('Please enter a valid amount');
      return false;
    }
    
    if (numAmount > currentBalance) {
      setError(`Insufficient funds. Available balance: $${currentBalance.toFixed(2)}`);
      return false;
    }
    
    if (numAmount < 1) {
      setError('Minimum transfer amount is $1.00');
      return false;
    }
    
    return true;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateAmount()) {
      setConfirmDialog(true);
    }
  };

  const handleConfirmTransfer = async () => {
    setConfirmDialog(false);
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      const data = await apiService.transferToInvestment(customerId, amount);
      
      if (data.success) {
        setSuccess({
          message: `Successfully transferred $${parseFloat(amount).toFixed(2)} to Investment Bank`,
          newBalance: data.result_data?.new_savings_balance
        });
        setAmount('');
        
        // Notify parent component to refresh data
        if (onTransferComplete) {
          onTransferComplete();
        }
      } else {
        setError(data.error || 'Transfer failed');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Transfer failed');
    } finally {
      setLoading(false);
    }
  };

  const handleCancelTransfer = () => {
    setConfirmDialog(false);
  };

  return (
    <Card elevation={3}>
      <CardContent>
        <Box display="flex" alignItems="center" mb={3}>
          <Send sx={{ fontSize: 32, mr: 2, color: 'primary.main' }} />
          <Typography variant="h5" fontWeight="bold" color="primary">
            Transfer to Investment Bank
          </Typography>
        </Box>

        <Divider sx={{ mb: 3 }} />

        {/* Current Balance Display */}
        <Box mb={3} p={2} bgcolor="primary.light" borderRadius={1}>
          <Typography variant="body2" color="white" gutterBottom>
            Available Balance
          </Typography>
          <Typography variant="h4" fontWeight="bold" color="white">
            ${currentBalance?.toFixed(2) || '0.00'}
          </Typography>
        </Box>

        {/* Transfer Form */}
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Transfer Amount"
            value={amount}
            onChange={handleAmountChange}
            placeholder="0.00"
            InputProps={{
              startAdornment: <Typography sx={{ mr: 1 }}>$</Typography>,
            }}
            disabled={loading}
            error={!!error}
            helperText={error || 'Enter amount to transfer to your Investment account'}
            sx={{ mb: 3 }}
          />

          <Button
            type="submit"
            variant="contained"
            size="large"
            fullWidth
            disabled={loading || !amount}
            startIcon={loading ? <CircularProgress size={20} /> : <Send />}
            sx={{ mb: 2 }}
          >
            {loading ? 'Processing...' : 'Transfer Funds'}
          </Button>
        </form>

        {/* Success Message */}
        {success && (
          <Alert 
            severity="success" 
            icon={<CheckCircle />}
            sx={{ mt: 2 }}
          >
            <Typography variant="body2" fontWeight="bold">
              {success.message}
            </Typography>
            {success.newBalance && (
              <Typography variant="caption">
                New balance: ${success.newBalance.toFixed(2)}
              </Typography>
            )}
          </Alert>
        )}

        {/* Info Box */}
        <Box mt={3} p={2} bgcolor="info.light" borderRadius={1}>
          <Typography variant="caption" color="info.dark">
            <strong>Note:</strong> Transfers are processed immediately and will appear in both accounts. 
            All transfers are subject to dual-run validation for security.
          </Typography>
        </Box>
      </CardContent>

      {/* Confirmation Dialog */}
      <Dialog open={confirmDialog} onClose={handleCancelTransfer}>
        <DialogTitle>
          <Box display="flex" alignItems="center">
            <Send sx={{ mr: 1, color: 'primary.main' }} />
            Confirm Transfer
          </Box>
        </DialogTitle>
        <DialogContent>
          <Typography variant="body1" gutterBottom>
            You are about to transfer:
          </Typography>
          <Typography variant="h4" color="primary" fontWeight="bold" my={2}>
            ${parseFloat(amount).toFixed(2)}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            From: <strong>Savings Bank</strong>
          </Typography>
          <Typography variant="body2" color="text.secondary" mb={2}>
            To: <strong>Investment Bank</strong>
          </Typography>
          <Alert severity="warning" sx={{ mt: 2 }}>
            This action cannot be undone. Please confirm to proceed.
          </Alert>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCancelTransfer} color="inherit">
            Cancel
          </Button>
          <Button 
            onClick={handleConfirmTransfer} 
            variant="contained" 
            color="primary"
            startIcon={<Send />}
          >
            Confirm Transfer
          </Button>
        </DialogActions>
      </Dialog>
    </Card>
  );
}

// Made with Bob
