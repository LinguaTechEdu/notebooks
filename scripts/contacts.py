"""
By: Kay Hudson

A script to generate a collection of contacts for the Address Book exercise.
"""
import json

from argparse import ArgumentParser
from faker import Factory

parser = ArgumentParser('User Generator',
                        usage='Run this script with the number of users. Defaults to 50',
                        description='Generate fake users.')
parser.add_argument('amount', type=int, nargs='?', default=50)
args = parser.parse_args()

fake = Factory.create('en_US')


def generate(amount=args.amount):
    address_book = []
    if not amount:
        amount = 101
    for n in range(0, amount):
        user = fake.simple_profile()
        address_book.append(user)
    print(str(len(address_book)) + ' users created.')

    return address_book

if __name__ == '__main__':
    f = open('data/contacts.json', 'w')
    json.dump(generate(), f, indent=4)
