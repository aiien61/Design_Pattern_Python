from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, number_of_players: int):
        self.number_of_players = number_of_players
        self.current_player: int = 0

    def run(self):
        self.start()
        while not self.has_winner():
            self.takes_turn()
        
        print(f"Player {self.winning_player} wins!")

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def has_winner(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def takes_turn(self) -> None:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def winning_player(self) -> None:
        raise NotImplementedError
    
class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns: int = 10
        self.turn: int = 1

    def start(self) -> None:
        print(f"Starting a game of chess with {self.number_of_players} players")

    def has_winner(self) -> bool:
        return self.turn == self.max_turns
    
    def takes_turn(self) -> None:
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player
    
    @property
    def winning_player(self) -> int:
        return self.current_player
    
if __name__ == "__main__":
    chess: Game = Chess()
    chess.run()