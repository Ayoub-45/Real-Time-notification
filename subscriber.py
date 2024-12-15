import redis

def subscribe_and_retrieve_history():
    # Connect to Redis
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Create a pubsub instance
    pubsub = client.pubsub()

    # Allow user to subscribe to multiple channels
    channels = input("Enter channels to subscribe to (comma-separated): ").split(",")
    channels = [channel.strip() for channel in channels]
    pubsub.subscribe(*channels)

    print(f"Subscribed to: {', '.join(channels)}")

    # Retrieve notification history for each channel
    for channel in channels:
        print(f"\nNotification history for '{channel}':")
        history = client.lrange(f"history:{channel}", 0, -1)
        for notification in history:
            print(f"- {notification}")

    # Listen for new messages
    print("\nListening for notifications...")
    for message in pubsub.listen():
        if message["type"] == "message":
            print(f"New notification on '{message['channel']}': {message['data']}")

if __name__ == "__main__":
    subscribe_and_retrieve_history()
