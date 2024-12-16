import redis

def subscribe_with_filtering():
    # Connect to Redis
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Create a pubsub instance
    pubsub = client.pubsub()

    # Allow user to subscribe to multiple channels
    channels = input("Enter channels to subscribe to (comma-separated): ").split(",")
    channels = [channel.strip() for channel in channels]
    pubsub.subscribe(*channels)

    # Allow user to set filter keywords
    filters = input("Enter keywords to filter notifications (comma-separated): ").split(",")
    filters = [filter.strip().lower() for filter in filters]
    print(f"Subscribed to: {', '.join(channels)}")
    print(f"Filters applied: {', '.join(filters)}")

    # Listen for new messages with filtering
    print("\nListening for filtered notifications...")
    for message in pubsub.listen():
        if message["type"] == "message":
            notification = message["data"].lower()
            if any(keyword in notification for keyword in filters):
                print(f"New filtered notification on '{message['channel']}': {message['data']}")
            else:
                print(f"Ignored notification on '{message['channel']}': {message['data']}")

if __name__ == "__main__":
    subscribe_with_filtering()
