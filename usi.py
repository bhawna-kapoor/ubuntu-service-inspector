#!/usr/bin/env python3

import argparse
import subprocess
import json

def main():
    # 1. Initialising the parser 
    parser = argparse.ArgumentParser(description="Ubuntu Service Inspector (usi)")

    # 2. Create a 'subparser' object
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 3. Define the 'list' command sub-tool
    list_parser = subparsers.add_parser(
        "list",
        help="List all services"
    )
    list_parser.add_argument("--failed", action="store_true", help="Show only failed")
    list_parser.add_argument("--no-pager", action="store_true", help="Print all output to stdout")

    # 4. Define the 'status' command sub-tool
    status_parser = subparsers.add_parser("status", help="Check the status of a specific service")
    status_parser.add_argument("service_name", help="Check bluetooth of a service")

    # 5. Process the input
    # If the user provides no command, argparse will print a help message and exit here.
    args = parser.parse_args()
    # The value is now stored inside the 'args' object.
    print(f"usi is running: {args.command}")
    user_input = ["systemctl"]

    # if command given by the user is 'list'
    if args.command == 'list':
        user_input = user_input + ['list-units', '--type=service', '--output=json']
        if args.failed:
            user_input.append('--failed')
        if args.no_pager:
            user_input.append('--no-pager')
    
    # if command given is 'status'
    elif args.command == 'status':
        user_input = user_input + ['status', args.service_name]
    # using subprocess.run logic using args object
    result = subprocess.run(
        user_input,
        capture_output=True,
        text=True
        )

    if args.command == 'list':
        services = json.loads(result.stdout)
        print(services[0])
    elif args.command == 'status':
        print(f"status of {args.service_name} is: {result.stdout}")


if __name__=="__main__":
    main()
