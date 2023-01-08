from __future__ import annotations
import math
from collections.abc import Iterable
from typing import Optional


class Tree:
    def __init__(self, height: int) -> None:
        self.height = height
        self.visible: Optional[bool] = None
        self.scenic_score: Optional[int] = None


class VisibilityNotCalculated(Exception):
    pass


class ScenicScoresNotCalculated(Exception):
    pass


class Forest:
    def __init__(self) -> None:
        self._trees: list[list[Tree]] = []
        self._visibility_calculated = False
        self._scenic_scores_calculated = False
        self._visible_trees_count: Optional[int] = None
        self._maximum_scenic_score: Optional[int] = None

    @classmethod
    def from_lines(cls, lines: Iterable[str]) -> Forest:
        tree = cls()
        for line in lines:
            tree._trees.append([])
            for char in line:
                tree._trees[-1].append(Tree(int(char)))
        return tree

    def calculate_visibility(self) -> None:
        if self._visibility_calculated:
            return

        def calculate_visibility_for_iterable(trees: Iterable[Tree]):
            max_height = -1
            for tree in trees:
                if tree.height > max_height:
                    tree.visible = True
                    max_height = tree.height

        for row in self._trees:
            calculate_visibility_for_iterable(row)
            calculate_visibility_for_iterable(reversed(row))
        for column_index in range(len(self._trees[0])):
            calculate_visibility_for_iterable(
                self._trees[row_index][column_index]
                for row_index in range(len(self._trees))
            )
            calculate_visibility_for_iterable(
                self._trees[row_index][column_index]
                for row_index in range(len(self._trees) - 1, -1, -1)
            )

        for row in self._trees:
            for tree in row:
                if tree.visible is None:
                    tree.visible = False
        self._visibility_calculated = True

    def count_visible(self) -> int:
        if not self._visibility_calculated:
            raise VisibilityNotCalculated()
        if self._visible_trees_count is None:
            self._visible_trees_count = sum(tree.visible for row in self._trees for tree in row)  # type: ignore
        return self._visible_trees_count  # type: ignore

    def calculate_scenic_scores(self) -> None:
        if self._scenic_scores_calculated:
            return

        def calculate_visible_trees_from_iterable(trees: Iterable[Tree], height: int) -> int:
            visible_trees = 0
            for tree in trees:
                visible_trees += 1
                if tree.height >= height:
                    break
            return visible_trees

        for i in range(len(self._trees)):
            for j in range(len(self._trees[0])):
                tree = self._trees[i][j]
                tree.scenic_score = math.prod([
                    calculate_visible_trees_from_iterable(
                        (self._trees[i][index] for index in range(j + 1, len(self._trees[0]))), tree.height
                    ),
                    calculate_visible_trees_from_iterable(
                        (self._trees[i][index] for index in range(j - 1, -1, -1)), tree.height
                    ),
                    calculate_visible_trees_from_iterable(
                        (self._trees[index][j] for index in range(i + 1, len(self._trees))), tree.height
                    ),
                    calculate_visible_trees_from_iterable(
                        (self._trees[index][j] for index in range(i - 1, -1, -1)), tree.height
                    ),
                ])
        self._scenic_scores_calculated = True

    def get_maximum_scenic_score(self) -> int:
        if not self._scenic_scores_calculated:
            raise ScenicScoresNotCalculated()
        if self._maximum_scenic_score is None:
            self._maximum_scenic_score = max(tree.scenic_score for row in self._trees for tree in row)  # type: ignore
        return self._maximum_scenic_score  # type: ignore

    def __str__(self) -> str:
        def red(text: str) -> str:
            return f'\u001b[31m{text}\u001b[0m'

        def green(text: str) -> str:
            return f'\u001b[32m{text}\u001b[0m'

        def yellow(text: str) -> str:
            return f'\u001b[33m{text}\u001b[0m'

        rows: list[list[str]] = []
        for row in self._trees:
            rows.append([])
            for tree in row:
                if self._scenic_scores_calculated and tree.scenic_score == self.get_maximum_scenic_score():
                    rows[-1].append(yellow(str(tree.height)))
                elif tree.visible is None:
                    rows[-1].append(red(str(tree.height)))
                elif tree.visible:
                    rows[-1].append(green(str(tree.height)))
                else:
                    rows[-1].append(str(tree.height))

        return '\n'.join(''.join(row) for row in rows)
