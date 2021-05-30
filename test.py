import logging

log = logging.getLogger("application")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
log.info("Starting application")
