from fastapi import FastAPI
import logging

# ロガー設定
# google.cloud.logging.Client().setup_logging()

app = FastAPI()

@app.get(f"/")
def home():
    logging.info(f"[log]:start")
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
