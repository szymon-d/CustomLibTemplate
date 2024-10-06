from typing import Iterable

__all__ = ['command']

def command(command: str, numbers: Iterable) -> str:
    """
    Example methods

    Args:
        command (str): command string
        numbers (Iterable): numbers to be included in command

    Returns:
        str: Concatenated string
    """
    return f"{command}: {','.join([str(i) for i in numbers])}"