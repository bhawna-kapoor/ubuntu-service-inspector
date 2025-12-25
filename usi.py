#!/usr/bin/env python3
'''Code using argparse'''
import argparse
import subprocess
import json

def main():
    # 1. Initialising the parser 
    parser = argparse.ArgumentParser(description="Ubuntu Service Inspector (usi)")

    # 2. Add the 'command' argument
    # By setting 'choices', argparse will automatically reject anything except 'list'.
    parser.add_argument(
        "command",
        choices=["list"],
        help="The action to perform (e.g., list)"
    )

    # 3. Process the input
    # If the user provides no command, argparse will print a help message and exit here.
    args = parser.parse_args()
    # The value is now stored inside the 'args' object.
    print(f"usi is running: {args.command}")

    # using subprocess.run logic using args object
    result = subprocess.run(
        [
            "systemctl",
            args.command,
            "--type=service",
            "--all",
            "--no-pager",
            "--no-legend",
            "--output=json"
        ],
        capture_output=True,
        text=True
            )
    services = json.loads(result.stdout)
    print(services[0])
    

'''Code uses sys.argv -> Manual Code'''
# import sys
# import subprocess
# import json

# # print("Arguments passed:", sys.argv)
# def main():
#     print("usi is running")
#     if len(sys.argv) < 2:
#         print("Error: missing command")
#         sys.exit(1)
    
#     command = sys.argv[1]

#     if command != "list":
#         print(f"Unknown command: {command}")
#         sys.exit(1)

#     print("Listing servises....")
#     result = subprocess.run(
#         [
#             "systemctl",
#             "list-units",
#             "--type=service",
#             "--all",
#             "--no-pager",
#             "--no-legend",
#             "--output=json"
#         ],
#         capture_output=True,
#         text=True
#     )
#     services = json.loads(result.stdout)
#     print(services[0])


if __name__=="__main__":
    main()
