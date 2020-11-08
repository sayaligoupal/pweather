# -*- coding: utf-8 -*-
import sys
import os
import requests
import pprint
from logger import *

__author__    = "sayaligoupal"
__copyright__ = "sayaligoupal"
__license__   = "mit"

def main(args):
    """Main entry point allowing external calls
    Args:
      args ([str]): command line parameter list
    """
    _url = "http://api.openweathermap.org/data/2.5/weather"
    _API_SECRET = os.environ.get("SECRET_KEY")
    _log_h = logger.get_logger()

    if not _API_SECRET:
        _log_h.error("can't find API SECRET KEY")
        sys.exit(1)
    if len(args) != 1:
        _log_h.error("only one command line param expected")
        sys.exit(1)
    else:
        if not isinstance(args[0], str):
            _log_h.error("command line argument is not a string")
            sys.exit(2)

    _city = args[0]
    params = dict ( q = _city, appid = _API_SECRET)
    resp = requests.get(url=_url, params=params)
    data = resp.json()

    if data['cod'] != 200:
        _log_h.error(data['message'])
    else:
        print("Max Temp at " + _city + " : " + str(round(data['main']['temp_max'] - 273.15,2)))
        print("Min Temp at " + _city + " : " + str(round(data['main']['temp_min'] - 273.15,2)))
        print("Weather at " + _city + " : " +  data['weather'][0]['main'])

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
