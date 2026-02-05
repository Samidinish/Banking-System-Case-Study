# Banking System – Python OOP Project

## Overview
This project implements a simplified banking system using Python and
Object-Oriented Programming (OOP) principles. The application is executed
from the command line and allows users to interact with customers and
banking services.

The system uses **SQLAlchemy ORM** with a **SQLite database**. The `Loan` and
`CreditCard` entities are mapped by inheriting from the SQLAlchemy
declarative `Base` class, which allows database tables to be created
automatically at runtime.

---

## Design
The system is designed following core OOP concepts:

- Encapsulation
- Composition
- Separation of concerns

The codebase is organized into models, database configuration, and service
layers to improve readability and maintainability.

---

## Entities
The banking system includes the following entities:

- **Customer** – Stores customer personal information
- **Account** – Represents checking or savings accounts
- **Employee** – Represents bank staff members
- **Loan** – Represents customer loans
- **CreditCard** – Represents credit card services

---

## Logging
Logging is implemented using Python’s built-in `logging` module.

- Log messages are printed to the console
- Errors and warnings are written to `logs/app.log`

This helps track application behavior and diagnose issues.

---

## Exception Handling
The application uses Python exception handling to manage invalid operations,
such as:

- Negative deposit amounts
- Insufficient account balances
- Credit limit violations

Errors are handled gracefully without crashing the application.

---

## How to Run the Application

1. Create the database and tables:
```bash
python main.py
