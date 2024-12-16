# Real-Time Notification System

## Overview
This project implements a **Real-Time Notification System** using Redis and Python. The system enables users to publish and subscribe to messages with support for:
- **Real-time delivery** using Redis Pub/Sub.
- **Prioritization** of messages (High, Medium, Low).
- **Filtering** messages based on keywords or priorities.
- **Notification history** stored in Redis.
- **Automatic expiration** of old messages using Redis TTL.

## Features

### Core Functionality
1. **Send Notifications**
   - Notifications can be sent to specific channels with a specified priority (High, Medium, Low).
   - Each notification is stored in Redis with automatic expiration after 24 hours.

2. **Real-Time Delivery**
   - Notifications are delivered in real-time to subscribers using Redis Pub/Sub.

3. **Notification History**
   - Stores the last 100 notifications for each channel and priority.
   - Notifications older than 24 hours are automatically deleted using TTL.

4. **Filtering**
   - Subscribers can filter messages based on keywords and priorities.

5. **Prioritization**
   - Notifications are categorized into three levels: High, Medium, and Low.
   - Subscribers can choose to receive messages of specific priorities.

## System Requirements
1. **Redis**: Ensure Redis is installed and running locally or via Docker.
   ```bash
   docker run -d -p 6379:6379 --name myredis redis
   ```
2. **Python 3.8+**
   Install the necessary Python packages:
   ```bash
   pip install redis
   ```

## Usage

### Publisher
The publisher sends notifications to a specific channel with a priority. Notifications are stored in Redis with a TTL of 24 hours.

Run the publisher:
```bash
python publisher.py
```
Example interaction:
```plaintext
Welcome to the Redis Publisher!
Enter the channel name to publish to: notifications
Publishing to channel: notifications (type 'exit' to quit)
Enter message: Server is down!
Enter priority (high/medium/low): high
Message sent to 'notifications' with high priority!
```

### Subscriber
The subscriber listens for messages on a specific channel and filters them based on keywords and priorities.

Run the subscriber:
```bash
python subscriber.py
```
Example interaction:
```plaintext
Enter the channel name to subscribe to: notifications
Set up your filters:
Enter keywords to filter (comma-separated, or leave blank for none): server,query
Enter priorities to filter (e.g., high,medium,low): high,medium
Subscribed to channel: notifications
Filters applied: Keywords = ['server', 'query'], Priorities = ['high', 'medium']
Listening for messages... (Ctrl+C to exit)
New message on notifications: [HIGH] Server is down!
New message on notifications: [MEDIUM] Database query slow
```

## Technical Details

### Redis Data Structures
1. **Pub/Sub**: Used for real-time notification delivery.
2. **Lists**: Stores the last 100 notifications for each channel and priority.
3. **TTL**: Ensures notifications older than 24 hours are deleted automatically.

## Future Enhancements
1. **User Authentication**: Secure access to notifications.
2. **Notification Groups**: Support grouped notifications for related channels.
3. **Analytics Dashboard**: Add real-time analytics to monitor notifications by type and priority.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
