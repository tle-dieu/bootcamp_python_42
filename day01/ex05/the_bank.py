class Account:
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.ide = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def get_account(self, acc):
        if isinstance(acc, int):
            acc = next((x for x in self.account if x.ide == acc), None)
        elif isinstance(acc, str):
            acc = next((x for x in self.account if x.name == acc), None)
        else:
            return False
        if (not acc or not isinstance(acc, Account)):
            return False
        if (any(i not in acc.__dict__ for i in ('value', 'ide', 'name'))
                or not len(acc.__dict__) % 2
                or not any(s.startswith('addr') for s in acc.__dict__)
                or not any(s.startswith('zip') for s in acc.__dict__)
                or any(s.startswith('b') for s in acc.__dict__)):
            return False
        return acc

    def transfer(self, origin, dest, amount):
        origin = self.get_account(origin)
        dest = self.get_account(dest)
        if not dest or not origin or amount > origin.value or amount < 0:
            return False
        origin.transfer(-amount)
        dest.transfer(amount)
        return True

    def fix_account(self, acc):
        if isinstance(acc, int):
            acc = next((x for x in self.account if x.ide == acc), None)
        elif isinstance(acc, str):
            acc = next((x for x in self.account if x.name == acc), None)
        else:
            return False
        if (not acc or not isinstance(acc, Account)):
            return False
        if 'value' not in acc.__dict__:
            acc.value = 0
        if 'name' not in acc.__dict__:
            acc.name = 'fix_name'
        if 'ide' not in acc.__dict__:
            acc.name = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not any(s.startswith('addr') for s in acc.__dict__):
            acc.addr_fix = True
        if not any(s.startswith('zip') for s in acc.__dict__):
            acc.zip_fix = True
        for i in list(acc.__dict__):
            if i.startswith('b'):
                delattr(acc, i)
        if not len(acc.__dict__) % 2:
            if 'fix' in acc.__dict__:
                del acc.fix
            else:
                acc.__dict__.fix = True
        return True


def main():
    acc_thomas = Account("Thomas", value=1000, my=1, ok=1, bank=True)
    acc_thomas.transfer(10000)
    acc_jacques = Account("Jacques", value=0, zip=None, addr=None)
    acc_jacques.transfer(100)
    bank = Bank()
    bank.add(acc_jacques)
    bank.add(acc_thomas)
    print(acc_jacques.__dict__)
    print(acc_thomas.__dict__)
    print(bank.transfer("Thomas", "Jacques", 5000))
    print("fix account:", bank.fix_account("Thomas"))
    print("fix account:", bank.fix_account("Jacques"))
    print(acc_jacques.__dict__)
    print(acc_thomas.__dict__)
    print(bank.transfer("Thomas", "Jacques", 5000))
    print(acc_jacques.__dict__)
    print(acc_thomas.__dict__)


if __name__ == "__main__":
    main()
