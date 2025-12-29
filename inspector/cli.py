#!/usr/bin/env python3

import argparse
import json
from inspector.services import list_services, get_service_status

def cli_main():
    # Initialising the parser 
    parser = argparse.ArgumentParser(description="Ubuntu Service Inspector (usi)")

    # Creating a 'subparser' object
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Defining the 'list' command sub-tool
    list_parser = subparsers.add_parser("list", help="List all services")
    list_parser.add_argument("-f", "--failed", action="store_true", help="Show only failed")
    list_parser.add_argument("-n", "--no-pager", action="store_true", help="Print all output to stdout")

    # Defining the 'status' command sub-tool
    status_parser = subparsers.add_parser("status", help="Check the status of a specific service")
    status_parser.add_argument("service_name", help="Check status of this service")

    # Processing the input
    # If the user provides no command, argparse will print a help message and exit here.
    args = parser.parse_args()
    # The value is now stored inside the 'args' object.

    # if command given by the user is 'list'
    if args.command == 'list':
        data = list_services(failed_only=args.failed)
        print(json.dumps(data[0], indent=2))
    
    # if command given is 'status'
    elif args.command == 'status':
        try:
            data = get_service_status(args.service_name)
            print(data)
        except SystemctlError as e:
            print(f"Error: {e}")


if __name__=="__main__":
    cli_main()

