class Author:
    all = []
    def __init__(self, name=''):
        self.name = name
        Author.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
        
    def total_royalties(self):
         return sum(contract.royalties for contract in Contract.all if contract.author == self)
    
    
class Book:
    all=[]
    def __init__(self, title='', name=''):
        self.title = title
        self.name = name
        Book.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]    
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
        
        
class Contract:
    all=[]
    def __init__(self,author, book, date='', royalties=0):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
        if self.author not in (Author.all):
           raise Exception(f'{self.author} is not in {Author}')
        elif self.book not in (Book.all):
            raise Exception(f'{self.book} is not in {Book}')
        elif not isinstance(date, str):
            raise Exception(f'{date} is not {str}')
        elif not isinstance(royalties, int):
            raise Exception(f'{royalties} is not {int}')
        
    @classmethod    
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date] 