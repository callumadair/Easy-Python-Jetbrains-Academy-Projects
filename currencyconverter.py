# converts values between different currencies.
import json

import requests


def add_cached_currency(cached_currencies, currency):
    r = requests.get("http://www.floatrates.com/daily/" + currency + ".json")
    cached_currencies[currency] = json.loads(r.text)


cached_currencies = {}
add_cached_currency(cached_currencies, "usd")
add_cached_currency(cached_currencies, "eur")

original_currency = input()
while True:
    target_currency = input().lower()
    if len(target_currency) == 0:
        exit()
    value_in_original = float(input())

    print("Checking the cache...")
    if target_currency in cached_currencies:
        print("Oh! It is in the cache!")

    else:
        print("Sorry, but it is not in the cache!")
        add_cached_currency(cached_currencies, target_currency)

    value_in_exchanged = value_in_original * cached_currencies[target_currency][original_currency]["inverseRate"]
    print("You received " + str(round(value_in_exchanged, 2)) + " " + target_currency.upper() + ".")
