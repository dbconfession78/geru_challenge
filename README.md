Installation
=============
from a comand line:
- navigate to the download location
- run 'source ./geru_setup'

Use
===
* start server: 'geru_start'
* stop server: 'geru_stop'

In a browser or curl from the command line:
   * localhost:6543/ - returns the lading page
   * localhost:6543/quotes - returns all quotes
   * localhost:6543/quotes/<1-19> - returns a specific quote
   * localhost:6543/quotes/random - returns a random quote

api:
	* all requests from a specific session id - localhost:6543/api/user_requests
	* localhost:6543/api/user_requests?=<session_id>