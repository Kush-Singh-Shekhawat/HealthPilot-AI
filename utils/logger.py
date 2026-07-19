from pathlib import Path
from loguru import logger

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "healthpilot.log",
    rotation="5 MB",
    retention="10 days",
    level="INFO",
    enqueue=True,
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
)

app_logger = logger