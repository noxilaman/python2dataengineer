import logging
def log(message):
    logging.basicConfig(
        filename='app.log',          # File where logs will be saved
        filemode='a',                # 'a' to append logs, 'w' to overwrite every run
        format='%(asctime)s\n\n[%(levelname)s]\n\n%(message)s\n\n', # Log line format
        datefmt='%Y-%m-%d %H:%M:%S', # Date/Time format
        level=logging.INFO           # Minimum log level to capture
    )
    logging.info(message)