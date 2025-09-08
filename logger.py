import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()          # Log ke terminal
    ]
)

logger = logging.getLogger(__name__)
