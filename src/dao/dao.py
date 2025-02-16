from .base import BaseDAO
from src.models import Item


class ItemDAO(BaseDAO):
    model = Item
