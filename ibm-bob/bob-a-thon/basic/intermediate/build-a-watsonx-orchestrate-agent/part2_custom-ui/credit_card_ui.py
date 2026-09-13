"""
クレジットカード管理アプリケーション - Web UI
Streamlitベースのクレジットカード管理ダッシュボード

Author: Bob AI Assistant
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# モジュールインポートのために親ディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wxo.wxo_agent_adapter import WxOAgentAdapter

# ページ設定
st.set_page_config(
    page_title="クレジットカード管理",
    page_icon="💳",
    layout="wide"
)

# カスタムCSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .category-badge {
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# モックトランザクションデータを生成
@st.cache_data
def generate_mock_transactions():
    """15-20件のモックトランザクションデータを生成"""
    base_date = datetime.now()
    
    transactions = [
        {
            "transaction_id": "TXN001",
            "date": (base_date - timedelta(days=2)).strftime("%Y-%m-%d"),
            "merchant": "Amazon",
            "category": "retail",
            "amount": 89.99,
            "description": "電子機器購入",
            "status": "completed"
        },
        {
            "transaction_id": "TXN002",
            "date": (base_date - timedelta(days=5)).strftime("%Y-%m-%d"),
            "merchant": "Netflix",
            "category": "subscription",
            "amount": 15.99,
            "description": "月額サブスクリプション",
            "status": "completed"
        },
        {
            "transaction_id": "TXN003",
            "date": (base_date - timedelta(days=7)).strftime("%Y-%m-%d"),
            "merchant": "Delta Airlines",
            "category": "travel",
            "amount": 450.00,
            "description": "航空券",
            "status": "completed"
        },
        {
            "transaction_id": "TXN004",
            "date": (base_date - timedelta(days=8)).strftime("%Y-%m-%d"),
            "merchant": "Whole Foods",
            "category": "groceries",
            "amount": 127.45,
            "description": "食料品",
            "status": "completed"
        },
        {
            "transaction_id": "TXN005",
            "date": (base_date - timedelta(days=10)).strftime("%Y-%m-%d"),
            "merchant": "Shell",
            "category": "gas",
            "amount": 52.30,
            "description": "ガソリン",
            "status": "completed"
        },
        {
            "transaction_id": "TXN006",
            "date": (base_date - timedelta(days=12)).strftime("%Y-%m-%d"),
            "merchant": "Spotify",
            "category": "subscription",
            "amount": 9.99,
            "description": "音楽ストリーミング",
            "status": "completed"
        },
        {
            "transaction_id": "TXN007",
            "date": (base_date - timedelta(days=13)).strftime("%Y-%m-%d"),
            "merchant": "Target",
            "category": "retail",
            "amount": 156.78,
            "description": "日用品",
            "status": "completed"
        },
        {
            "transaction_id": "TXN008",
            "date": (base_date - timedelta(days=15)).strftime("%Y-%m-%d"),
            "merchant": "Marriott Hotel",
            "category": "travel",
            "amount": 289.00,
            "description": "ホテル宿泊",
            "status": "completed"
        },
        {
            "transaction_id": "TXN009",
            "date": (base_date - timedelta(days=16)).strftime("%Y-%m-%d"),
            "merchant": "Trader Joe's",
            "category": "groceries",
            "amount": 84.32,
            "description": "食料品",
            "status": "completed"
        },
        {
            "transaction_id": "TXN010",
            "date": (base_date - timedelta(days=18)).strftime("%Y-%m-%d"),
            "merchant": "Chevron",
            "category": "gas",
            "amount": 48.75,
            "description": "ガソリン",
            "status": "completed"
        },
        {
            "transaction_id": "TXN011",
            "date": (base_date - timedelta(days=19)).strftime("%Y-%m-%d"),
            "merchant": "Adobe",
            "category": "subscription",
            "amount": 54.99,
            "description": "Creative Cloudサブスクリプション",
            "status": "completed"
        },
        {
            "transaction_id": "TXN012",
            "date": (base_date - timedelta(days=20)).strftime("%Y-%m-%d"),
            "merchant": "Best Buy",
            "category": "retail",
            "amount": 234.50,
            "description": "電子機器",
            "status": "completed"
        },
        {
            "transaction_id": "TXN013",
            "date": (base_date - timedelta(days=22)).strftime("%Y-%m-%d"),
            "merchant": "Uber",
            "category": "travel",
            "amount": 32.45,
            "description": "配車サービス",
            "status": "completed"
        },
        {
            "transaction_id": "TXN014",
            "date": (base_date - timedelta(days=23)).strftime("%Y-%m-%d"),
            "merchant": "Safeway",
            "category": "groceries",
            "amount": 95.67,
            "description": "食料品",
            "status": "completed"
        },
        {
            "transaction_id": "TXN015",
            "date": (base_date - timedelta(days=25)).strftime("%Y-%m-%d"),
            "merchant": "76 Gas Station",
            "category": "gas",
            "amount": 55.20,
            "description": "ガソリン",
            "status": "completed"
        },
        {
            "transaction_id": "TXN016",
            "date": (base_date - timedelta(days=26)).strftime("%Y-%m-%d"),
            "merchant": "Apple",
            "category": "retail",
            "amount": 299.00,
            "description": "AirPods Pro",
            "status": "completed"
        },
        {
            "transaction_id": "TXN017",
            "date": (base_date - timedelta(days=27)).strftime("%Y-%m-%d"),
            "merchant": "Disney+",
            "category": "subscription",
            "amount": 7.99,
            "description": "ストリーミングサービス",
            "status": "completed"
        },
        {
            "transaction_id": "TXN018",
            "date": (base_date - timedelta(days=28)).strftime("%Y-%m-%d"),
            "merchant": "Costco",
            "category": "groceries",
            "amount": 178.90,
            "description": "大量購入",
            "status": "completed"
        },
    ]
    
    return pd.DataFrame(transactions)

# WxO Agent Adapterを初期化
@st.cache_resource
def get_wxo_adapter():
    """WxOAgentAdapterのシングルトンインスタンスを取得"""
    return WxOAgentAdapter()

# セッション状態を初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

if "transactions_df" not in st.session_state:
    st.session_state.transactions_df = generate_mock_transactions()

# メインヘッダー
st.markdown('<div class="main-header">💳 クレジットカード管理ダッシュボード</div>', unsafe_allow_html=True)

# データフレームを取得
df = st.session_state.transactions_df

# セクションA: ダッシュボードヘッダー（サマリー統計）
st.markdown("### 📊 概要")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_spending = df['amount'].sum()
    st.metric(
        label="💰 総支出",
        value=f"${total_spending:,.2f}"
    )

with col2:
    transaction_count = len(df)
    st.metric(
        label="📝 取引件数",
        value=f"{transaction_count}"
    )

with col3:
    avg_transaction = df['amount'].mean()
    st.metric(
        label="📈 平均取引額",
        value=f"${avg_transaction:,.2f}"
    )

with col4:
    # 今月の支出（過去30日）
    current_month_spending = total_spending  # すべてのデータが過去30日以内
    st.metric(
        label="📅 今月の支出",
        value=f"${current_month_spending:,.2f}"
    )

st.divider()

# セクションB: 可視化（グラフ）
st.markdown("### 📊 支出分析")

graph_col1, graph_col2 = st.columns(2)

with graph_col1:
    st.markdown("#### カテゴリ別支出")
    
    # カテゴリ別の支出を集計
    category_spending = df.groupby('category')['amount'].sum().reset_index()
    category_spending = category_spending.sort_values('amount', ascending=False)
    
    # カテゴリ名を日本語に変換
    category_names = {
        'retail': '小売',
        'subscription': 'サブスクリプション',
        'travel': '旅行',
        'groceries': '食料品',
        'gas': 'ガソリン'
    }
    category_spending['category_jp'] = category_spending['category'].map(category_names)
    
    # 円グラフを作成
    fig_pie = px.pie(
        category_spending,
        values='amount',
        names='category_jp',
        title='',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with graph_col2:
    st.markdown("#### 時系列の支出")
    
    # 日付でソート
    df_sorted = df.sort_values('date')
    df_sorted['date'] = pd.to_datetime(df_sorted['date'])
    
    # 日次支出の折れ線グラフ
    fig_line = px.line(
        df_sorted,
        x='date',
        y='amount',
        title='',
        markers=True
    )
    fig_line.update_layout(
        xaxis_title="日付",
        yaxis_title="金額 ($)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# セクションC: トランザクションリスト
st.markdown("### 📋 取引履歴")

# フィルタリングオプション
filter_col1, filter_col2 = st.columns([1, 3])

with filter_col1:
    category_filter = st.multiselect(
        "カテゴリでフィルタ",
        options=['すべて'] + list(df['category'].unique()),
        default=['すべて']
    )

# フィルタリングを適用
if 'すべて' not in category_filter and len(category_filter) > 0:
    filtered_df = df[df['category'].isin(category_filter)]
else:
    filtered_df = df

# データフレームの表示用に列名を日本語化
display_df = filtered_df.copy()
display_df['category_jp'] = display_df['category'].map(category_names)
display_df = display_df[['transaction_id', 'date', 'merchant', 'category_jp', 'amount', 'description', 'status']]
display_df.columns = ['取引ID', '日付', '加盟店', 'カテゴリ', '金額', '説明', 'ステータス']

# データフレームを表示（ソート可能）
st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "金額": st.column_config.NumberColumn(
            "金額",
            format="$%.2f"
        ),
        "日付": st.column_config.DateColumn(
            "日付",
            format="YYYY-MM-DD"
        )
    }
)

st.divider()

# セクションD: チャットインターフェース
st.markdown("### 💬 AIアシスタント")
st.caption("取引について質問してください")

# チャット履歴を表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# チャット入力
if prompt := st.chat_input("例: 「サブスクリプション料金は何ですか？」"):
    # ユーザーメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI応答を取得
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # WxO Adapterを取得
            wxo_adapter = get_wxo_adapter()
            
            accumulated_response = []
            returned_thread_id = None
            
            # route_to_wxo_streaming()メソッドを呼び出す
            for chunk in wxo_adapter.route_to_wxo_streaming(
                prompt,
                st.session_state.thread_id
            ):
                if 'thread_id' in chunk and not returned_thread_id:
                    returned_thread_id = chunk['thread_id']
                
                if chunk.get('content'):
                    accumulated_response.append(chunk['content'])
                    current_text = ''.join(accumulated_response)
                    message_placeholder.markdown(current_text + " ⏳")
                
                if chunk.get('done'):
                    full_response = ''.join(accumulated_response)
                    message_placeholder.markdown(full_response)
                    break
            
            # 会話の継続性のためにthread_idを更新
            if returned_thread_id:
                st.session_state.thread_id = returned_thread_id
            
            full_response = ''.join(accumulated_response)
            
        except Exception as error:
            print(f"Error: {error}")
            import traceback
            traceback.print_exc()
            full_response = "申し訳ございません。エラーが発生しました。もう一度お試しください。"
            message_placeholder.markdown(full_response)
    
    # アシスタントの応答を保存
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# サイドバー
with st.sidebar:
    st.header("⚙️ オプション")
    
    # チャット履歴をクリア
    if st.button("🗑️ チャット履歴をクリア", use_container_width=True):
        st.session_state.messages = []
        st.session_state.thread_id = None
        st.rerun()
    
    st.divider()
    
    # 統計情報
    st.subheader("📈 統計")
    st.write(f"**総取引件数:** {len(df)}")
    st.write(f"**総支出:** ${df['amount'].sum():,.2f}")
    st.write(f"**最高額取引:** ${df['amount'].max():,.2f}")
    st.write(f"**最低額取引:** ${df['amount'].min():,.2f}")
    
    st.divider()
    
    # カテゴリ別サマリー
    st.subheader("📊 カテゴリ別")
    for category in df['category'].unique():
        category_total = df[df['category'] == category]['amount'].sum()
        category_jp = category_names.get(category, category)
        st.write(f"**{category_jp}:** ${category_total:,.2f}")
    
    st.divider()
    
    # アプリについて
    st.subheader("ℹ️ について")
    st.info(
        "このアプリケーションは、クレジットカード取引を管理し、"
        "AIアシスタントを使用して取引に関する質問に答えるプロトタイプです。"
    )
    
    st.caption("Powered by Streamlit & WxO Agent")

# Made with Bob
