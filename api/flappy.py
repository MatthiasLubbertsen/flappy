import random
import logging
import os

# Standaard logging naar stdout (Vercel pakt dit op in de function logs)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

def main(request):
    logger.info("api/flappy.py invoked")
    # Optioneel: log environment info om te helpen debuggen
    logger.info("VERCEL: %s", os.environ.get("VERCEL", "unknown"))
    # Simuleer up/down
    up = random.choice([True, False])
    if up:
        status = 200
        body = "Site is UP"
    else:
        status = 500
        body = "Site is DOWN"

    logger.info("Responding with status=%d body=%s", status, body)

    # Vercel verwacht doorgaans een dict met statusCode, headers en body
    return {
        "statusCode": status,
        "headers": {"Content-Type": "text/plain"},
        "body": body
    }

# Vercel zoekt naar 'handler' of 'app' — exporteer beide naar onze main functie
handler = main
app = main
