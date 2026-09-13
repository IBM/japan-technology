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
      setError('有効な金額を入力してください');
      return false;
    }
    
    if (numAmount > currentBalance) {
      setError(`残高不足です。利用可能残高: $${currentBalance.toFixed(2)}`);
      return false;
    }
    
    if (numAmount < 1) {
      setError('最小振替額は $1.00 です');
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
          message: `Investment Bank へ $${parseFloat(amount).toFixed(2)} を振り替えました`,
          newBalance: data.result_data?.new_savings_balance
        });
        setAmount('');
        
        // Notify parent component to refresh data
        if (onTransferComplete) {
          onTransferComplete();
        }
      } else {
        setError(data.error || '振替に失敗しました');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || '振替に失敗しました');
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
            Investment Bank への振替
          </Typography>
        </Box>

        <Divider sx={{ mb: 3 }} />

        {/* Current Balance Display */}
        <Box mb={3} p={2} bgcolor="primary.light" borderRadius={1}>
          <Typography variant="body2" color="white" gutterBottom>
            利用可能残高
          </Typography>
          <Typography variant="h4" fontWeight="bold" color="white">
            ${currentBalance?.toFixed(2) || '0.00'}
          </Typography>
        </Box>

        {/* Transfer Form */}
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="振替金額"
            value={amount}
            onChange={handleAmountChange}
            placeholder="0.00"
            InputProps={{
              startAdornment: <Typography sx={{ mr: 1 }}>$</Typography>,
            }}
            disabled={loading}
            error={!!error}
            helperText={error || 'Investment Bank 口座へ振り替える金額を入力してください'}
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
            {loading ? '処理中...' : '振替を実行'}
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
                新しい残高: ${success.newBalance.toFixed(2)}
              </Typography>
            )}
          </Alert>
        )}

        {/* Info Box */}
        <Box mt={3} p={2} bgcolor="info.light" borderRadius={1}>
          <Typography variant="caption" color="info.dark">
            <strong>補足:</strong> 振替は即時処理され、両方の口座に反映されます。
            すべての振替はセキュリティのために dual-run validation の対象です。
          </Typography>
        </Box>
      </CardContent>

      {/* Confirmation Dialog */}
      <Dialog open={confirmDialog} onClose={handleCancelTransfer}>
        <DialogTitle>
          <Box display="flex" alignItems="center">
            <Send sx={{ mr: 1, color: 'primary.main' }} />
            振替内容の確認
          </Box>
        </DialogTitle>
        <DialogContent>
          <Typography variant="body1" gutterBottom>
            次の内容で振替を実行します:
          </Typography>
          <Typography variant="h4" color="primary" fontWeight="bold" my={2}>
            ${parseFloat(amount).toFixed(2)}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            振替元: <strong>Savings Bank</strong>
          </Typography>
          <Typography variant="body2" color="text.secondary" mb={2}>
            振替先: <strong>Investment Bank</strong>
          </Typography>
          <Alert severity="warning" sx={{ mt: 2 }}>
            この操作は取り消せません。問題なければ実行してください。
          </Alert>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCancelTransfer} color="inherit">
            キャンセル
          </Button>
          <Button 
            onClick={handleConfirmTransfer} 
            variant="contained" 
            color="primary"
            startIcon={<Send />}
          >
            振替を確定
          </Button>
        </DialogActions>
      </Dialog>
    </Card>
  );
}

// Made with Bob
