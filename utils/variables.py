"""Variables used in the monitor."""

import os

import dotenv

dotenv.read_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


def get_env_variable(var_name):
    """Get environment variables."""
    try:
        return os.environ[var_name]
    except KeyError:
        raise ValueError(
            "Set the %s environment variable" % var_name)


# set the headers like we are a browser,
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)' +
    ' AppleWebKit/537.36 (KHTML, like Gecko)' +
    ' Chrome/39.0.2171.95 Safari/537.36'}
SENDER_EMAIL = get_env_variable('EMAIL_ADDRESS')
SENDER_EMAIL_PASSWORD = get_env_variable('EMAIL_PASSWORD')
