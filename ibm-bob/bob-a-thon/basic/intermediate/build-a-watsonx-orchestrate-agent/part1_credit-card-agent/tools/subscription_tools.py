"""
サブスクリプション管理ツール
クレジットカードのサブスクリプション取引の管理機能を提供
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta
from typing import Optional
import json


@tool()
def get_subscriptions() -> str:
    """サブスクリプションであるすべての取引をリストします。
    
    詳細(名前、金額、頻度、次回請求日)を含む5〜7件のサブスクリプションを返します。
    
    Returns:
        str: サブスクリプションのJSON形式のリスト
    """
    # ハードコードされたサンプルサブスクリプションデータ
    subscriptions = [
        {
            "subscription_id": "SUB-001",
            "name": "Netflix Premium",
            "category": "streaming",
            "amount": 15.99,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2023-01-15",
            "next_billing_date": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "Netflix Inc."
        },
        {
            "subscription_id": "SUB-002",
            "name": "Spotify Family",
            "category": "streaming",
            "amount": 16.99,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2023-03-20",
            "next_billing_date": (datetime.now() + timedelta(days=12)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "Spotify AB"
        },
        {
            "subscription_id": "SUB-003",
            "name": "Adobe Creative Cloud",
            "category": "software",
            "amount": 54.99,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2022-11-01",
            "next_billing_date": (datetime.now() + timedelta(days=18)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "Adobe Systems"
        },
        {
            "subscription_id": "SUB-004",
            "name": "Planet Fitness Membership",
            "category": "fitness",
            "amount": 22.99,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2023-02-10",
            "next_billing_date": (datetime.now() + timedelta(days=8)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "Planet Fitness"
        },
        {
            "subscription_id": "SUB-005",
            "name": "Amazon Prime",
            "category": "shopping",
            "amount": 14.99,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2022-06-15",
            "next_billing_date": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "Amazon.com"
        },
        {
            "subscription_id": "SUB-006",
            "name": "The New York Times Digital",
            "category": "news",
            "amount": 17.00,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2023-04-01",
            "next_billing_date": (datetime.now() + timedelta(days=25)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "The New York Times"
        },
        {
            "subscription_id": "SUB-007",
            "name": "Microsoft 365 Family",
            "category": "software",
            "amount": 9.99,
            "currency": "USD",
            "frequency": "monthly",
            "start_date": "2022-09-12",
            "next_billing_date": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
            "status": "active",
            "merchant": "Microsoft Corporation"
        }
    ]
    
    # 合計月額費用を計算
    total_monthly = sum(sub["amount"] for sub in subscriptions)
    
    result = {
        "status": "success",
        "message": f"{len(subscriptions)}件のアクティブなサブスクリプションが見つかりました",
        "count": len(subscriptions),
        "total_monthly_cost": round(total_monthly, 2),
        "currency": "USD",
        "subscriptions": subscriptions
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@tool()
def get_subscription_spend(category: Optional[str] = None) -> str:
    """さまざまなサブスクリプションカテゴリに費やした金額を計算します。
    
    Args:
        category (str, optional): フィルタリングするカテゴリ
            (例: "streaming", "software", "fitness", "shopping", "news")
    
    Returns:
        str: カテゴリ別の支出情報を含むJSON形式の応答
    """
    # ハードコードされたカテゴリ別支出データ
    category_spending = {
        "streaming": {
            "category": "streaming",
            "monthly_total": 32.98,
            "annual_total": 395.76,
            "subscriptions": [
                {"name": "Netflix Premium", "amount": 15.99},
                {"name": "Spotify Family", "amount": 16.99}
            ]
        },
        "software": {
            "category": "software",
            "monthly_total": 64.98,
            "annual_total": 779.76,
            "subscriptions": [
                {"name": "Adobe Creative Cloud", "amount": 54.99},
                {"name": "Microsoft 365 Family", "amount": 9.99}
            ]
        },
        "fitness": {
            "category": "fitness",
            "monthly_total": 22.99,
            "annual_total": 275.88,
            "subscriptions": [
                {"name": "Planet Fitness Membership", "amount": 22.99}
            ]
        },
        "shopping": {
            "category": "shopping",
            "monthly_total": 14.99,
            "annual_total": 179.88,
            "subscriptions": [
                {"name": "Amazon Prime", "amount": 14.99}
            ]
        },
        "news": {
            "category": "news",
            "monthly_total": 17.00,
            "annual_total": 204.00,
            "subscriptions": [
                {"name": "The New York Times Digital", "amount": 17.00}
            ]
        }
    }
    
    if category:
        # 特定のカテゴリでフィルタリング
        category_lower = category.lower()
        if category_lower in category_spending:
            result = {
                "status": "success",
                "message": f"カテゴリ '{category}' の支出情報",
                "filter": category,
                "data": category_spending[category_lower]
            }
        else:
            result = {
                "status": "error",
                "message": f"カテゴリ '{category}' が見つかりません",
                "available_categories": list(category_spending.keys())
            }
    else:
        # すべてのカテゴリの概要
        total_monthly = sum(cat["monthly_total"] for cat in category_spending.values())
        total_annual = sum(cat["annual_total"] for cat in category_spending.values())
        
        result = {
            "status": "success",
            "message": "すべてのカテゴリの支出概要",
            "summary": {
                "total_monthly": round(total_monthly, 2),
                "total_annual": round(total_annual, 2),
                "currency": "USD",
                "category_count": len(category_spending)
            },
            "categories": category_spending
        }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@tool()
def cancel_subscription(subscription_name: str) -> str:
    """サブスクリプションをキャンセルします。
    
    Args:
        subscription_name (str): キャンセルするサブスクリプションの名前
    
    Returns:
        str: サブスクリプションキャンセルの確認を含むJSON形式の応答
    """
    # ハードコードされた応答
    cancellation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_billing_date = (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")
    
    # サンプルサブスクリプション情報（実際のシステムではデータベースから取得）
    subscription_info = {
        "subscription_name": subscription_name,
        "status": "cancelled",
        "cancellation_date": cancellation_date,
        "last_billing_date": last_billing_date,
        "refund_eligible": False,
        "access_until": last_billing_date
    }
    
    result = {
        "status": "success",
        "message": f"サブスクリプション '{subscription_name}' が正常にキャンセルされました",
        "subscription": subscription_info,
        "details": {
            "immediate_cancellation": False,
            "access_continues": True,
            "access_until": last_billing_date,
            "no_future_charges": True
        },
        "notes": [
            f"現在の請求期間の終了({last_billing_date})までサービスにアクセスできます",
            "今後の請求は発生しません",
            "いつでも再登録できます"
        ]
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)

# Made with Bob
