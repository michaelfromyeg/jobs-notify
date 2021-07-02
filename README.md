# jobs-notify

E-mail me when there are new jobs to apply to.

Inspired by [internship-notify](https://github.com/Bryce-MW/internship-notify/blob/main/notify.py).

## Usage

Install `python`. Setup a virtual environment, such as `python -m venv env`.

Setup your environment variables in a `.env` file. If you'd like to use Gmail, you'll likely need an [app password](https://support.google.com/accounts/answer/185833?hl=en).

Run `pip install -r requirements.txt`.

Finally, do `python3 notify.py`.

A cool way to use this project is via a cron

## Notes

To update the `.env` file, run

```shellscript
sed 's/=.*/=/' .env > .env.example
```