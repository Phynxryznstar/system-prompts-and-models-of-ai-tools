"""Neo4j connection utilities.

Provides a shared driver/session factory for connecting to the Neo4j
graph database using settings from the config package.
"""

from __future__ import annotations

from neo4j import Driver, GraphDatabase, Session

from config.settings import get_settings

_driver: Driver | None = None


def get_driver() -> Driver:
    """Return a lazily-initialized, process-wide Neo4j driver."""
    global _driver
    if _driver is None:
        settings = get_settings()
        _driver = GraphDatabase.driver(
            settings.neo4j_uri,
            auth=(settings.neo4j_username, settings.neo4j_password),
        )
    return _driver


def get_session() -> Session:
    """Return a new Neo4j session bound to the configured database.

    Intended to be used as a context manager::

        with get_session() as session:
            session.run("MATCH (n) RETURN n LIMIT 1")
    """
    settings = get_settings()
    return get_driver().session(database=settings.neo4j_database)


def verify_connectivity() -> None:
    """Raise an exception if the configured Neo4j instance is unreachable."""
    get_driver().verify_connectivity()


def close_driver() -> None:
    """Close the shared driver, if one has been created.

    Should be called on application shutdown to release connections.
    """
    global _driver
    if _driver is not None:
        _driver.close()
        _driver = None
