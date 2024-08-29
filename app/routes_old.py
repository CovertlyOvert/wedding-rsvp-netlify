from flask import Blueprint, request, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
from app.models import save_rsvp

main = Blueprint('main', __name__)

@main.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    phone_number = request.values.get('From', '').split(':')[-1]
    resp = MessagingResponse()
    msg = resp.message()

    if 'yes' in incoming_msg:
        msg.body(f"Great! Please complete your RSVP by clicking the link below:\nhttps://66c21c0a832d57a435f489ee--sprightly-cucurucho-511aaa.netlify.app/")
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
    phone_number = request.form['phone_number']
    
     # Save the data to the database
    save_rsvp(phone_number, name, attendance, arrival_date, departure_date, guests)

    # After saving, redirect to a thank you page or return a confirmation message
    return "Thank you for your RSVP!"