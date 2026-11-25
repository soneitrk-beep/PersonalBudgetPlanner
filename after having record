import json
import os

from set_budget import *
from record_expense import *

BUDGET_FILE = "budgets.json"


def load_budgets():
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Could not read the saved budget, starting with an empty one.")
    return {}


def save_budgets(budgets):
    with open(BUDGET_FILE, "w") as f:
        json.dump(budgets, f, indent=4)


def budget_menu():
    budgets = load_budgets()
    data = load_expenses()
    if len(budgets) > 0:
        print("Your saved budget was loaded.")

    while True:
        print("\n===== Budget Menu =====")
        print("1. Set a budget")
        print("2. Add or change budget")
        print("3. Show budget")
        print("4. Add expense")
        print("5. View all expenses")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if len(budgets) > 0:
                answer = input("This replaces your budget. Continue? (y/n): ")
                if answer != "y" and answer != "Y":
                    continue
            new_budget = set_budget()
            if len(new_budget) > 0:
                budgets = new_budget
                save_budgets(budgets)
            else:
                print("Nothing was saved.")
        elif choice == "2":
            if len(budgets) == 0:
                print("Please set a budget first (option 1).")
            else:
                edit_budget(budgets)
                save_budgets(budgets)
        elif choice == "3":
            if len(budgets) == 0:
                print("Please set a budget first (option 1).")
            else:
                show_budget(budgets)
        elif choice == "4":
            if len(budgets) == 0:
                print("Please set a budget first (option 1).")
            else:
                add_expense(budgets, data)
        elif choice == "5":
            view_records(data)
        elif choice == "6":
            print("Thank you for using this program.")
            return budgets
        else:
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    budgets = budget_menu()
