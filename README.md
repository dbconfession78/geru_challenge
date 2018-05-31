DESCRIPTION
===========
This application queries a remote 'Zen of Python' dictionary to:
	 - display all 19 lines from the dictionary
	 - display a specific quote and quote number from the dictionary
	 - display a random quote and quote number from the dictionary

The application assigns a unique uuid4 id to each unique browser that makes a reuqest. This id, along with the requested page and time are recorded in a sqlite3 database available for query by a RESTful API.

INSTALLATION
============
from the comand line:
- navigate to the download location
- run 'source ./geru_setup'

USE
===
NOTE: THis is intended for development and uses a virtual environment. This means that, environmental variables and aliasaes created in setup will not persist between terminal instances

At a command-line prompt:
   * 'geru_start': starts the server. if it is already running, it will restart
   * 'geru_stop': stops the server
   * 'geru_restart': stops and starts the server

In a browser (or curl from CLI):
   * localhost:6543/ - returns the landing page
   * localhost:6543/quotes - returns all quotes (strict slashes enforced)
   * localhost:6543/quotes/<1-19> - returns a specific quote
   * localhost:6543/quotes/random - returns a random quote

api:
  * localhost:6543/api/session_requests - returns all records
  * optional filter parameters: session_id, request, time

  	example:
		localhost:6543:api/session_requests?session_id=b984e2b1-251f-4387-a1ca-7034d80b0274&request=http://localhost:6543/quotes/1&time=2018-05-30 01:24:18.548583

	return format:
	{"response": [
	                 {
					     "session_id": "b984e2b1-251f-4387-a1ca-7034d80b0274",
                         "time": "2018-05-30 22:21:42.548583",
                         "request": "http://localhost:6543/quotes/1"
                      }
                 ]
	}

AUTHOR
======
* Stuart Kuredjian<br>
[sgkur04@gmail.com](sgkur04@gmail.com)<br>
[github.com/dbconfession78](https://www.github.com/dbconfession78)<br>
[linkedin.com/in/stuart-kuredjian](https://www.linkedin.com/in/stuart-kuredjian)<br>
[twitter.com/stueygk](https://twitter.com/stueygk)