#! /usr/bin/env python

import requests


def get_public_ip():
    """
    Fetches the public IP address of the machine.

    Returns:
      str: Public IP address or None if the request fails.
    """
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None


if __name__ == "__main__":
    try:
        public_ip = get_public_ip()
        if public_ip:
            print(f"Public IP address: {public_ip}")
        else:
            print("Failed to retrieve public IP address.")
    except ModuleNotFoundError:
        print("The 'requests' library is not installed. Please install it using:\n")
        print("pip install requests")
