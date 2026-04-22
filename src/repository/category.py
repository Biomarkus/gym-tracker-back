from sqlalchemy.orm import Query
from src.db.models.category import Category
from factory import session


def get_category_by_id(category_id: int) -> Query:
    return session.query(Category).filter_by(category_id=category_id)


def get_categories_by_name(category_name: str) -> Query:
    return session.query(Category).filter_by(name=category_name)


def create_new_category(category: Category) -> None:
        session.add(category)
        session.commit()

def get_all_categories() -> Query:
    return session.query(Category)