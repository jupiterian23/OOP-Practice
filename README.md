# 🏦 Python OOP Banking System

> 💻 A Python-based banking system demonstrating **Object-Oriented Programming (OOP)** concepts such as inheritance, polymorphism, custom exceptions, encapsulation, and transaction handling.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-Object%20Oriented%20Programming-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

This project is a simple **Bank Account Management System built with Python**.

It simulates common banking operations such as:

* 💰 Creating bank accounts
* 📊 Checking account balances
* 💵 Depositing money
* 💸 Withdrawing money
* 🔄 Transferring money between accounts
* 🎁 Interest/reward-based deposits
* 🏦 Savings accounts with withdrawal fees
* ⚠️ Handling insufficient-balance transactions using custom exceptions

The primary purpose of this project is to practice and demonstrate **Python Object-Oriented Programming concepts through a practical application**.

---

# 🎯 Project Objectives

The project was created to practice:

* 🧱 Classes and objects
* 🔐 Encapsulation
* 🧬 Inheritance
* 🔄 Method overriding
* 🎭 Polymorphism
* ⚠️ Custom exceptions
* 🛡️ Exception handling
* 🔁 Reusable methods
* 📦 Modular Python code
* 💻 Practical OOP design

---

# 🏗️ Class Architecture

The project uses a simple inheritance hierarchy:

```text
                    🏦 BankAccount
                         │
                         │ Inheritance
                         ▼
              🎁 InterestRewardsAcct
                         │
                         │ Inheritance
                         ▼
                   💰 SavingsAcct
```

### 🏦 BankAccount

The base class representing a standard bank account.

It provides functionality for:

* Creating an account
* Checking balance
* Depositing money
* Withdrawing money
* Transferring money
* Validating transactions

---

### 🎁 InterestRewwardsAcct

A child class of `BankAccount`.

It overrides the deposit behavior and provides an additional **1.5× reward amount** on deposits.

For example:

```text
Deposit = $100

Reward deposit = $100 × 1.50

Amount added = $150
```

> 📌 Note: The class name `InterestRewwardsAcct` is kept as used in the original project.

---

### 💰 SavingsAcct

A child class of `InterestRewwardsAcct`.

It adds a withdrawal fee to savings-account transactions.

```text
Withdrawal = $100
Fee = $5

Total deducted = $105
```

This class demonstrates **multi-level inheritance**.

---

# ⚠️ Custom Exception Handling

The project defines a custom exception:

```python
class BalanceException(Exception):
    pass
```

This exception is used when an account does not have enough balance to complete a transaction.

Example:

```text
Sorry, account 'Blaze' only has a balance of $...
```

Instead of allowing the program to fail unexpectedly, the exception is caught and an understandable message is displayed.

---

# 💳 Supported Operations

| Operation             | Description                                       |
| --------------------- | ------------------------------------------------- |
| 🆕 Account Creation   | Creates a new bank account                        |
| 📊 Get Balance        | Displays current account balance                  |
| 💵 Deposit            | Adds money to an account                          |
| 💸 Withdrawal         | Removes money from an account                     |
| 🔄 Transfer           | Transfers money between accounts                  |
| 🎁 Reward Deposit     | Adds 1.5× the deposited amount                    |
| 💰 Savings Withdrawal | Withdraws money plus a transaction fee            |
| ⚠️ Balance Validation | Prevents transactions exceeding available balance |

---

# 👥 Example Accounts

The demonstration script creates several account types.

### 👤 Dave

```python
Dave = BankAccount(1000, "Dave")
```

Standard bank account with an initial balance of `$1000`.

---

### 👤 Sara

```python
Sara = BankAccount(2000, "Sara")
```

Standard bank account with an initial balance of `$2000`.

---

### 👤 Jim

```python
Jim = InterestRewwardsAcct(1000, "Jim")
```

Interest/rewards account with an initial balance of `$1000`.

Deposits receive the configured reward behavior.

---

### 👤 Blaze

```python
Blaze = SavingsAcct(1000, "Blaze")
```

Savings account with a `$5` withdrawal fee.

---

# 📁 Project Structure

```text
python-oop-banking-system/
│
├── 📄 bank_account.py
├── 📄 main.py
├── 📄 README.md
└── 📄 .gitignore
```

### `bank_account.py`

Contains:

* `BalanceException`
* `BankAccount`
* `InterestRewwardsAcct`
* `SavingsAcct`

### `main.py`

Contains the example program that creates accounts and performs banking operations.

---

# ⚙️ Requirements

You only need:

* 🐍 Python 3.x
* 💻 Terminal / Command Prompt
* 📝 Any Python-compatible code editor

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

---

# 🚀 How to Run

## 1️⃣ Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

## 2️⃣ Enter the Project Directory

```bash
cd python-oop-banking-system
```

## 3️⃣ Run the Program

```bash
python main.py
```

On some Linux systems:

```bash
python3 main.py
```

---

# 🧪 Example Workflow

The demonstration program performs operations such as:

```text
🏦 Create Dave's account
🏦 Create Sara's account

📊 Check balances

💵 Deposit money into Sara's account

💸 Withdraw money from Dave's account

🔄 Transfer money from Dave to Sara

🎁 Create Jim's rewards account

💵 Deposit money into Jim's account

🔄 Transfer money from Jim to Dave

💰 Create Blaze's savings account

💵 Deposit money into Blaze's account

🔄 Attempt a large transfer from Blaze
```

The final transaction demonstrates the project's **balance validation and exception handling**.

---

# 🧠 OOP Concepts Demonstrated

## 1. 🧱 Classes & Objects

Classes define the structure and behavior of accounts.

Objects represent individual customers/accounts.

```python
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")
```

---

## 2. 🧬 Inheritance

Specialized account types inherit functionality from the base account:

```text
BankAccount
     ↓
InterestRewwardsAcct
     ↓
SavingsAcct
```

This reduces code duplication and allows specialized behavior.

---

## 3. 🔄 Method Overriding

`InterestRewwardsAcct` overrides the `deposite()` method to change how deposits are calculated.

`SavingsAcct` overrides `withdraw()` to include a withdrawal fee.

---

## 4. 🎭 Polymorphism

Different account classes can use methods with the same name while implementing different behaviors.

For example:

```python
account.deposite(amount)
```

can behave differently depending on the account type.

---

## 5. ⚠️ Custom Exceptions

`BalanceException` provides a dedicated exception type for insufficient account balance.

---

## 6. 🛡️ Exception Handling

The project uses:

```python
try:
    ...
except BalanceException:
    ...
```

to safely handle failed transactions.

---

# 🔄 Transaction Flow

```text
             💳 Transaction
                    │
                    ▼
          🔍 Check Available Balance
                    │
             ┌──────┴──────┐
             │             │
          Enough         Not Enough
             │             │
             ▼             ▼
        ✅ Process      ⚠️ Exception
        Transaction     BalanceException
             │
             ▼
       📊 New Balance
```

---

# 📚 What I Learned

By building this project, I practiced:

* 🐍 Python programming
* 🧱 Object-Oriented Programming
* 🧬 Inheritance
* 🎭 Polymorphism
* 🔄 Method overriding
* ⚠️ Custom exceptions
* 🛡️ Error handling
* 📦 Python modules
* 🔁 Reusable class methods
* 💻 Building a practical console application

---

# 🚀 Possible Future Improvements

The current project is intentionally simple and focused on OOP fundamentals.

Future improvements could include:

* 🔐 PIN/password authentication
* 👥 Customer management
* 🧾 Transaction history
* 💾 Database integration
* 🖥️ GUI interface
* 🌐 REST API
* 📊 Account statements
* 🔒 Improved security and validation
* 🧪 Automated unit tests
* 🐳 Docker containerization

---

# ⚠️ Disclaimer

This is an **educational Python project** created to demonstrate programming and OOP concepts.

It is **not intended for handling real financial transactions or production banking systems**.

---

# 👨‍💻 Author

**Shubham Gorule**

🎓 BCA Student
☁️ Aspiring Cloud Engineer
🐍 Python • AWS • Linux • Networking • Terraform • Docker • Kubernetes

🔗 GitHub: **jupiterian23**

---

## ⭐ Project Highlights

```text
🐍 Python
        +
🧱 OOP
        +
🧬 Inheritance
        +
🎭 Polymorphism
        +
⚠️ Exception Handling
        ↓
🏦 Banking System
```

**Built to learn Python OOP through practical implementation. 🚀**
