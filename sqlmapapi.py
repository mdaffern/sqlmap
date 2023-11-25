#!/usr/bin/env python

"""
Usage:
  script.py --server [--host=<host>] [--port=<port>] [--adapter=<adapter>] [--username=<username>] [--password=<password>]
  script.py --client [--host=<host>] [--port=<port>] [--username=<username>] [--password=<password>]
  script.py -h | --help

Options:
  -h --help               Show this screen.
  --server                Run as a REST-JSON API server.
  --client                Run as a REST-JSON API client.
  --host=<host>           Host of the REST-JSON API server [default: {RESTAPI_DEFAULT_ADDRESS}].
  --port=<port>           Port of the REST-JSON API server [default: {RESTAPI_DEFAULT_PORT}].
  --adapter=<adapter>     Server (bottle) adapter to use [default: {RESTAPI_DEFAULT_ADAPTER}].
  --username=<username>   Basic authentication username (optional).
  --password=<password>   Basic authentication password (optional).
"""

import sys
import logging
import os
import warnings
from docopt import docopt

# ... [other imports and function definitions]

def main():
    """
    REST-JSON API main function
    """

    # ... [other setup code]

    # Parse command line options using docopt
    args = docopt(__doc__.format(
        RESTAPI_DEFAULT_ADDRESS=RESTAPI_DEFAULT_ADDRESS,
        RESTAPI_DEFAULT_PORT=RESTAPI_DEFAULT_PORT,
        RESTAPI_DEFAULT_ADAPTER=RESTAPI_DEFAULT_ADAPTER
    ))

    # Start the client or the server
    if args['--server']:
        server(args['--host'], int(args['--port']), adapter=args['--adapter'], username=args['--username'], password=args['--password'])
    elif args['--client']:
        client(args['--host'], int(args['--port']), username=args['--username'], password=args['--password'])
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
