"""
Created by:Shawn Adams boris317
https://gist.github.com/boris317/3783153
"""

from app import app
import IPython

app.testing = True
test_client = app.test_client()

welcome_message = """Welcome to your Flask CLI environment. 
The following variables are available to use:
app           -> Your Flask app instance.
test_client   -> Your Flask app.test_client().
"""

IPython.embed(header=welcome_message)
