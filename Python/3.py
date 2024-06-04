transactions = {}

class BankAccount:
    def __init__(self, account_number, holder_name, password):
        self.account_number = account_number
        self.holder_name = holder_name
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankTransaction.add_transaction(self.account_number,['Deposited', amount])
            print('Amount Deposited')
        else:
            print('INVALID INPUT! ')
    
    def withdraw(self, amount):
        if 0 < amount and amount <= self.balance:
            self.balance -= amount
            BankTransaction.add_transaction(self.account_number,['Withdrew', amount])
            print('Amount Withdrawn')
        elif amount > self.balance:
            print('INSUFICENT FUNDS! ')
        else:
            print('INVALID INPUT')

    def show_info(self):
        print(f'Account Number: {self.account_number}\nHolder Name: {self.holder_name}\nBalance: {self.balance}')


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number,holder_name,password):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number,holder_name,password)
            BankTransaction.add_account(account_number)
            print('Account created Successfully')
        else:
            print('Account already exists')
    def login(self,account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            print('Login Successful.')
            return account
        else : 
            print('Invalid account number of password!.')


class BankTransaction:
    
    @staticmethod
    def add_account(account_number):
        if account_number not in transactions:
            transactions[account_number] = []
        else:
            print('Account already exists!')

    @staticmethod
    def add_transaction(account_number, Details):
        if account_number in transactions:
            temp = transactions[account_number]
            temp.append(Details)
            transactions[account_number] = temp
        else:
            return 'Account not found in Transaction.'

def main():
    bank_system = BankSystem()

    while True:
        print('-'*10,'Welcome to Banking System', '-'*10)
        print('1. Create Account')
        print('2. Login')
        print('3. Exit')
        choice = input('Enter your choice : ')
        if choice == '1':
            ac_number = int(input('Enter account number : '))
            name = input("Enter holder's name : ")
            password = input("Enter your account's password : ")
            bank_system.create_account(ac_number, name, password)
            
        elif choice == '2':
            ac_number = int(input('Enter your account number : '))
            password = input('Enter your password : ')
            account = bank_system.login(ac_number,password)
            if account:
                while True:
                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Show account info')
                    print('4. Show Transactions')
                    print('5. Exit')
                    action = input('Enter your choice : ')
                    if action == '1':
                        amount = int(input('Enter amount to deposit : '))
                        account.deposit(amount)
                    elif action == '2':
                        amount = int(input('Enter amount to withdraw : '))
                        account.withdraw(amount)
                    elif action == '3':
                        account.show_info()
                    elif action == '4':
                        account_transaction = transactions[ac_number]
                        for i in account_transaction:
                            print(f"{i[0]} : {i[1]}")
                    elif action == '5':
                        break
                    else:
                        print('Invalid input.')
        elif choice == '3':
            print('Thankyou for using Banking System')
            break
        else:
            print('Invalid input')

                        
if __name__ == "__main__":
    main()