"""Set up logging."""
import logging

from . import env

logging.basicConfig(
    level=logging.DEBUG if env.get("debug") else logging.INFO,
    format='%(asctime)s: [%(levelname)s] %(message)s',
    datefmt='%m-%d-%Y|%H-%M-%S'
)
logger = logging.getLogger("__name__")
