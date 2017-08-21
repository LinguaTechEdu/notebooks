"""
Address Book
============

Write a script that:
    - prints your address book
    - finds a specific user and returns it
    - emails information to a given email address
"""
import json


def show_entries():
    """Display a list of contacts."""
    f = open('../data/contacts.json', 'r')
    users_list = json.load(f)

    return users_list


def find_user(name):
    """Return the user."""
    users = show_entries()
    for user in users:
        if name in user['name']:
            return user

