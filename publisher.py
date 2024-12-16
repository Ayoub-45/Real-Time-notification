import redis

def publisher():
    # Connect to Redis
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    print("Welcome to the Redis Publisher!")
    channel = input("Enter the channel name to publish to: ")

    print(f"Publishing to channel: {channel} (type 'exit' to quit)")
    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break

        priority = input("Enter priority (high/medium/low): ").lower()
        if priority not in ["high", "medium", "low"]:
            print("Invalid priority! Please enter 'high', 'medium', or 'low'.")
            continue

        # Format the message
        formatted_message = f"[{priority.upper()}] {message}"

        # Publish the message
        client.publish(channel, formatted_message)

        # Store the message in history with expiration
        history_key = f"history:{channel}:{priority}"
        client.lpush(history_key, formatted_message)
        client.ltrim(history_key, 0, 99)  # Keep the last 100 messages
        client.expire(history_key, 86400)  # Set TTL to 24 hours

        print(f"Message sent to '{channel}' with {priority} priority!")

if __name__ == "__main__":
    publisher()
