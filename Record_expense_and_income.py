import calendar
import json
import os
from datetime import date

from set_budget import get_amount, money

EXPENSE_FILE = "expenses.json"


# ---------- Saving / loading ----------
def load_expenses():
    today = date.today()
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            data = json.load(f)
        if data.get("year") == today.year and data.get("month") == today.month:
            return data
    return {"year": today.year, "month": today.month, "records": []}


def save_expenses(data):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_day(max_day):
    while True:
        value = input(f"Day of the month 1-{max_day} (blank to go back): ")
        if value == "":
            return None
        try:
            day = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if day >= 1 and day <= max_day:
            return day
        print(f"Day must be between 1 and {max_day}.")


def pick_category(budgets):
    names = list(budgets.keys())
    while True:
        print("\nYour categories:")
        number = 1
        for name in names:
            print(f"{number}. {name}")
            number += 1
        choice = input("Enter a number (blank to go back): ")
        if choice == "":
            return None
        try:
            number = int(choice)
        except ValueError:
            number = 0
        if number >= 1 and number <= len(names):
            return names[number - 1]
        print("Please pick a number from the list.")

def add_expense(budgets, data):
    days_in_month = calendar.monthrange(data["year"], data["month"])[1]

    day = get_day(days_in_month)
    if day is None:
        return
    category = pick_category(budgets)
    if category is None:
        return

    currency = budgets[category]["currency"]
    amount = get_amount(f"Amount spent on {category} in {currency} (blank to go back): ")
    if amount is None:
        return
    note = input("Note (optional): ").strip()

    data["records"].append(
        {"day": day, "category": category, "amount": amount,
         "currency": currency, "note": note}
    )
    save_expenses(data)
    print(f"Saved {money(amount, currency)} for {category} on day {day}.")


def view_records(data):
    if len(data["records"]) == 0:
        print("No expenses recorded yet.")
        return

    print(f"\nExpenses for {calendar.month_name[data['month']]} {data['year']}:")
    days = sorted({r["day"] for r in data["records"]})
    for day in days:
        print(f"Day {day}")
        for r in data["records"]:
            if r["day"] == day:
                note = f" - {r['note']}" if r["note"] else ""

