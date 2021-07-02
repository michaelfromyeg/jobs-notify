import smtplib, ssl, os, requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# The list of repositories to target
repos = (
    "pittcsc/Summer2022-Internships",
    "quantprep/quantinternships2022",
    "ChrisDryden/Canadian-Tech-Internships-Summer-2022",
)

DEBUG = False

if __name__ == "__main__":
    # Load environment variables from project root
    load_dotenv()

    # Get the current time; check the previous day
    time = (datetime.now() - timedelta(days=1)).isoformat()

    count = 0
    html_list = []
    plaintext_list = []
    for repo in repos:
        for res in requests.get(
            f"https://api.github.com/repos/{repo}/commits?since={time}",
            headers={"Accept": "application/vnd.github.v3+json"},
        ).json():
            if DEBUG:
                print(f"Updated commit {res}")
            plaintext_list.append(
                f"{repo}: {res['commit']['message']} <{res['html_url']}> by {res['commit']['author']['name']} on {res['commit']['author']['date']}"
            )
            html_list.append(
                f"<li>{repo}: <a href=\"{res['html_url']}\">{res['commit']['message']}</a> by {res['commit']['author']['name']} on {res['commit']['author']['date']}</li>"
            )
            count += 1

    print(f"There were {count} commits made!")

    message = MIMEMultipart("alternative")
    message["Subject"] = f"[jobs-notify] New internship postings! ({time[0:9]})"

    # Produce the formatted email
    plaintext_email = """\
    Hi {to_name},

    The following internship repositories have been updated within the past day. Good luck!

    {plaintext_list}

    As always, feel free to take a look at the repositories yourself: pittcsc/Summer2022-Internships <https://github.com/pittcsc/Summer2022-Internships>, quantprep/quantinternships2022 <https://github.com/quantprep/quantinternships2022>, ChrisDryden/Canadian-Tech-Internships-Summer-2022, <https://github.com/ChrisDryden/Canadian-Tech-Internships-Summer-2022>

    Best,

    jobs-notify

    """.format(
        to_name=os.environ["TO_NAME"], plaintext_list="".join(plaintext_list)
    )

    html_email = """\
    <html>
        <body>
            <p>Hi {to_name},</p>
            <p>The following internship repositories have been updated within the past day. Good luck!</p>
            <ul>
                {html_list}
            </ul>
            <p>As always, feel free to take a look at the repositories yourself: <a href="https://github.com/pittcsc/Summer2022-Internships">pittcsc/Summer2022-Internships</a>, <a href="https://github.com/quantprep/quantinternships2022">quantprep/quantinternships2022</a>, <a href="https://github.com/ChrisDryden/Canadian-Tech-Internships-Summer-2022">ChrisDryden/Canadian-Tech-Internships-Summer-2022</a></p>
            <p>Best,</p>
            <p>jobs-notify</p>
        </body>
    </html>
    """.format(
        to_name=os.environ["TO_NAME"], html_list="".join(html_list)
    )

    # Turn plaintext, HTML into MIMEText objects
    part1 = MIMEText(plaintext_email, "plain")
    part2 = MIMEText(html_email, "html")

    # The email client will try to render the last part first, i.e., the HTML
    message.attach(part1)
    message.attach(part2)

    if count > 0:
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
