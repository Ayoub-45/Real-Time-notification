import redis

def prioritized_publisher():
    # Connect to Redis
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    print("Publishing prioritized notifications...")
    while True:
        # Input the channel and message
        channel = input("Enter channel name (or 'exit' to quit): ")
        if channel.lower() == "exit":
            break

        # Input message and priority
        message = input(f"Enter message for channel '{channel}': ")
        priority = input("Enter priority (high/medium/low): ").lower()

        if priority not in ["high", "medium", "low"]:
            print("Invalid priority! Please enter high, medium, or low.")
            continue

        # Publish the message to the channel
        client.publish(channel, f"[{priority.upper()}] {message}")

        # Save the notification in the appropriate priority list
        key = f"history:{channel}:{priority}"
        client.lpush(key, message)
        client.ltrim(key, 0, 99)  # Keep only the last 100 messages
        client.expire(key, 86400)  # 24-hour expiration

        print(f"Notification sent to '{channel}' with {priority} priority!")

if __name__ == "__main__":
    prioritized_publisher()
