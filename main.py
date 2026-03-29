from fastapi import FastAPI

app = FastAPI()


@app.post("/contacts")
def get_contacts():
    return [
        {
            "OFFER_RMA_NUMBER": "RKSU95050000519999",
            "OFFER_DATE": "20260329",
            "CUSTOMER_IDENTIFICATION": "2023022009999",
            "CUSTOMER_LASTNAME": "Sueyasu",
            "CUSTOMER_FIRSTNAME": "API Test",
            "OFFER_MODEL": "iPhone SE 3 256GB Midnight - Rakuten",
            "OFFER_SERIAL_NUMBER": "350158429809999",
            "MOBILE_NUMBER": "+819018919939",
            "ORIGINAL_START_DATE": "2026/3/8",
            "RECEIPT_DEVICE_STATUS": "NR01",
            "TRACKING_NUMBER": "",
            "RETURN_DEADLINE": "2026/3/28"
        },
        {
            "OFFER_RMA_NUMBER": "RKSU95050000518888",
            "OFFER_DATE": "20260308",
            "CUSTOMER_IDENTIFICATION": "2023022008888",
            "CUSTOMER_LASTNAME": "API Test",
            "CUSTOMER_FIRSTNAME": "Kohei",
            "OFFER_MODEL": "iPhone 13 Pro 256GB Midnight",
            "OFFER_SERIAL_NUMBER": "350158429808888",
            "MOBILE_NUMBER": "+819011111111",
            "ORIGINAL_START_DATE": "2026/3/8",
            "RECEIPT_DEVICE_STATUS": "NR03",
            "TRACKING_NUMBER": "",
            "RETURN_DEADLINE": "2026/3/28"
        }
    ]
