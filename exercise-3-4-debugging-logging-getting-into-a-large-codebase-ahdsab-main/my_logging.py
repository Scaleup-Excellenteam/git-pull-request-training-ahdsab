import logging

def logging_constructor():
    logging.basicConfig(level=logging.DEBUG, filename="chess_log.log", filemode="w", format="%(levelname)s:-> %(message)s")

logging_constructor()