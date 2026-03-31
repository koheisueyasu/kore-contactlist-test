from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime

app = FastAPI()


@app.post("/kore-webhook")
async def kore_webhook(request: Request):
    body = await request.json()

    # 受信ログ（RenderのLogsで見える）
    print("=== POST received from Kore ===")
    print(body)

    # デモ用レスポンス
    return JSONResponse(status_code=200, content={"result": "success", "received_at": datetime.datetime.utcnow().isoformat(), "received_body": body})


@app.get("/")
def health_check():
    return {"status": "ok"}
