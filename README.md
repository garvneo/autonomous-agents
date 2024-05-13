# Autonomous Agents (an Asynchronous Web App)

- This project is an upgraded version of project **[async-autonomous-agent-basic.](https://github.com/garvneo/autonomous-agent-basic/pull/1)**
- This project demonstrates the implementation of asynchronous handling of communication and behaviour of autonomous agents using **asyncio, Quart(official async implementation of Flask)**, a Python web framework, for the backend, and HTML, CSS, and JavaScript for the frontend, utilizes **Docker for containerization and Hypercorn as ASGI for deployment on production server**. Also this project is live on internet.
- **Autonomous Agents Web App's: [live site](https://autonomous-agents.onrender.com/)**
![upgraded-autonomous-agent](https://github.com/garvneo/autonomous-agents/assets/97349044/9e09072d-c394-4458-90df-1fcc750d7728)

## Tech Stack
1. **Python - (asyncio, unittest, logging, datetime etc)**
2. **[Quart](https://palletsprojects.com/p/quart/) - (official reimplementation of Flask using async/await)**
3. **Docker - for containerization**
4. **[Hypercorn](https://pypi.org/project/Hypercorn/) - (ASGI for production deployment, brother of Gunicorn(WSGI))**
5. **HTML, CSS - (front end)**
6. **Javascript - (front to back interconnectivity)**
7. **[Ruff](https://docs.astral.sh/ruff/) - for linting & formatting**

## Design:
### 1. Basic Implementation
- Picked 'asyncio' standard library of python to implement this project. 
- Created a folder named 'agents'.
- Developed a module 'agents\autonomous_agent.py' as a blueprint for the 'Autonomous Agent', addressing its reactivity, proactivity, behaviors, and asynchronous message handling.
- Implemented a module 'agents\concrete_agent.py' which somewhat follows the blueprint of 'Autonomous Agent' or inherits 'agents\autonomous_agent.py'.
- Utilized 'Queue' data structure to manage messages in InBoxes and OutBoxes, and dictionaries and lists for message handlers and behaviors, respectively.
- Created a simple 'app.py' acting as a controller, where instances of concrete classes were created, their inboxes linked to outboxes, and behaviors invoked asynchronously, enabling agents to communicate asynchronously.
- Developed unit and integration test cases using Python's standard library 'Unittest'.
   
### 2. Upgraded Basic project to WEB APP
- Later I wanted to upgrade this whole project and thought to trigger and handle all this behaviour via API calls incorporated in a web app and publish it on internet.
- **Followed MVC Architecture** to implement the upgrade.
- Utilized the benefit of modularity of previous basic build and started scaling the project on top of it.
- Usually Flask is the goto option for me for APIs but it is mostly used for synchronous programming and our's problem was to handle asynchronous calls, hence I went ahed and picked **[Quart](https://palletsprojects.com/p/quart/)** which is another very good offering by **[Pallets Projects](https://palletsprojects.com/)** beside from Flask, hence a great appreciation to them for this.
- So now I had Quart which can handle asynchronous programming and with this I made the 'app.py'.
- Once API app was done, I went ahead and created the templates and static js and css code for UI part.
- After UI, implemented docker for containerization.
- Implemeted [Hypercorn](https://pypi.org/project/Hypercorn/) as Asynchronous Server Gateway Interface for production deployment.
- Wrote Readme.md
- Pushed to GitHub
- Created a webservice on a hosting platform and configured & published this webapp there, and set the configuration to auto publish on merged commits.
- **Result:** [web app is live](https://autonomous-agents.onrender.com/). {Click on button 'Run Agents' to invoke instances of agents and on 'Stop Agents' to put them to sleep.}
<img width="1254" alt="Screenshot 2024-05-13 044616" src="https://github.com/garvneo/autonomous-agents/assets/97349044/0490431a-045e-482f-9bc2-3e0c09b79b04">

### 3. Best practices followed:
1. Utilized 'Ruff' for making code more Pythonic and also added 'ruff.toml' to ensure that same rules of linting & formatting can be followed by all who will be contributing to the project.
2. Ensured modular code design for increased maintainability and scalability.
3. Incorporated test cases for ensuring better project delivery.
4. Exception handling has been utilized for more robustness.
5. Incorporated logging which can come very handy in debugging production failures and also in multiple other scenarios.
6. Applied MVC architecture methodology.

### 4. Proposed Future Enhancements:
1. **'Redis'** can be incorporated as a message broker queue.
2. For much bigger upgrade the UI, API and the core functionality can be separated in three different microservices altogether.

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
