const chatBox = document.getElementById("chatBox");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearBtn");


// Add a message to the chat
function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    if (sender === "user") {

        messageDiv.className = "message user-message";

        messageDiv.innerHTML = `
            <div class="avatar">👤</div>

            <div class="message-content">
                <div class="sender">You</div>
                <div class="bubble">${message}</div>
            </div>
        `;

    } else {

        messageDiv.className = "message ai-message";

        messageDiv.innerHTML = `
            <div class="avatar">🤖</div>

            <div class="message-content">
                <div class="sender">Gemini</div>
                <div class="bubble">${message}</div>
            </div>
        `;
    }

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// Show loading message
function showLoading() {

    const loadingDiv = document.createElement("div");

    loadingDiv.id = "loadingMessage";
    loadingDiv.className = "message ai-message";

    loadingDiv.innerHTML = `
        <div class="avatar">🤖</div>

        <div class="message-content">
            <div class="sender">Gemini</div>

            <div class="bubble loading">
                Gemini is thinking... 🤔
            </div>
        </div>
    `;

    chatBox.appendChild(loadingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// Remove loading message
function removeLoading() {

    const loadingMessage =
        document.getElementById("loadingMessage");

    if (loadingMessage) {
        loadingMessage.remove();
    }
}


// Send message to backend
async function sendMessage() {

    const message = messageInput.value.trim();

    if (message === "") {
        return;
    }

    // Display user's message
    addMessage(message, "user");

    // Clear input
    messageInput.value = "";

    // Disable button
    sendBtn.disabled = true;

    // Show loading
    showLoading();

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        removeLoading();

        if (!response.ok) {

    if (response.status === 429) {
        addMessage(
            "⚠️ Gemini API quota has been reached. The AI service is temporarily unavailable.",
            "ai"
        );
    } else {
        addMessage(
            "⚠️ Something went wrong. Please try again.",
            "ai"
        );
    }

    return;
}

        // Display Gemini response
        addMessage(data.response, "ai");

    } catch (error) {

        removeLoading();

        console.error(error);

        addMessage(
            "⚠️ Unable to connect to the Gemini backend. Make sure the backend is running.",
            "ai"
        );

    } finally {

        sendBtn.disabled = false;

        messageInput.focus();
    }
}


// Send button
sendBtn.addEventListener("click", sendMessage);


// Press Enter to send
messageInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});


// Clear chat
clearBtn.addEventListener("click", function() {

    chatBox.innerHTML = "";

    addMessage(
        "Chat cleared! 👋 How can I help you?",
        "ai"
    );

});