import { format } from 'date-fns';
import { ja } from 'date-fns/locale';

const accountTypeLabels = {
  savings: '普通預金',
  investment: '投資口座',
};

const transactionTypeLabels = {
  deposit: '入金',
  withdrawal: '出金',
  transfer: '振替',
  dividend: '配当',
};

const categoryLabels = {
  salary: '給与',
  groceries: '食料品',
  utilities: '公共料金',
  entertainment: '娯楽',
  transfer: '振替',
  stocks: '株式',
  bonds: '債券',
  mutual_funds: '投資信託',
  etf: 'ETF',
  other: 'その他',
};

const descriptionLabels = {
  'Monthly salary': '月給',
  Supermarket: 'スーパーマーケット',
  'Electric bill': '電気料金',
  'Movie tickets': '映画チケット',
  'Weekly shopping': '週次の買い物',
  'Transfer to Investment Bank': 'Investment Bank への振替',
  'Transfer from Investment Bank': 'Investment Bank からの振替',
  'Transfer to Savings Bank': 'Savings Bank への振替',
  'Transfer from Savings Bank': 'Savings Bank からの振替',
  'Stock purchase - Tech sector': '株式購入 - テックセクター',
  'Quarterly dividend': '四半期配当',
  'Bond investment': '債券投資',
  'Stock purchase - Healthcare': '株式購入 - ヘルスケア',
  'Dividend payment': '配当金支払い',
  'Mutual fund investment': '投資信託への投資',
  'Stock sale': '株式売却',
  'Bond purchase': '債券購入',
  'ETF investment': 'ETF 投資',
};

function translateFromMap(value, labels, fallback = '未設定') {
  if (value === null || value === undefined || value === '') {
    return fallback;
  }

  const key = String(value).trim().toLowerCase();
  return labels[key] || String(value);
}

export function translateAccountType(value) {
  return translateFromMap(value, accountTypeLabels);
}

export function translateTransactionType(value) {
  return translateFromMap(value, transactionTypeLabels, '不明');
}

export function translateCategory(value) {
  return translateFromMap(value, categoryLabels, 'その他');
}

export function translateDescription(value) {
  if (!value) {
    return '説明なし';
  }

  return descriptionLabels[value] || value;
}

export function formatJapaneseDate(value) {
  try {
    return format(new Date(value), 'yyyy/MM/dd HH:mm', { locale: ja });
  } catch {
    return value;
  }
}

export function formatJapaneseDay(value) {
  try {
    return format(new Date(value), 'yyyy/MM/dd', { locale: ja });
  } catch {
    return value;
  }
}

export function formatJapaneseMonth(value) {
  try {
    return format(new Date(`${value}-01T00:00:00`), 'yyyy年M月', { locale: ja });
  } catch {
    return value;
  }
}
