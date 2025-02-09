import logging
from prometheus_client import start_http_server, Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a Prometheus counter to track the number of successfully processed events
EVENTS_PROCESSED = Counter('events_processed', 'Total number of events processed successfully')

# Start Prometheus HTTP server on port 8000 for metrics scraping
start_http_server(8000)

def log_event(event_id):
    """
    Logs event processing and increments the Prometheus counter.
    :param event_id: The ID of the event being processed.
    """
    EVENTS_PROCESSED.inc()
    logging.info(f"Event {event_id} processed successfully")

# Example usage (This would typically be inside the main event processing loop)
if __name__ == '__main__':
    sample_event_id = 123
    log_event(sample_event_id)

