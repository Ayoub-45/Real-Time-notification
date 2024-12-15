import redis

def publisher():
    # Connect to Redis
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    print("Publishing notifications...")
    while True:
        # Input the channel and message
        channel = input("Enter channel name (or 'exit' to quit): ")
        if channel.lower() == "exit":
            break
        message = input(f"Enter message for channel '{channel}': ")

        # Publish the message to the channel
        client.publish(channel, message)

        # Save the notification in history (keep only last 100)
        client.lpush(f"history:{channel}", message)
        client.ltrim(f"history:{channel}", 0, 99)  # Limit to last 100 messages

        print(f"Notification sent to '{channel}'!")

if __name__ == "__main__":
    publisher()
