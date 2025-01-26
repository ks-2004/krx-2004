import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.title("Worker Requirement Form")

# Dropdown for employment type
employment_types = [
    "Carpentry", "Plumbing", "Painting", "Home Workers", "Craftsmen",
    "Electricians", "Peons", "Sculptors"
]
employment_type = st.selectbox("Select Employment Type", employment_types)

# Number input for number of workers needed
num_workers = st.number_input("Number of Workers Needed", min_value=1, step=1)

# Text input for location
location = st.text_input("Location", "")

# Email credentials (update with your actual email and app password)
sender_email = "22b883@nssce.ac.in"
sender_password = "jlrb dfye gpkt ihjn"
receiver_email = "22b379@nssce.ac.in"

# Submit button
if st.button("Submit"):
    if location.strip():
        # Display success message
        st.success(f"Request submitted successfully!\n\nEmployment Type: {employment_type}\nNumber of Workers: {num_workers}\nLocation: {location}")

        # Create email content
        subject = "New Worker Requirement Submission"
        body = f"""
        Worker Requirement Details:
        Employment Type: {employment_type}
        Number of Workers: {num_workers}
        Location: {location}
        """

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            # Send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                st.info("Details have been sent to the specified email.")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
    else:
        st.error("Please enter a valid location.")
