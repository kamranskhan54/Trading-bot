import logging
import logging.handlers
import os
from pathlib import Path

def setup_logging(log_dir: str = "logs", log_file: str = "trading_bot.log") -> None:
    """
    Configure logging with file and console handlers
    
    Args:
        log_dir: Directory for log files
        log_file: Name of log file
    """
    # Create logs directory if it doesn't exist
    Path(log_dir).mkdir(exist_ok=True)
    
    log_path = os.path.join(log_dir, log_file)
    
    # Create logger
    logger = logging.getLogger('trading_bot')
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return
    
    # File handler (rotating)
    file_handler = logging.handlers.RotatingFileHandler(
        log_path,
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.info("Logging configured")
