from fastapi import FastAPI
from datetime import date

app = FastAPI()


@app.post("/contacts")
def get_contacts():
    result = {
        "contact": {
            {
                "phoneNumber": "+819018919939",
                "firstName": "APIテスト",
                "lastName": "末安",
                "uniqueId": "RKSU95050000519999",
                "timeZone": "Asia/Tokyo",
                "contactPriority": "1",
                "OFFER_RMA_NUMBER": "RKSU95050000519999",
                "OFFER_DATE": "20260329",
                "CUSTOMER_IDENTIFICATION": "2023022009999",
                "OFFER_MODEL": "iPhone SE 3 256GB Midnight - Rakuten",
                "OFFER_SERIAL_NUMBER": "350158429809999",
                "ORIGINAL_START_DATE": "2026/3/8",
                "RECEIPT_DEVICE_STATUS": "NR01",
                "TRACKING_NUMBER": "",
                "RETURN_DEADLINE": "2026/3/28",
            },
            {
                "phoneNumber": "+819011111111",
                "firstName": "興平",
                "lastName": "APIテスト",
                "uniqueId": "RKSU95050000518888",
                "timeZone": "Asia/Tokyo",
                "contactPriority": "2",
                "OFFER_RMA_NUMBER": "RKSU95050000518888",
                "OFFER_DATE": "20260308",
                "CUSTOMER_IDENTIFICATION": "2023022008888",
                "OFFER_MODEL": "iPhone 13 Pro 256GB Midnight",
                "OFFER_SERIAL_NUMBER": "350158429808888",
                "ORIGINAL_START_DATE": "2026/3/8",
                "RECEIPT_DEVICE_STATUS": "NR03",
                "TRACKING_NUMBER": "",
                "RETURN_DEADLINE": "2026/3/28",
            },
        }
    }
    return result
