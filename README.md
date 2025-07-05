# GreetingApp_FLASK

A simple and elegant greeting web application built with **Flask**.  
This app displays a friendly message to the user based on their name input.  
It uses a clean UI with HTML, CSS, and Python in the backend — and is structured to be deploy-ready for platforms like **Heroku**.

![Screenshot](https://raw.githubusercontent.com/winterr79/greetingApp_FLASK/main/static/screenshots/screenshot.png)

---

## Features

- Responsive and centered layout
- Flash messaging using Flask
- Simple and minimalistic design
- Clear project structure (`templates`, `static`, `app.py`)
- Deployment-ready with `Procfile` and `requirements.txt`

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/greetingApp_FLASK.git
   cd greetingApp_FLASK
   ```

2. Set up virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   flask run
   ```

   Then open your browser at http://127.0.0.1:5000/hello

## Deployment

This app is configured for Heroku deployment using gunicorn, a Procfile, and a requirements.txt.

**Note:**
I was not able to deploy this on Heroku because I do not currently have access to a credit card, which Heroku now requires for account verification.
The app remains fully functional locally and ready for deployment if needed.

## Author

Harish Kumbar

Inspired by the tutorial originally created by Mariya Sha.
You can watch her original YouTube tutorial here: Create a Web App with Flask

## License

This project is shared for learning purposes and can be freely used or adapted.