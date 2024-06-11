from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List


class ListStrategy(ABC):
    @abstractmethod
    def start(self, buffer: List): pass
    @abstractmethod
    def end(self, buffer: List): pass
    @abstractmethod
    def add_list_item(self, buffer: List, item: str): pass


class MarkdownListStrategy(ListStrategy):
    def start(self, buffer: List): pass
    def end(self, buffer: List): pass
    def add_list_item(self, buffer: List, item: str):
        buffer.append(f" * {item}\n")


class HtmlListStrategy(ListStrategy):
    def start(self, buffer: List):
        buffer.append('<ul>\n')

    def end(self, buffer: List):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer: List, item: str):
        buffer.append(f'  <li>{item}</li>\n')


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items: List[str]):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format: OutputFormat):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
    
    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'bass']

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)
