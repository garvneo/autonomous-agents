# Autonomous Agents

This project demonstrates the implementation of autonomous agents using Quart(official async implementation of Flask), 
a Python web framework, for the backend, and HTML, CSS, and JavaScript for the frontend. The agents are capable of 
communication and executing behaviors asynchronously.

## Design Choices
### Basic Implementation
1. To implement the basic functionality at first I went ahead with 'Asyncio' library of python as the requirement was to handle reactiveness and proactiveness of more than one instances of an autonomous agent and they had to done in an asynchronous way.
Below is how I started
- Made a folder: 'agents'.
- Created module 'agents\autonomous_agent.py' as a blueprint of 'Autonomous Agent' in order to cater to it's reactiveness and
proactiveness along with behaviour and asynchronous inbox and outbox message handling.  
- Created module 'agents\concrete_agent.py' which in somewhat manner follows the blueprint of 'Autonomous Agent' or say it 
inherits 'agents\autonomous_agent.py'.
- Used Queue data structure to hold the messages of InBoxes and OutBoxes.
- Then created a simple app.py with a 'main' functionality (or say it acted like a controller) where I created instances of concrete class linked their inboxes to outboxes and invoked their behaviours asynchronously and agents started 
communicating asynchronously.
- After completing the functionality I created unit and integration test cases using Unit test Cases. 
### Major Upgrade
- Later I wanted to upgrade this whole project and thought to trigger and handle all this behaviour using an API.

## Tech Stack
1. Python
2. Quart - (official reimplementation of Flask using async/await)
3. Docker
4. Hypercorn - (ASGI, brother of Gunicorn(WSGI))
5. HTML, CSS
6. Javascript

## Installation

1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage
### Method 1: Normal
1. Start the Quart server:

    ```
    python app.py
    ```

2. Access the web interface by navigating to `http://localhost:5000` in your web browser.

3. Click on the "Run Agents" button to start the agents. You will see log messages displayed on the UI as the agents execute their behaviors and communicate with each other.

4. To stop the agents, click on the "Stop Agents" button.

### Method 2: Docker
1. First build the image: (Note: make sure docker engine is running in background in your system)
    ```
    docker build -t your_tag_name .
    ```

2. Then run the container in daemon mode or as one like (I prefer it as it automatically takes in the changes made).
    ```
    docker run -dp 8080:8080 -w /app -v "path/to/pwd:/app" your_tag_name
    ```
3. Access the web interface by navigating to `http://localhost:8080` in your web browser.

