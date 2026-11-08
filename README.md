# SmartValidate – Input Validation System

## 1. Project Overview

SmartValidate is an integrated input validation system developed using concepts of Automata Theory and Compiler Design.

It validates usernames, Indian mobile numbers and email addresses using Deterministic Finite Automata (DFA) and Regular Expressions.

The application identifies valid and invalid inputs and displays rejection reasons, final DFA states and transition histories.

## 2. Objectives

- To understand the practical applications of Finite Automata.
- To implement DFA-based input validation.
- To use Regular Expressions for pattern matching.
- To identify and reject invalid input formats.
- To display DFA transition histories and validation results.

## 3. Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Concepts: DFA and Regular Expressions
- Development Tool: Visual Studio Code

## 4. Modules

### Username Validator

Rules:
- Must start with an English letter.
- Length must be between 5 and 15 characters.
- Allows letters, digits and underscores.

Regular Expression:

`[A-Za-z][A-Za-z0-9_]{4,14}`

### Mobile Number Validator

Rules:
- Must contain exactly 10 digits.
- Must start with 6, 7, 8 or 9.
- Only digits from 0 to 9 are allowed.

Regular Expression:

`[6-9][0-9]{9}`

### Email Address Validator

Rules:
- Must contain a valid username.
- Must include the @ symbol.
- Must contain a valid domain and extension.

Regular Expression:

`[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+`

## 5. Working Process

1. User enters an input.
2. JavaScript sends the input to the Flask backend.
3. The DFA processes the input character by character.
4. Regular Expressions check the input pattern.
5. The system displays the validation result.
6. The application displays the rejection reason and DFA transition history.

## 6. Project Structure

```text
SmartValidate/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## 7. How to Run the Project

Install Flask:

```bash
pip install Flask
```

Run the application:

```bash
python app.py
```

Open the browser:

```text
http://127.0.0.1:5000/
```

## 8. Expected Output

The application displays:
- Valid or invalid input status.
- Reason for rejection.
- Final DFA state.
- Regular Expression result.
- DFA transition history.

## 9. Conclusion

SmartValidate demonstrates how Finite Automata and Regular Expressions can be applied to real-world input validation. It provides a practical understanding of DFA states, transitions, pattern recognition and rejection of invalid inputs.