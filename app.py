from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional
from pydantic import BaseModel
import store

app = FastAPI()

class Notification(BaseModel):
    btc_price: float
    trade_vol: float
    high: float
    mcap: float

class SendNotificationRequest(BaseModel):
    id: int
    email: str

@app.post("/notifications/")
def create_notif(notification: Notification):
    created_notification = create_notification(
        btc_price=notification.btc_price,
        trade_vol=notification.trade_vol,
        high=notification.high,
        mcap=notification.mcap,
    )
    return created_notification

@app.get("/notifications/")
def get_notif(status: Optional[str] = None) -> List[Dict]:
    return get_notifications(status)

@app.delete("/notifications/{notif_id}")
def delete_notif(notif_id: int):
    deleted_notification = delete_notification(notif_id)
    if not deleted_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return deleted_notification

@app.post("/notifications/send/")
def send_notif(request: SendNotificationRequest):
    updated_notification = update_notification_status(request.id, "sent")
    if not updated_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"message": f"Notification {request.id} sent to {request.email}"}
