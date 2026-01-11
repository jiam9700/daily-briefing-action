import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504)
) -> requests.Session:
    """
    Creates a Requests Session with automatic retry mechanism.
    
    :param retries: Maximum number of retries.
    :param backoff_factor: A backoff factor to apply between attempts after the second try.
                           (sleep = {backoff factor} * (2 ** ({number of total retries} - 1)))
    :param status_forcelist: A set of HTTP status codes that we should force a retry on.
    :return: requests.Session object with retry adapter mounted.
    """
    session = requests.Session()
    
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session