from __future__ import annotations
import collections
from collections.abc import Generator
from typing import Optional


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent: Optional[Directory] = None) -> None:
        self.name = name
        self.parent = parent
        self.child_directories: dict[str, Directory] = {}
        self.files: dict[str, File] = {}
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def increase_size(self, amount: int) -> None:
        self._size += amount
        if self.parent is not None:
            self.parent.increase_size(amount)

    def add_file(self, file: File) -> None:
        self.files[file.name] = file
        self.increase_size(file.size)

    def add_directory(self, directory: Directory) -> None:
        self.child_directories[directory.name] = directory


class FileTree:
    def __init__(self) -> None:
        self.root = Directory('root')
        self.pointer = self.root

    def cd(self, name: str) -> None:
        if name == '..':
            if self.pointer.parent is not None:
                self.pointer = self.pointer.parent
        elif name == '/':
            self.pointer = self.root
        else:
            self.pointer = self.pointer.child_directories[name]

    @property
    def size(self) -> int:
        return self.root.size

    def add_directory(self, name: str) -> None:
        self.pointer.add_directory(Directory(name, self.pointer))

    def add_file(self, name: str, size: int) -> None:
        self.pointer.add_file(File(name, size))

    def traverse_all_directories(self) -> Generator[Directory, None, None]:
        stack = collections.deque([self.root])
        while stack:
            current_directory = stack.pop()
            yield current_directory
            for directory in current_directory.child_directories.values():
                stack.append(directory)
