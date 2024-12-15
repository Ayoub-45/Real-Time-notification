import redis
def subscriber():
    # Connect to Redis
    client=redis.StrictRedis(host="localhost",port=6379,decode_responses=True)
    #subscribe to channel 
    pubsub=client.pubsub()
    pubsub.subscribe("notifications")
    print("Listening for notifications...")
    #Listen for messages
    for message in pubsub.listen():
        if message["type"] =="message":
            print(f"New notification:{message['data']}")
            

if __name__=="__main__":
    subscriber()