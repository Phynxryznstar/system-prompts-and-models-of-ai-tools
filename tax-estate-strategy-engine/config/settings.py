"""Application configuration: Neo4j connection settings and API keys.

Values are read from environment variables (populated from a local
`.env` file via `python-dotenv`, or from Replit Secrets at runtime).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime configuration for the strategy engine."""

    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str
    neo4j_database: str = "neo4j"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Load and cache settings from environment variables.

    Raises:
        RuntimeError: If required Neo4j configuration is missing.
    """
    uri = os.environ.get("NEO4J_URI")
    username = os.environ.get("NEO4J_USERNAME")
    password = os.environ.get("NEO4J_PASSWORD")

    if not uri or not username or not password:
        raise RuntimeError(
            "Missing Neo4j configuration. Set NEO4J_URI, NEO4J_USERNAME, "
            "and NEO4J_PASSWORD (e.g. in a .env file or Replit Secrets)."
        )

    return Settings(
        neo4j_uri=uri,
        neo4j_username=username,
        neo4j_password=password,
        neo4j_database=os.environ.get("NEO4J_DATABASE", "neo4j"),
    )
