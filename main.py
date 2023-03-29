import time
import logging


def Job():
    # Настроить логгер
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Создать обработчик файлового журнала и настроить уровень журнала
    log_file = '/var/log/python_test.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Создать форматировщик и добавить его в обработчик
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавить обработчик к логгеру
    logger.addHandler(file_handler)

    logger.info("I started working")
    for i in range(5):
        time.sleep(2)
        logger.info("I'm working")
    logger.info("I'm done working")


if __name__ == '__main__':
    Job()
