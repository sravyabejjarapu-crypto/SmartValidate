
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


# --------------------------------
# 1. USERNAME VALIDATOR USING DFA
# --------------------------------

def validate_username(username):
    transitions = []
    state = 0
    reason = "Valid username."

    if not username:
        return {
            "valid": False,
            "reason": "Username cannot be empty.",
            "final_state": "q0",
            "transitions": [],
            "regex_match": False
        }

    for char in username:
        if state == 0:
            if char.isascii() and char.isalpha():
                state = 1
            else:
                state = -1
        elif state < 15:
            if char.isascii() and (char.isalnum() or char == "_"):
                state += 1
            else:
                state = -1
        else:
            state = -1

        transitions.append(
            f"After '{char}' -> {'REJECT' if state == -1 else 'q' + str(state)}"
        )

        if state == -1:
            reason = "Username must start with a letter and contain only letters, digits, or underscores."
            break

    regex_match = bool(
        re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,14}", username)
    )

    valid = state >= 5 and state <= 15 and regex_match

    if not valid and state != -1:
        reason = "Username must contain 5 to 15 characters."

    return {
        "valid": valid,
        "reason": reason,
        "final_state": "REJECT" if state == -1 else f"q{state}",
        "transitions": transitions,
        "regex_match": regex_match
    }


# --------------------------------
# 2. MOBILE NUMBER VALIDATOR USING DFA
# --------------------------------

def validate_mobile(mobile):
    transitions = []
    state = 0
    reason = "Valid mobile number."

    if not mobile:
        return {
            "valid": False,
            "reason": "Mobile number cannot be empty.",
            "final_state": "q0",
            "transitions": [],
            "regex_match": False
        }

    for char in mobile:
        if state == 0:
            if char in "6789":
                state = 1
            else:
                state = -1
        elif 1 <= state < 10:
            if char.isascii() and char.isdigit():
                state += 1
            else:
                state = -1
        else:
            state = -1

        transitions.append(
            f"After '{char}' -> {'REJECT' if state == -1 else 'q' + str(state)}"
        )

        if state == -1:
            reason = "Mobile number must start with 6, 7, 8, or 9 and contain only digits."
            break

    regex_match = bool(re.fullmatch(r"[6-9][0-9]{9}", mobile))
    valid = state == 10 and regex_match

    if not valid and state != -1:
        reason = "Mobile number must contain exactly 10 digits."

    return {
        "valid": valid,
        "reason": reason,
        "final_state": "REJECT" if state == -1 else f"q{state}",
        "transitions": transitions,
        "regex_match": regex_match
    }


# --------------------------------
# 3. EMAIL VALIDATOR USING DFA + REGEX
# --------------------------------

def validate_email(email):
    transitions = []
    state = "q0"
    reason = "Valid email address."

    if not email:
        return {
            "valid": False,
            "reason": "Email address cannot be empty.",
            "final_state": "q0",
            "transitions": [],
            "regex_match": False
        }

    for char in email:

        if state == "q0":
            if char.isascii() and char.isalnum():
                state = "q1"
            else:
                state = "REJECT"

        elif state == "q1":
            if char.isascii() and char.isalnum():
                state = "q1"
            elif char in "._%+-":
                state = "q1"
            elif char == "@":
                state = "q2"
            else:
                state = "REJECT"

        elif state == "q2":
            if char.isascii() and char.isalnum():
                state = "q3"
            else:
                state = "REJECT"

        elif state == "q3":
            if char.isascii() and char.isalnum():
                state = "q3"
            elif char == "-":
                state = "q3"
            elif char == ".":
                state = "q4"
            else:
                state = "REJECT"

        elif state == "q4":
            if char.isascii() and char.isalpha():
                state = "q5"
            else:
                state = "REJECT"

        elif state == "q5":
            if char.isascii() and char.isalpha():
                state = "q5"
            elif char == ".":
                state = "q4"
            else:
                state = "REJECT"

        transitions.append(f"After '{char}' -> {state}")

        if state == "REJECT":
            reason = "Email contains invalid characters or an invalid format."
            break

    email_pattern = (
        r"[A-Za-z0-9][A-Za-z0-9._%+-]*"
        r"@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+"
    )

    regex_match = bool(re.fullmatch(email_pattern, email))

    parts = email.split("@")

    local_valid = False
    domain_valid = False

    if len(parts) == 2:
        local_part = parts[0]
        domain_part = parts[1]

        local_valid = (
            len(local_part) > 0
            and not local_part.startswith(".")
            and not local_part.endswith(".")
            and ".." not in local_part
        )

        domain_labels = domain_part.split(".")

        domain_valid = (
            len(domain_labels) >= 2
            and all(
                label
                and not label.startswith("-")
                and not label.endswith("-")
                for label in domain_labels
            )
            and all(label.isascii() and label.isalnum() or
                    (label.isascii() and all(c.isalnum() or c == "-" for c in label))
                    for label in domain_labels)
        )

    valid = (
        state == "q5"
        and regex_match
        and local_valid
        and domain_valid
    )

    if not valid and state != "REJECT":
        reason = "Please enter a valid email address with a proper username and domain."

    return {
        "valid": valid,
        "reason": reason,
        "final_state": state,
        "transitions": transitions,
        "regex_match": regex_match
    }


# --------------------------------
# FLASK ROUTES
# --------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/validate/username", methods=["POST"])
def username_route():
    data = request.get_json()
    username = data.get("username", "")
    return jsonify(validate_username(username))


@app.route("/validate/mobile", methods=["POST"])
def mobile_route():
    data = request.get_json()
    mobile = data.get("mobile", "")
    return jsonify(validate_mobile(mobile))


@app.route("/validate/email", methods=["POST"])
def email_route():
    data = request.get_json()
    email = data.get("email", "")
    return jsonify(validate_email(email))


# --------------------------------
# RUN APPLICATION
# --------------------------------

if __name__ == "__main__":
    app.run(debug=True)
