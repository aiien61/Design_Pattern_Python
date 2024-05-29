"""Single Responsibility Principle 單一職責原則 (= Separation of Concerns 關注點分離): 
A class should have only one reason to change, meaning it should have only one job or responsibility.
"""

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, position: int):
        if 0 <= position < len(self.entries):
            del self.entries[position]

    def __str__(self):
        return '\n'.join(self.entries)
    
    # The following two methods break the single responsibility principle
    # def save(self, filename: str):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename: str):
    #     file = open(filename, 'r')
    #     return file.read()
    

class PersistenceManager:
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    @staticmethod
    def load_from_file(filename: str):
        with open(filename, 'r') as file:
            contents = file.read()
            journal = Journal()
            for entry in contents.split('\n'):
                journal.add_entry(':'.join(entry.split(': ')[1:]))
            return journal


"""Consider whether or not the following statement makes sense for every method in a class.
The <classname> <method> itself

e.g.
Before the separation of concerns:
class Automobile:
    start()
    stop()
    change_tires()
    drive()
    wash()
    check_oil()
    get_oil()


The Automobile starts itself (o)
The Automobile stops itself (o)
The Automobile changes its tires (x) -> The CarWash washes an automobile itself (o)
The Automobile drives itself (o)
The Automobile washes itself (x)
The Automobile checks oil itself (x)
The Automobile gets oil itself (o)

After the separation of concerns:
class Automobile:
    start()
    stop()
    drive()
    get_oil()

class CarWash:
    wash()

class Mechanic:
    change_tires()
    check_oil()
"""

if __name__ == '__main__':
    journal = Journal()
    journal.add_entry("Monday: A fresh start in a new week.")
    journal.add_entry("Challenge of The Day: Learn Design Patterns.")
    journal.add_entry("Reminder: Recording the progress.")


    print(f'Journal entries: \n{journal}\n')
    
    print('\nDelete the second entry:')
    journal.remove_entry(1)
    print(f'Journal entries: \n{journal}\n')

    '''This operation is weird as it breaks the single responsibility principle
    the Journal instance should not be responsible for persisting its data
    to a file and load a journal from a file.'''

    # print('\nSave journal to a file')
    # journal.save('../data/journal.txt')

    # print('\nLoad journal from a file:')
    # new_journal = journal.load('../data/journal.txt')

    # print(f'New journal entries: \n{new_journal}\n')

    '''This operation sticks to the rule of the single responsibility principle'''
    print('\nSave journal to a file')
    PersistenceManager.save_to_file(journal, '../data/journal.txt')
    
    print('\nLoad journal from a file:')
    new_journal = PersistenceManager.load_from_file('../data/journal.txt')
    print(f'New journal entries: \n{new_journal}\n')
    
