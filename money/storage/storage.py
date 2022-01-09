from __future__ import annotations
from typing import Iterable, Optional, Protocol

from money.event import EventBase
from money.predicate import Predicate
from money.aggregate import AggregateBase


class Storage(Protocol):
    """A protocol describing the shared capabilities of different storage providers."""

    async def load_events(
        self, query: Optional[Predicate] = None
    ) -> Iterable[EventBase]:
        ...

    async def save_events(self, events: Iterable[EventBase]):
        ...

    async def save_snapshots(self, snaps: Iterable[AggregateBase]):
        ...

    async def load_snapshots(self, query: Predicate = None) -> Iterable[AggregateBase]:
        ...