from typing import List, Dict, Optional

notifications = []
notif_id = 1

def create_notification(btc_price: float, trade_vol: float, high: float, mcap: float) -> Dict:
    global notif_id, notifications

    notification = {
        "id": notif_id,
        "btc_price": btc_price,
        "high_price": high,
        "market_cap": mcap,
        "volume": trade_vol,
        "status": "outstanding",
    }

    notifications.append(notification)
    notif_id += 1
    return notification

def get_notifications(status: Optional[str] = None) -> List[Dict]:
    if status:
        return [notif for notif in notifications if notif["status"] == status]
    return notifications

def delete_notification(notification_id: int) -> Dict:
    global notifications
    for notif in notifications:
        if notif["id"] == notification_id:
            notifications.remove(notif)
            return notif
    return None

def update_notification_status(notification_id: int, status: str) -> Optional[Dict]:
    for notif in notifications:
        if notif["id"] == notification_id:
            notif["status"] = status
            return notif
    return None
