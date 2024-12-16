import redis

def subscriber():
    # Connect to Redis
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # Subscribe to a channel
    channel = input("Enter the channel name to subscribe to: ")
    pubsub = client.pubsub()
    pubsub.subscribe(channel)

    # Set up filtering options
    print("Set up your filters:")
    keywords = input("Enter keywords to filter (comma-separated, or leave blank for none): ")
    priorities = input("Enter priorities to filter (e.g., high,medium,low): ").lower().split(",")

    # Parse keywords and priorities
    keyword_list = [kw.strip().lower() for kw in keywords.split(",") if kw.strip()]
    priority_list = [pr.strip() for pr in priorities if pr.strip() in ["high", "medium", "low"]]

    print(f"Subscribed to channel: {channel}")
    print(f"Filters applied: Keywords = {keyword_list}, Priorities = {priority_list}")
    print("Listening for messages... (Ctrl+C to exit)")

    # Listen for messages
    try:
        for message in pubsub.listen():
            if message["type"] == "message":
                data = message["data"]

                # Filter by priority
                message_priority = data.split("]")[0].strip("[").lower()
                if priority_list and message_priority not in priority_list:
                    continue

                # Filter by keywords
                if keyword_list and not any(kw in data.lower() for kw in keyword_list):
                    continue

                print(f"New message on {channel}: {data}")
    except KeyboardInterrupt:
        print("\nExited.")
        pubsub.close()

if __name__ == "__main__":
    subscriber()
