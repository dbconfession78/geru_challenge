Installation
=============
from the comand line:
- navigate to the download location
- run 'source ./geru_setup'

Use
===
* start server: 'geru_start'
* stop server: 'geru_stop'

In a browser or curl from the command line:
   * localhost:6543/ - returns the landing page
   * localhost:6543/quotes - returns all quotes
   * localhost:6543/quotes/<1-19> - returns a specific quote
   * localhost:6543/quotes/random - returns a random quote

api:
  * all session requests - localhost:6543/api/session_requests
  	return format:
    {
        <session id 1>: [{'time': '<time>', 'request': '<page request>'},
                         {'time': '<time>', 'request': '<page request>'}],

        <session id 2>: [{'time': '<time>', 'request': '<page request>'},
                         {'time': '<time>', 'request': '<page request>'}]
    }

  *  all requests from a specific session id - localhost:6543/api/session_requests?=<session_id>
  	 return format:
     {
        <session id>: [{'time': '<time>', 'request': '<page request>'},
                       {'time': '<time>', 'request': '<page request>'}]
     }
