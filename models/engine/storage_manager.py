#!/usr/bin/python3
from models.engine.file_storage import FileStorage

class StorageManager:
    """Handles the interaction between the BaseModel and the storage system."""

    def __init__(self):
        """Initialize StorageManager with the storage handler (FileStorage)."""
        self._storage = FileStorage()

    def all(self):
        """Return all objects from FileStorage."""
        return self._storage.all()

    def new(self, obj):
        """Add a new object to FileStorage."""
        self._storage.new(obj)

    def save(self, obj=None):
        """Persist the objects to FileStorage."""
        self._storage.save()

    def reload(self):
        """Reload objects from FileStorage."""
        self._storage.reload()
