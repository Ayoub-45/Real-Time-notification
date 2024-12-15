import redis
import time 
def publisher():
    #connect to Redis
    client=redis.StrictRedis(host="localhost",port=6379,decode_responses=True)
    print("Sending notifications...")
    while True:
        #Create notification
        notification =input("Enter notification message (type 'exit' to quit)")
        if notification.lower() == "exit":
            break
        client.publish("notifications", notification)
        print("notification sent!")

if __name__=="__main__":
    publisher()