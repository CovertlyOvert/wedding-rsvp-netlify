from flask import Blueprint, request, redirect, url_for, render_template, os
from twilio.twiml.messaging_response import MessagingResponse
from app.models import save_rsvp

main = Blueprint('main', __name__)

#Root route
@main.route('/')
def index():
    print("Current working directory:", os.getcwd())
    return render_template('index.html')

#Whatsapp 
@main.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    phone_number = request.values.get('From', '').split(':')[-1]  # Extract the phone number
    resp = MessagingResponse()
    msg = resp.message()

    if 'yes' in incoming_msg:
        # Generate a URL with the phone number as a query parameter
        netlify_url = f"https://66c21c0a832d57a435f489ee--sprightly-cucurucho-511aaa.netlify.app/?phone_number={phone_number}"
        msg.body(f"Great! Please complete your RSVP by clicking the link below:\n{netlify_url}")
    elif 'no' in incoming_msg:
        msg.body('Sorry to hear that! Let us know if anything changes.')
        save_rsvp(phone_number, None, 'No', None, None, None)
    else:
        msg.body('Please reply with YES or NO for the RSVP.')

    return str(resp)

@main.route('/submit_rsvp', methods=['POST'])
def submit_rsvp():
    name = request.form['name']
    attendance = request.form['attendance']
    arrival_date = request.form['arrival_date']
    departure_date = request.form['departure_date']
    guests = request.form['guests']

    # Handle the phone number safely, defaulting to None if "None" is passed
    phone_number = request.form.get('phone_number')
    if phone_number == 'None':
        phone_number = None

    # Save the data to the database
    save_rsvp(phone_number, name, attendance, arrival_date, departure_date, guests)

    # Redirect or confirm after submission
    return "Thank you for your RSVP!"
