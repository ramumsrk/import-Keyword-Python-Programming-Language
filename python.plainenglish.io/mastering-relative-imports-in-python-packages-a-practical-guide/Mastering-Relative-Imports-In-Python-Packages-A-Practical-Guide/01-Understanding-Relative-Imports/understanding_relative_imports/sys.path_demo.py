#! /usr/bin/python3.12

import sys

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent.parent}/logs/sys.path_demo.log'
)

if __name__ == '__main__':

  for path in sys.path:
    logging.debug(
      f'{path=}'
    )