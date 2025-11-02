"""Minimal Agent example for AI-Agents repo.

This module defines a simple Agent class with a single method
`act` to demonstrate adding a new file in branch `activework1`.
"""

from typing import Any


class Agent:
    """A minimal agent skeleton.

    Methods
    -------
    act(observation) -> action
        Return an action given an observation (placeholder implementation).
    """

    def __init__(self, name: str = "agent") -> None:
        self.name = name

    def act(self, observation: Any) -> Any:
        """Return a trivial action based on the observation.

        For now this returns the observation unchanged. Replace with
        real logic as needed.
        """
        return observation


__all__ = ["Agent"]
