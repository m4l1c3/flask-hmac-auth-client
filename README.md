# flask-hmac-auth-client
Python client library for flask-hmac-auth

# Use:
- Create an environment variable named APIKEY:

<code>
export APIKEY="WHATEVER_YOU_WANT!!!"
</code>

<code>
from flask_hmac_auth_client import MessageAuthentication()<br/>

a = MessageAuthentication()<br/>

a.compute('a', 'a')<br/>
</code>
