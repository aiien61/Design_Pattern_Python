class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, position: int):
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


if __name__ == '__main__':
    j = Journal()
    j.add_entry('I cried today.')
    j.add_entry('I smiled tonight.')

    print(f'Journal entries: \n{j}\n')

    '''This operation is weird as it breaks the single responsibility principle
    the Journal instance should not be responsible for persisting its data
    to a file and load a journal from a file.'''
    # j.save('data/journal.txt')
    # new_j = j.load('data/journal.txt')
    # print(f'New journal entries: \n{new_j}\n')

    '''This operation stick to the rule of the single responsibility principle'''
    p = PersistenceManager()
    p.save_to_file(j, 'data/journal.txt')
    
    # verify
    with open('data/journal.txt', 'r') as file:
        print(file.read())
