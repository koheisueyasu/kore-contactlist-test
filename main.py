from fastapi import FastAPI

app = FastAPI()


@app.post("/contacts")
def get_contacts():
    return {
        "status": "success",
        "data": {
            "results": [
                {
                    "OFFER_RMA_NUMBER": "RKSU95050000519999",
                    "OFFER_DATE": "20260329",
                    "CUSTOMER_IDENTIFICATION": "2023022009999",
                    "CUSTOMER_LASTNAME": "末安",
                    "CUSTOMER_FIRSTNAME": "APIテスト",
                    "OFFER_MODEL": "iPhone SE 3 256GB Midnight - Rakuten",
                    "OFFER_SERIAL_NUMBER": "350158429809999",
                    "MOBILE_NUMBER": "+819018919939",
                    "ORIGINAL_START_DATE": "2026/3/8",
                    "RECEIPT_DEVICE_STATUS": "NR01",
                    "TRACKING_NUMBER": "",
                    "RETURN_DEADLINE": "2026/3/28",
                },
                {
                    "OFFER_RMA_NUMBER": "RKSU95050000518888",
                    "OFFER_DATE": "20260308",
                    "CUSTOMER_IDENTIFICATION": "2023022008888",
                    "CUSTOMER_LASTNAME": "APIテスト",
                    "CUSTOMER_FIRSTNAME": "興平",
                    "OFFER_MODEL": "iPhone 13 Pro 256GB Midnight",
                    "OFFER_SERIAL_NUMBER": "350158429808888",
                    "MOBILE_NUMBER": "+819011111111",
                    "ORIGINAL_START_DATE": "2026/3/8",
                    "RECEIPT_DEVICE_STATUS": "NR03",
                    "TRACKING_NUMBER": "",
                    "RETURN_DEADLINE": "2026/3/28",
                },
            ]
        },
    }
