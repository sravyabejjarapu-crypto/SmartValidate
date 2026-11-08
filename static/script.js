
const usernameInput = document.getElementById("usernameInput");
const usernameBtn = document.getElementById("usernameBtn");
const usernameResult = document.getElementById("usernameResult");
const usernameDetails = document.getElementById("usernameDetails");

usernameBtn.addEventListener("click", validateUsername);

usernameInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        validateUsername();
    }
});

async function validateUsername() {
    const username = usernameInput.value;

    try {
        usernameBtn.disabled = true;
        usernameBtn.textContent = "Checking...";

        const response = await fetch("/validate/username", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username
            })
        });

        const data = await response.json();

        usernameResult.className = data.valid
            ? "result-box valid"
            : "result-box invalid";

        usernameResult.textContent = data.valid
            ? "✓ VALID USERNAME"
            : "✕ INVALID USERNAME";

        usernameDetails.replaceChildren();

        const reason = document.createElement("p");
        reason.textContent = "Reason: " + data.reason;

        const finalState = document.createElement("p");
        finalState.textContent = "Final DFA State: " + data.final_state;

        const regex = document.createElement("p");
        regex.textContent = "Regex Result: " +
            (data.regex_match ? "Accepted" : "Rejected");

        const heading = document.createElement("h3");
        heading.textContent = "DFA Transition History";

        const list = document.createElement("ul");

        data.transitions.forEach(function(transition) {
            const item = document.createElement("li");
            item.textContent = transition;
            list.appendChild(item);
        });

        usernameDetails.append(
            reason,
            finalState,
            regex,
            heading,
            list
        );

    } catch (error) {
        usernameResult.className = "result-box invalid";
        usernameResult.textContent =
            "Unable to connect to the server. Please try again.";

        usernameDetails.textContent = "";
        console.error(error);

    } finally {
        usernameBtn.disabled = false;
        usernameBtn.textContent = "Validate Username →";
    }
}

const mobileInput = document.getElementById("mobileInput");
const mobileBtn = document.getElementById("mobileBtn");
const mobileResult = document.getElementById("mobileResult");
const mobileDetails = document.getElementById("mobileDetails");

mobileBtn.addEventListener("click", validateMobile);

mobileInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        validateMobile();
    }
});

async function validateMobile() {
    const mobile = mobileInput.value;

    try {
        mobileBtn.disabled = true;
        mobileBtn.textContent = "Checking...";

        const response = await fetch("/validate/mobile", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                mobile: mobile
            })
        });

        const data = await response.json();

        mobileResult.className = data.valid
            ? "result-box valid"
            : "result-box invalid";

        mobileResult.textContent = data.valid
            ? "✓ VALID MOBILE NUMBER"
            : "✕ INVALID MOBILE NUMBER";

        mobileDetails.replaceChildren();

        const reason = document.createElement("p");
        reason.textContent = "Reason: " + data.reason;

        const finalState = document.createElement("p");
        finalState.textContent =
            "Final DFA State: " + data.final_state;

        const regex = document.createElement("p");
        regex.textContent = "Regex Result: " +
            (data.regex_match ? "Accepted" : "Rejected");

        const heading = document.createElement("h3");
        heading.textContent = "DFA Transition History";

        const list = document.createElement("ul");

        data.transitions.forEach(function(transition) {
            const item = document.createElement("li");
            item.textContent = transition;
            list.appendChild(item);
        });

        mobileDetails.append(
            reason,
            finalState,
            regex,
            heading,
            list
        );

    } catch (error) {
        mobileResult.className = "result-box invalid";
        mobileResult.textContent =
            "Unable to connect to the server. Please try again.";

        mobileDetails.textContent = "";
        console.error(error);

    } finally {
        mobileBtn.disabled = false;
        mobileBtn.textContent = "Validate Mobile Number →";
    }
}
// EMAIL VALIDATION

const emailInput = document.getElementById("emailInput");
const emailBtn = document.getElementById("emailBtn");
const emailResult = document.getElementById("emailResult");
const emailDetails = document.getElementById("emailDetails");

emailBtn.addEventListener("click", validateEmail);

emailInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        validateEmail();
    }
});

async function validateEmail() {
    const email = emailInput.value.trim();

    try {
        emailBtn.disabled = true;
        emailBtn.textContent = "Checking...";

        const response = await fetch("/validate/email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email })
        });

        const data = await response.json();

        emailResult.className = data.valid
            ? "result-box valid"
            : "result-box invalid";

        emailResult.textContent = data.valid
            ? "✓ VALID EMAIL ADDRESS"
            : "✕ INVALID EMAIL ADDRESS";

        emailDetails.replaceChildren();

        const reason = document.createElement("p");
        reason.textContent = "Reason: " + data.reason;

        const finalState = document.createElement("p");
        finalState.textContent = "Final DFA State: " + data.final_state;

        const regex = document.createElement("p");
        regex.textContent = "Regex Result: " +
            (data.regex_match ? "Accepted" : "Rejected");

        const heading = document.createElement("h3");
        heading.textContent = "DFA Transition History";

        const list = document.createElement("ul");

        data.transitions.forEach(function(transition) {
            const item = document.createElement("li");
            item.textContent = transition;
            list.appendChild(item);
        });

        emailDetails.append(reason, finalState, regex, heading, list);

    } catch (error) {
        emailResult.className = "result-box invalid";
        emailResult.textContent =
            "Unable to connect to the server. Please try again.";

        console.error(error);

    } finally {
        emailBtn.disabled = false;
        emailBtn.textContent = "Validate Email →";
    }
}