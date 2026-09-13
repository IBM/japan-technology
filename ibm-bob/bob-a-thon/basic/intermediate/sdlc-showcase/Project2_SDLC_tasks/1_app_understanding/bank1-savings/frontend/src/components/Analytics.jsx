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
import {
  formatJapaneseDay,
  formatJapaneseMonth,
  translateCategory,
} from '../utils/labels';

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
        setError('分析データがありません');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message || '分析データの取得に失敗しました');
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
  const categorySource = analytics?.by_category || analytics?.category_breakdown || [];
  const categoryData = categorySource.map((item) => ({
    name: translateCategory(item.category || item.name || 'other'),
    value: Math.abs(item.total ?? item.total_amount ?? item.value ?? 0),
    count: item.count || item.transaction_count || 0,
  }));

  const trendSource = analytics?.monthly || analytics?.daily_spending || [];
  const trendData = trendSource.map((item) => ({
    label: item.month ? formatJapaneseMonth(item.month) : formatJapaneseDay(item.date),
    amount: Math.abs(item.total ?? item.total_amount ?? item.amount ?? 0),
    count: item.transaction_count || item.count || 0,
  }));

  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <Paper sx={{ p: 2 }}>
          <Typography variant="body2" fontWeight="bold">
            {payload[0].name}
          </Typography>
          <Typography variant="body2" color="primary">
            金額: ${payload[0].value.toFixed(2)}
          </Typography>
          {payload[0].payload.count && (
            <Typography variant="caption" color="text.secondary">
              件数: {payload[0].payload.count}
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
          支出分析
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* Spending by Category - Pie Chart */}
        <Grid item xs={12} md={6}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom fontWeight="bold">
                カテゴリ別支出
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
                <Alert severity="info">カテゴリ別データがありません</Alert>
              )}
            </CardContent>
          </Card>
        </Grid>

        {/* Monthly Spending - Bar Chart */}
        <Grid item xs={12} md={6}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom fontWeight="bold">
                支出の推移
              </Typography>
              {trendData.length > 0 ? (
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={trendData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="label" />
                    <YAxis />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="amount" fill="#2E7D32" />
                  </BarChart>
                </ResponsiveContainer>
              ) : (
                <Alert severity="info">時系列データがありません</Alert>
              )}
            </CardContent>
          </Card>
        </Grid>

        {/* Summary Statistics */}
        <Grid item xs={12}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom fontWeight="bold">
                サマリー
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={4}>
                  <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'success.light' }}>
                    <Typography variant="body2" color="white">
                      カテゴリ数
                    </Typography>
                    <Typography variant="h4" fontWeight="bold" color="white">
                      {categoryData.length}
                    </Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={4}>
                  <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'info.light' }}>
                    <Typography variant="body2" color="white">
                      時系列データ数
                    </Typography>
                    <Typography variant="h4" fontWeight="bold" color="white">
                      {trendData.length}
                    </Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={4}>
                  <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'primary.light' }}>
                    <Typography variant="body2" color="white">
                      総支出額
                    </Typography>
                    <Typography variant="h4" fontWeight="bold" color="white">
                      ${Number(analytics?.total_spent || categoryData.reduce((sum, item) => sum + (item.value || 0), 0)).toFixed(2)}
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
            分析結果は取引履歴に基づいて随時更新されます。
            支出傾向を把握しやすいように、カテゴリ別および時系列で集計しています。
          </Typography>
        </Alert>
      </Box>
    </Box>
  );
}

// Made with Bob
