import os, requests
from local import send_email
from data import fetch_jobs
from datetime import datetime, timedelta

DEBUG = False


def main() -> None:
    """
    Send email with the latest internship postings.
    """

    # Get the current time; check the previous day
    time = (datetime.now() - timedelta(days=1)).isoformat()

    [plaintext_list, html_list] = fetch_jobs(time)

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

    subject = f"[jobs-notify] New internship postings! ({time[0:10]})"

    send_email(subject=subject, plaintext_email=plaintext_email, html_email=html_email)


if __name__ == "__main__":
    main()
