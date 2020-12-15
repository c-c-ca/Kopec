from typing import TypeVar, List, Callable, Set, Optional, Tuple
from generic_search import Node, Stack, Queue
from maze import MazeLocation, Maze, node_to_path

T = TypeVar('T')

def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Tuple[Optional[Node[T]], int]:
    # frontier is where we've yet to go
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    # explored is where we've been
    explored: Set[T] = {initial}
    # number of states explored so far
    state_count: int = 0

    # keep going while there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        state_count += 1
        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node, state_count
        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None, state_count  # went through everything and never found goal


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Tuple[Optional[Node[T]], int]:
    # frontier is where we've yet to go
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    # explored is where we've been
    explored: Set[T] = {initial}
    # number of states explored so far
    state_count: int = 0

    # keep going while there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        state_count += 1
        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node, state_count
        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None, state_count  # went through everything and never found goal


def evaluate(
    search: Callable[[T, Callable[[T], bool], Callable[[T], List[T]]], Tuple[Optional[Node[T]], int]],
    mazes: List[Maze]) -> float:
    count: int = 0
    for m in mazes:
        solution1: Tuple[Optional[Node[MazeLocation]], int] = search(m.start, m.goal_test, m.successors)
        count += solution1[1]
    return count / len(mazes)


if __name__ == "__main__":
    mazes: List[Maze] = [Maze() for _ in range(100)]
    for search in dfs, bfs:
        print(f"Solution found using {search.__name__} in {evaluate(search, mazes)} states on average.")