# Create a notification. Line items may include current price of BTC, market trade volume, intra day high price, market cap 
# Send a notification to an email
# List sent notifications (sent, outstanding, failed etc.)
# Delete a notification

from fastapi import FastAPI, HTTPException
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI()

notifications = []
notif_id = 1

class Notification(BaseModel):
    email: str
    btc_price: float
    trade_vol: float
    high: float
    mcap: float

class SendNotificationRequest(BaseModel):
    id: int
    email: str

@app.post("/notifications/")
def create_notif(notification: Notification):
    global notif_id

    notification = {
        "id": notif_id,
        "email": notification.email,
        "btc_price": notification.btc_price,
        "high_price": notification.high,
        "market_cap": notification.mcap,
        "volume": notification.trade_vol,
        "status": "outstanding",
    }

    notifications.append(notification)
    notif_id += 1
    return notification


@app.get("/notifications/")
def get_notif(status: str = None)-> List[Dict]:
    if status:
        filtered_notifs = [x for x in notifications if x["status"] == status]
        return filtered_notifs
    return notifications

@app.delete("/notifications/{notif_id}")
def delete_notif(notif_id: int):
    # print("DSafhssdhsrthdsf")
    global notifications
    # print("dshdgj", notifications)
    for notif in notifications:
        if notif["id"] == notif_id:
            notifications.remove(notif)
            return notif
    raise HTTPException(status_code=404, detail="NOtification not found")


@app.post("/notifications/send/")
def send_notif(request: SendNotificationRequest):
    global notifications
    for notif in notifications:
        if notif["id"] == request.id:
            if notif["email"] == request.email:
                notif["status"] = "sent"
                return {"message": f"Notification {request.id} sent to {request.email}"}
            else:
                raise HTTPException(status_code=400, detail="email do not matlhc")
    raise HTTPException(status_code=404, detail="Notification not found")






    
