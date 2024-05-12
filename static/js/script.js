//static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    // Function: to fetch and display log messages
    function fetchLogMessages() {
        fetch("/log_messages")
            .then(response => response.json())
            .then(messages => {
                const logMessagesElement = document.getElementById("logMessages");
                logMessagesElement.innerHTML = ""; // Clear: previous messages
                messages.forEach(message => {
                    const messageElement = document.createElement("div");
                    messageElement.textContent = message;
                    logMessagesElement.appendChild(messageElement);
                });
            })
            .catch(error => console.error("Error fetching log messages:", error));
    }

    // Function: to fetch button states
    function fetchButtonStates() {
        fetch("/button_states")
            .then(response => response.json())
            .then(states => {
                toggleButtons(states.startEnabled, states.stopEnabled);
            })
            .catch(error => console.error("Error fetching button states:", error));
    }

    // Fetch: log messages initially
    fetchLogMessages();

    // Fetch: button states initially
    fetchButtonStates();

    // Fetch: log messages periodically
    setInterval(fetchLogMessages, 5000); // Fetch every 5 seconds

    // Fetch: button states periodically
    setInterval(fetchButtonStates, 5000); // Fetch every 5 seconds

    // Function: to toggle buttons
    function toggleButtons(startEnabled, stopEnabled) {
        document.getElementById("runAgentsBtn").disabled = !startEnabled;
        document.getElementById("stopAgentsBtn").disabled = !stopEnabled;
        console.log("Start Button Disabled:", !startEnabled);
        console.log("Stop Button Disabled:", !stopEnabled);
    }

    document.getElementById("runAgentsBtn").addEventListener("click", function() {
        fetch("/run_agents")
            .then(response => response.text())
            .then(message => {
                document.getElementById("logMessages").innerHTML += message;
            var messageContainer = document.getElementById("message_container");
            messageContainer.scrollTop = messageContainer.scrollHeight;
            })
            .catch(error => console.error("Error:", error));
    });

    document.getElementById("stopAgentsBtn").addEventListener("click", function() {
        fetch("/stop_agents")
            .then(response => response.text())
            .then(message => {
                alert(message);
            })
            .catch(error => console.error("Error:", error));
    });
});
