# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import logging
import argparse
import os
from collections import namedtuple

# Logger config
logging.basicConfig(filename="directory_info.log", filemode="w", encoding="UTF-8", level=20)
# Create logger
logger = logging.getLogger(__name__)


def dir_observer(directory: str):
    if not os.listdir(directory) or not directory:
        logger.error("Directory is empty or not exist.")

    else:
        data = namedtuple("Data", ["name", "extension", "is_directory", "parent_dir"])

        for dir_path, _, file_name in os.walk(directory):
            dir_info = data(
                os.path.basename(dir_path), None, True, os.path.dirname(dir_path)
            )
            logger.info(dir_info)

            for file in file_name:
                file_info = data(
                    file.split(".")[0],
                    file.split(".")[1],
                    False,
                    os.path.dirname(dir_path),
                )
                logger.info(file_info)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Dir_info",
        description="Folder information",
        epilog="This program make a log file with some information about directory you choose",
    )
    parser.add_argument(
        "directory",
        metavar="path",
        type=str,
        nargs="?",
        help="Input directory path",
    )
    path = parser.parse_args()
    dir_observer(path.directory)
