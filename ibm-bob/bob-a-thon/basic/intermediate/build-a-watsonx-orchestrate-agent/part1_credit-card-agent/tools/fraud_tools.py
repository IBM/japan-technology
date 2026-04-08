"""
不正検知ツール
クレジットカードの不正取引検知、カード凍結、キャンセル、新規カード発行機能を提供
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta
import json


@tool()
def check_transactions() -> str:
    """異常な取引をリストします。
    
    不正の可能性がある取引を最大3件返します。
    各取引には、取引ID、日時、金額、店舗名、場所、疑わしい理由が含まれます。
    
    Returns:
        str: 異常な取引のJSON形式のリスト
    """
    # ハードコードされたサンプル不正取引データ
    suspicious_transactions = [
        {
            "transaction_id": "TXN-2024-001",
            "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "amount": 1250.00,
            "currency": "USD",
            "merchant": "Electronics World Online",
            "location": "Moscow, Russia",
            "category": "retail",
            "reason": "通常と異なる地域からの高額購入"
        },
        {
            "transaction_id": "TXN-2024-002",
            "date": (datetime.now() - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
            "amount": 899.99,
            "currency": "USD",
            "merchant": "Luxury Fashion Store",
            "location": "Paris, France",
            "category": "retail",
            "reason": "短時間に複数の高額取引"
        },
        {
            "transaction_id": "TXN-2024-003",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": 2500.00,
            "currency": "USD",
            "merchant": "International Wire Transfer",
            "location": "Lagos, Nigeria",
            "category": "transfer",
            "reason": "通常と異なるタイプの取引"
        }
    ]
    
    result = {
        "status": "success",
        "message": "3件の疑わしい取引が見つかりました",
        "count": len(suspicious_transactions),
        "transactions": suspicious_transactions
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@tool()
def report_fraud(transaction_id: str) -> str:
    """不正ケースを開き、新しいクレジットカードの送付を推奨します。
    
    Args:
        transaction_id (str): 報告する取引のID
    
    Returns:
        str: 不正報告の確認とケース番号を含むJSON形式の応答
    """
    # ハードコードされた応答
    case_number = f"FRAUD-{datetime.now().strftime('%Y%m%d')}-{transaction_id[-3:]}"
    
    result = {
        "status": "success",
        "message": "不正ケースが正常に開かれました",
        "case_number": case_number,
        "transaction_id": transaction_id,
        "reported_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "next_steps": [
            "取引は調査のためにブロックされました",
            "新しいクレジットカードの発行を推奨します",
            "調査結果は3-5営業日以内にメールで通知されます"
        ],
        "recommendation": "新しいクレジットカードを発行してください"
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@tool()
def freeze_credit_card(card_number: str) -> str:
    """クレジットカードを凍結します。
    
    Args:
        card_number (str): カード番号の下4桁
    
    Returns:
        str: カード凍結の確認を含むJSON形式の応答
    """
    # ハードコードされた応答
    result = {
        "status": "success",
        "message": f"カード番号 ****{card_number} が正常に凍結されました",
        "card_last_four": card_number,
        "frozen_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": {
            "all_transactions_blocked": True,
            "can_unfreeze": True,
            "unfreeze_method": "モバイルアプリまたはカスタマーサービスに連絡"
        },
        "note": "カードは凍結されましたが、キャンセルされていません。いつでも凍結解除できます。"
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@tool()
def cancel_credit_card(card_number: str, reason: str) -> str:
    """クレジットカードをキャンセルします。
    
    Args:
        card_number (str): カード番号の下4桁
        reason (str): キャンセルの理由
    
    Returns:
        str: カードキャンセルの確認を含むJSON形式の応答
    """
    # ハードコードされた応答
    result = {
        "status": "success",
        "message": f"カード番号 ****{card_number} が正常にキャンセルされました",
        "card_last_four": card_number,
        "cancelled_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "reason": reason,
        "details": {
            "card_destroyed": True,
            "all_transactions_blocked": True,
            "can_reactivate": False
        },
        "next_steps": [
            "このカードは完全に無効化されました",
            "新しいカードが必要な場合は、send_new_credit_cardツールを使用してください",
            "最終明細書は次の請求サイクルで送付されます"
        ]
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@tool()
def send_new_credit_card(address: str) -> str:
    """新しいクレジットカードを送付します。
    
    Args:
        address (str): 配送先住所
    
    Returns:
        str: 新しいカード送付の確認を含むJSON形式の応答
    """
    # ハードコードされた応答
    tracking_number = f"TRACK-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    expected_delivery = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    result = {
        "status": "success",
        "message": "新しいクレジットカードが正常に発送されました",
        "delivery_address": address,
        "order_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "expected_delivery": expected_delivery,
        "tracking_number": tracking_number,
        "card_details": {
            "card_type": "Visa Platinum",
            "last_four_digits": "新しいカード番号は配送時に確認できます",
            "activation_required": True
        },
        "instructions": [
            "カードを受け取ったら、同封の手順に従って有効化してください",
            "有効化には、カード裏面の電話番号に電話するか、モバイルアプリを使用してください",
            "古いカードは安全に破棄してください"
        ]
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)

# Made with Bob
