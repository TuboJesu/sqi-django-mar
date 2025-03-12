window.onload = function () {
    // Create overlay
    let overlay = document.createElement("div");
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.width = "100%";
    overlay.style.height = "100%";
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    overlay.style.display = "flex";
    overlay.style.justifyContent = "center";
    overlay.style.alignItems = "center";
    overlay.style.zIndex = "1000";

    // Create modal box
    let modal = document.createElement("div");
    modal.style.backgroundColor = "white";
    modal.style.padding = "20px";
    modal.style.borderRadius = "10px";
    modal.style.boxShadow = "0 4px 8px rgba(0,0,0,0.3)";
    modal.style.textAlign = "center";
    modal.style.width = "300px";
    modal.style.position = "relative"; // Needed for close button

    // Create close button ("X")
    let closeButton = document.createElement("span");
    closeButton.innerHTML = "&times;"; // HTML entity for "×"
    closeButton.style.position = "absolute";
    closeButton.style.top = "10px";
    closeButton.style.right = "15px";
    closeButton.style.fontSize = "20px";
    closeButton.style.cursor = "pointer";
    closeButton.style.color = "#333";

    // Close modal when "X" is clicked
    closeButton.onclick = function () {
        document.body.removeChild(overlay);
    };

    // Create text message
    let message = document.createElement("p");
    message.textContent = "Enter your email to subscribe to our newsletter:";
    message.style.marginBottom = "10px";

    // Create input field
    let input = document.createElement("input");
    input.type = "email";
    input.placeholder = "Enter your email";
    input.style.width = "100%";
    input.style.padding = "8px";
    input.style.marginBottom = "10px";
    input.style.border = "1px solid #ccc";
    input.style.borderRadius = "5px";

    // Create submit button
    let button = document.createElement("button");
    button.textContent = "Subscribe";
    button.style.padding = "8px 15px";
    button.style.backgroundColor = "#007BFF";
    button.style.color = "white";
    button.style.border = "none";
    button.style.borderRadius = "5px";
    button.style.cursor = "pointer";

    // Close modal on button click
    button.onclick = function () {
        alert("Thank you for subscribing, " + input.value + "!");
        document.body.removeChild(overlay);
    };

    // Append elements
    modal.appendChild(closeButton); // Add close button
    modal.appendChild(message);
    modal.appendChild(input);
    modal.appendChild(button);
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
};
