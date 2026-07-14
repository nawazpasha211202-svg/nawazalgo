from logging_setup import setup_logger

log = setup_logger()

# Example logs
log.info("User login attempt", extra={"user": "nawaz", "status": "failed"})
log.error("Database connection error")
log.debug("Debugging trade execution flow")
