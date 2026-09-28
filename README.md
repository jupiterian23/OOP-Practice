# 🏦 Python OOP Banking System

> 💻 A Python-based banking system project demonstrating **Object-Oriented Programming (OOP)** concepts through account management, transactions, inheritance, polymorphism, and custom exception handling.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-Object--Oriented%20Programming-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

This project is a simple **Bank Account Management System built with Python**.

It demonstrates how Object-Oriented Programming can be used to model different types of bank accounts and their transactions.

The project supports:

* 🏦 Bank account creation
* 💰 Balance management
* 💵 Deposits
* 💸 Withdrawals
* 🔄 Money transfers
* 🎁 Interest/reward-based accounts
* 💳 Savings accounts with withdrawal fees
* ⚠️ Insufficient-balance exception handling

The main goal of this project is to strengthen practical understanding of **Python OOP concepts** by implementing them in a real-world-inspired banking scenario.

---

# 🎯 Project Objectives

The project focuses on practicing:

* 🧱 Classes and objects
* 🧬 Inheritance
* 🎭 Polymorphism
* 🔄 Method overriding
* ⚠️ Custom exceptions
* 🛡️ Exception handling
* 📦 Python modules
* 🔁 Reusable methods
* 💳 Transaction validation

---

# 🏗️ Class Architecture

The project uses an inheritance hierarchy for different account types:

```text
                    🏦 BankAccount
                         │
                         │ Inheritance
                         ▼
              🎁 InterestRewwardsAcct
                         │
                         │ Inheritance
                         ▼
                   💰 SavingsAcct
```

### 🏦 BankAccount

The base class representing a standard bank account.

It provides functionality for:

* Account creation
* Balance checking
* Depositing money
* Withdrawing money
* Transferring money
* Transaction validation

---

### 🎁 InterestRewwardsAcct

This class inherits from `BankAccount`.

It overrides the deposit method to provide an additional reward calculation when money is deposited.

Example:

```text
Deposit = $100

Reward calculation
$100 × 1.50 = $150

Amount added to balance = $150
```

---

### 💰 SavingsAcct

This class inherits from `InterestRewwardsAcct`.

It adds a withdrawal fee to transactions.

Example:

```text
Withdrawal = $100
Fee = $5

Total deducted = $105
```

This demonstrates **multi-level inheritance**:

```text
BankAccount
     ↓
InterestRewwardsAcct
     ↓
SavingsAcct
```

---

# ⚠️ Custom Exception Handling

The project defines a custom exception:

```python
class BalanceException(Exception):
    pass
```

`BalanceException` is used when an account does not have sufficient funds to complete a transaction.

For example, if an account has `$500` and attempts to withdraw `$1,000`, the transaction is interrupted instead of allowing the balance to become negative.

```text
⚠️ Transaction interrupted
Insufficient account balance
```

---

# 💳 Banking Operations

| Operation             | Description                                            |
| --------------------- | ------------------------------------------------------ |
| 🆕 Account Creation   | Creates a new account with an initial balance          |
| 📊 Get Balance        | Displays the current account balance                   |
| 💵 Deposit            | Adds money to an account                               |
| 💸 Withdraw           | Removes money from an account                          |
| 🔄 Transfer           | Transfers money between accounts                       |
| 🎁 Reward Deposit     | Applies the reward calculation for the rewards account |
| 💰 Savings Withdrawal | Applies a withdrawal fee                               |
| ⚠️ Balance Validation | Prevents transactions exceeding available funds        |

---

# 📁 Project Structure

```text
OOP-Practice/
│
├── 📄 README.md
├── 🐍 bank_account.py
└── 🐍 oop_project.py
```

### `bank_account.py`

Contains the main banking classes:

```text
BalanceException
BankAccount
InterestRewwardsAcct
SavingsAcct
```

This file contains the core banking logic.

---

### `oop_project.py`

This file demonstrates how the banking classes are used.

It creates accounts such as:

```python
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Jim = InterestRewwardsAcct(1000, "Jim")

Blaze = SavingsAcct(1000, "Blaze")
```

It then performs different banking operations such as deposits, withdrawals, and transfers.

---

# ⚙️ Requirements

You only need:

* 🐍 Python 3.x
* 💻 Terminal / Command Prompt
* 📝 A Python-compatible code editor

Check your Python installation:

```bash
python --version
```

Or on Linux:

```bash
python3 --version
```

---

# 🚀 How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/jupiterian23/OOP-Practice.git
```

## 2️⃣ Enter the Project Directory

```bash
cd OOP-Practice
```

## 3️⃣ Run the Project

```bash
python oop_project.py
```

On Linux systems:

```bash
python3 oop_project.py
```

The program will create sample accounts and execute different banking transactions.

---

# 🔄 Example Transaction Flow

```text
        🏦 Create Account
               │
               ▼
        📊 Check Balance
               │
               ▼
          💵 Deposit
               │
               ▼
         💸 Withdraw
               │
               ▼
         🔄 Transfer
               │
               ▼
       🔍 Validate Balance
               │
        ┌──────┴──────┐
        │             │
     Enough        Not Enough
        │             │
        ▼             ▼
   ✅ Complete     ⚠️ Exception
   Transaction     Handling
```

---

# 🧠 OOP Concepts Demonstrated

## 1. 🧱 Classes & Objects

Classes define the structure and behavior of bank accounts.

Objects represent individual accounts.

```python
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")
```

---

## 2. 🧬 Inheritance

Specialized account types inherit functionality from the base class.

```text
BankAccount
     ↓
InterestRewwardsAcct
     ↓
SavingsAcct
```

This allows common banking functionality to be reused.

---

## 3. 🔄 Method Overriding

The child classes modify inherited behavior.

For example:

* `InterestRewwardsAcct` changes the deposit behavior.
* `SavingsAcct` changes the withdrawal behavior by adding a fee.

---

## 4. 🎭 Polymorphism

Different account types can use methods with the same name while implementing different behavior.

For example:

```python
account.deposite(amount)
```

can produce different results depending on the account type.

---

## 5. ⚠️ Custom Exceptions

The project defines its own exception:

```python
BalanceException
```

This provides a specific way to handle insufficient funds.

---

## 6. 🛡️ Exception Handling

Transactions are protected using `try` and `except` blocks.

```python
try:
    ...
except BalanceException as error:
    ...
```

This prevents failed transactions from crashing the program.

---

# 👥 Sample Accounts

The demonstration program uses different account types.

### 👤 Dave

```python
Dave = BankAccount(1000, "Dave")
```

Standard bank account.

### 👤 Sara

```python
Sara = BankAccount(2000, "Sara")
```

Standard bank account.

### 👤 Jim

```python
Jim = InterestRewwardsAcct(1000, "Jim")
```

Rewards-based account.

### 👤 Blaze

```python
Blaze = SavingsAcct(1000, "Blaze")
```

Savings account with a withdrawal fee.

---

# 📚 What I Learned

Building this project helped me practice:

* 🐍 Python programming
* 🧱 Object-Oriented Programming
* 🧬 Inheritance
* 🎭 Polymorphism
* 🔄 Method overriding
* ⚠️ Custom exceptions
* 🛡️ Exception handling
* 📦 Python modules
* 🔁 Reusable code
* 💳 Transaction logic

---

# 🚀 Future Improvements

Possible improvements for a future version include:

* 🔐 PIN-based authentication
* 👥 Customer management
* 🧾 Transaction history
* 💾 Database integration
* 🌐 REST API
* 🖥️ GUI interface
* 🧪 Unit testing
* 🔒 Improved input validation
* 📊 Account statements
* 🐳 Docker support

---

# ⚠️ Disclaimer

This project is created for **educational purposes** to demonstrate Python programming and Object-Oriented Programming concepts.

It is **not intended for real-world financial transactions or production banking systems**.

---

# 👨‍💻 Author

**Shubham Gorule**

🎓 BCA Student
☁️ Aspiring Cloud Engineer

**Skills & Technologies:**

`Python` • `AWS` • `Linux` • `Networking` • `Terraform` • `Docker` • `Kubernetes` • `DevOps`

🐙 GitHub: [jupiterian23](https://github.com/jupiterian23)

---

## ⭐ Project Summary

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

**Built to practice Python OOP through a practical banking application. 🚀**
