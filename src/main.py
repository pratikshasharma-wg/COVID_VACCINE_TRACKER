import logging

from config.logs.logs import Logs
from views.auth import AuthViews
from utils.decorators import load_config
from database.database_operations import db


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'src\\config\\logs\\logs.txt')


logger = logging.getLogger('main')


@load_config
def main():
    logger.info(Logs.WELCOME)
    db.create_tables()
    AuthViews().start()


if __name__ == "__main__":
    
    try:
        main()
    except Exception as e:
        logger.error('Error Occured in application: {}'.format(e))
    finally:
        #close database connection
        db.connection.close()
        print("Exiting from Application")
        logger.info("Connection closed. Exiting from application")
