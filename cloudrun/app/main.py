import logging

# ロガー設定
# google.cloud.logging.Client().setup_logging()

@app.get(f"/")
def output_log():

    logging.info(f"[log]:start")

    try:
        logging.info(f"[log]:hogehoge")
        raise ExceptionError

    except ExceptionError:
        logging.error(f"[log]:error!!")

    return "done"