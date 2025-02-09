from kafka import KafkaConsumer, KafkaProducer
import json

BROKER = 'localhost:9092'
INPUT_TOPIC = 'event_stream'
ERROR_TOPIC = 'error_events'
RECOVERED_TOPIC = 'recovered_events'

consumer = KafkaConsumer(
    ERROR_TOPIC, 
    bootstrap_servers=BROKER, 
    auto_offset_reset='earliest', 
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
producer = KafkaProducer(
    bootstrap_servers=BROKER, 
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def process_event(event):
    """Mock function to process an event."""
    try:
        event['status'] = 'processed'
        event['recalculated_value'] = event['original_value'] * 1.1  # Example recalculation
        return event
    except Exception as e:
        print(f"Error processing event {event['id']}: {e}")
        return None

def recover_and_reprocess():
    """Reads error events and reprocesses them."""
    for message in consumer:
        event = message.value
        print(f"Reprocessing event ID: {event['id']}")
        corrected_event = process_event(event)
        if corrected_event:
            producer.send(RECOVERED_TOPIC, corrected_event)
            print(f"Event ID {event['id']} successfully reprocessed.")

if __name__ == "__main__":
    recover_and_reprocess()