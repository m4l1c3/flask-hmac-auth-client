# flask-hmac-auth-client
Python client library for flask-hmac-auth

# Use:
Create an environment variable named APIKEY:

<code>
export APIKEY="WHATEVER_YOU_WANT!!!"
</code>

<code>
from flask_hmac_auth_client import MessageAuthentication()

a = MessageAuthentication()

a.compute('a', 'a')
</code>
