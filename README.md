# Real-Time Notification System

## Overview

This project implements a **Real-Time Notification System** using Redis, Python, and Flask. The system enables users to send, receive, and manage notifications with support for:

- **Real-time delivery** using Redis Pub/Sub.
- **Prioritization** with High, Medium, and Low priority levels.
- **Notification history** for each channel and priority.
- **Automatic expiration** of old notifications.
- A **web interface** for managing and retrieving notifications.

## Features

### Core Functionality

1. **Send Notifications**

   - Notifications can be sent to specific channels with a specified priority (High, Medium, Low).
   - Each notification is stored in Redis for history.

2. **Real-Time Delivery**

   - Notifications are delivered in real-time to subscribers using Redis Pub/Sub and WebSockets.

3. **Notification History**

   - Stores the last 100 notifications for each channel and priority.
   - Notifications older than 24 hours are automatically deleted using TTL.

4. **Prioritization**

   - Notifications are categorized into three levels: High, Medium, and Low.
   - Users can retrieve notifications filtered by priority.

5. **Web Interface**
   - Provides HTTP APIs for sending and retrieving notifications.
   - Supports WebSocket-based real-time updates.

## System Requirements

1. **Redis**: Ensure Redis is installed and running locally or via Docker.

   ```bash
   docker run -d -p 6379:6379 --name myredis redis
   ```

2. **Python 3.8+**
   Install the necessary Python packages:
   ```bash
   pip install flask flask-socketio redis
   ```

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Start the Flask application:

   ```bash
   python app.py
   ```

3. Ensure Redis is running locally or via Docker.

## Usage

### HTTP API

#### 1. **Send Notification**

- **Endpoint**: `POST /send`
- **Request Body**:
  ```json
  {
    "channel": "channel1",
    "message": "Server is down!",
    "priority": "high"
  }
  ```
- **Description**: Sends a notification to the specified channel with the given priority.

#### 2. **Retrieve Notification History**

- **Endpoint**: `GET /history/<channel>/<priority>`
- **Example**:
  ```bash
  GET /history/channel1/high
  ```
- **Description**: Retrieves the last 100 notifications for the specified channel and priority.

### Real-Time Subscription

1. Connect to WebSocket:

   - **URL**: `ws://127.0.0.1:5000`

2. Subscribe to a channel:
   - Send a JSON payload:
     ```json
     {
       "channel": "channel1"
     }
     ```
3. Receive notifications in real-time as they are published.

## Technical Details

### Redis Data Structures

1. **Pub/Sub**: Used for real-time notification delivery.
2. **Lists**: Stores the last 100 notifications for each channel and priority.
3. **TTL**: Ensures notifications older than 24 hours are deleted automatically.

### Flask Routes

1. `POST /send`: Sends a notification.
2. `GET /history/<channel>/<priority>`: Retrieves notification history.
3. WebSocket endpoint for real-time subscription.

## Future Enhancements

1. **User Authentication**: Secure access to notifications.
2. **Notification Groups**: Support grouped notifications for related channels.
3. **UI/UX Improvements**: Create a user-friendly web interface for managing notifications.
4. **Analytics Dashboard**: Add real-time analytics to monitor notifications by type and priority.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
