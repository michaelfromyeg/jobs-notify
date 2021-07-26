import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv
from notify import generate_email

DEBUG = True


def main() -> None:
    """
    Send email via local machine with the latest internship postings.
    """
    load_dotenv(find_dotenv())

    [subject, plaintext_email, html_email] = generate_email()

    send_email(subject=subject, plaintext_email=plaintext_email, html_email=html_email)

    return None


def send_email(subject: str, plaintext_email: str, html_email: str) -> None:
    """
    Send email via Gmail, using local environment variables.
    """
    # Load environment variables from project root
    load_dotenv()

    message = MIMEMultipart("alternative")
    message["Subject"] = subject

    # Turn plaintext, HTML into MIMEText objects
    part1 = MIMEText(plaintext_email, "plain")
    part2 = MIMEText(html_email, "html")

    # The email client will try to render the last part first, i.e., the HTML
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP_SSL(
        os.environ["MAIL_SERVER"],
        os.environ["MAIL_PORT"],
        context=ssl.create_default_context(),
    ) as server:
        # Enable debugging
        if DEBUG:
            server.set_debuglevel(2)

        # Send email
        server.login(os.environ["MAIL_USERNAME"], os.environ["MAIL_PASSWORD"])
        server.sendmail(
            os.environ["FROM_EMAIL"], os.environ["TO_EMAIL"], message.as_string()
        )

        # Print the email we sent
        print(f"Sent the following email:\n{plaintext_email}")


if __name__ == "__main__":
    main()
