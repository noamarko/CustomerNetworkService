from typing import TypeVar, Generic, Sequence

from fastapi import Query
from pydantic import BaseModel

from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams

T = TypeVar("T")


class Params(BaseModel, AbstractParams):
    page: int = Query(0, ge=0, description="Page number")
    size: int = Query(50, ge=1, le=100, description="Page size")

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.size,
            offset=self.size * self.page,
        )


class CustomPage(AbstractPage[T], Generic[T]):
    __root__: Sequence[T]

    __params_type__ = Params

    @classmethod
    def create(cls, items: Sequence[T], total: int, params: AbstractParams):
        return cls(__root__=items)