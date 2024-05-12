""" app.py
This is an Asynchronous app developed using Quart, Hypercorn and Docker.
This app demonstrates the interaction between concrete instances of an Autonomous Agent.
The agents exchange messages through their outboxes and inboxes, running behaviors concurrently.
"""
import asyncio
import logging

from quart import Quart, jsonify, render_template

from agents.concrete_agent import ConcreteAgent
from configs.config import AGENT_TASKS, LOG_MESSAGES, RUN_BUTTON_ENABLED, STOP_BUTTON_ENABLED
from lib.utility import display_log

app = Quart(__name__)

agent1 = ConcreteAgent()
agent2 = ConcreteAgent()

async def run_agents():
    """
    Runs async function does the job of connecting and starting the agents asynchronously.
    """
    try:
        display_log("Preparing the agents.")
        # Connect: the agents outboxes to each other's inboxes
        agent1.outbox = agent2.inbox
        agent2.outbox = agent1.inbox

        # Start: consuming messages and running behaviors for each agent
        display_log("Starting the agents with:")
        display_log("behaviour: to generate random 2-word messages.")
        display_log(
            "handler: to filters messages for the keyword 'hello' and then print its content."
        )
        tasks = [
            asyncio.create_task(agent1.consume_messages()),
            asyncio.create_task(agent2.consume_messages()),
            asyncio.create_task(agent1.run_behaviors()),
            asyncio.create_task(agent2.run_behaviors()),
        ]

        # Add: the tasks to the global list
        global AGENT_TASKS
        AGENT_TASKS = tasks

        # Wait: for all tasks to complete
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        display_log("Stopping the agents.")
    except asyncio.CancelledError:
        display_log("Agents are commanded to stop working.")
        raise
    except Exception as e:
        logging.exception(f"Oops! Our agents are down due to some internal error: {e}")


@app.route("/")
async def index():
    """
    This is starter endpoint of app.
    Provides choices like running and stopping the agent's asynchronous communications. 
    """
    return await render_template("index.html")


@app.route("/run_agents")
async def run_agents_route():
    """
    This endpoint instantiates the asynchronous working of agents instances.
    """
    global RUN_BUTTON_ENABLED, STOP_BUTTON_ENABLED
    try:
        LOG_MESSAGES.clear()
        asyncio.create_task(run_agents())  # Start: the agents asynchronously
        await asyncio.sleep(1)
        RUN_BUTTON_ENABLED = False
        STOP_BUTTON_ENABLED = True
        return "Accepted the command to invoke the sleeping agents."
    except asyncio.CancelledError:
        display_log("Agents have been stopped successfully!")
        LOG_MESSAGES.clear()
        return "Agents have been put to sleep successfully!"


@app.route("/stop_agents")
async def stop_agents_route():
    """
    This endpoint stops all the asynchronous action going on between the agents.
    """
    global RUN_BUTTON_ENABLED, STOP_BUTTON_ENABLED
    try:
        for task in AGENT_TASKS:
            task.cancel()
        await asyncio.gather(
            *AGENT_TASKS, return_exceptions=True
        )    # Wait: for all tasks to be cancelled
        display_log("All agents have been stopped.")
        LOG_MESSAGES.clear()
        RUN_BUTTON_ENABLED = True
        STOP_BUTTON_ENABLED = False
        return "Agents have been put to sleep successfully!"
    except Exception as e:
        logging.exception(f"Oops! Error occurred while stopping agents: {e}")
        return "Error occurred while stopping agents."


@app.route("/button_states")
async def get_button_states():
    """
    This endpoint handles the states of trigger buttons.
    """
    return jsonify({"startEnabled": RUN_BUTTON_ENABLED, "stopEnabled": STOP_BUTTON_ENABLED})


@app.route("/log_messages")
async def get_log_messages():
    """
    This endpoint handles the logged messages and renders them to UI.
    """
    return jsonify(LOG_MESSAGES)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s - %(message)s")
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        display_log("Shutting down: Exiting...")
    except Exception as e:
        logging.exception(f"Oops! System Failed to load as: {e}")
    finally:
        pass
