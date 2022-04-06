from typing import TypeVar, Generic, Sequence, List

from fastapi import Query
from pydantic import BaseModel
from pydantic.generics import GenericModel

from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams

T = TypeVar("T")


class Params(BaseModel, AbstractParams):
    size: int = Query(10)
    number: int = Query(0)

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.size,
            offset=self.size * (self.number),
        )


class ParamsResult(BaseModel):
    count: int
    number: int
    size: int


class PageResult(GenericModel, Generic[T]):
    total: int
    items: List[T]
    paging: ParamsResult


class CustomPage(AbstractPage[T], Generic[T]):
    result: Sequence[T]
    __params_type__ = Params

    @classmethod
    def create(cls, items: Sequence[T], total: int, params: AbstractParams):
        # if not isinstance(params, cls.__params_type__):
        #     raise TypeError(f"Params must be {cls.__params_type__}")

        return cls(result = items)
        # return cls(
        #     result=PageResult(
        #         total=total,
        #         items=items,
        #         paging=ParamsResult(
        #             count=total,
        #             number=params.number,
        #             size=params.size,
        #         )
        #     )

        # )
