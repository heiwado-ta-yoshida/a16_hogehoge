import  logging

# ロガー設定
google.cloud.logging.Client().setup_logging()

@router.get("/")
def output_log():

    logging.info(f"[log]:start")

    try:
        logging.info(f"[log]:hogehoge")
        raise Error

    except Error:
        logging.error(f"[log]:error!!")


