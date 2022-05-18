from typing import List, Optional, Union

from fastapi.exceptions import HTTPException as FastApiException
from fastapi.responses import UJSONResponse as FastAPIResponse
from fastapi.encoders import jsonable_encoder


class UJSONResponse(FastAPIResponse):
    def __init__(
        self,
        message: str,
        status_code: int,
        data: Optional[Union[dict, List[dict]]] = None
    ):

        data_encoder = jsonable_encoder(data)
        response = dict(
            message=message,
            status_code=status_code,
            data=data_encoder,
        )
        super().__init__(response, status_code)


class HTTPException(FastApiException):

    def __init__(self, message: str, status_code: int, data: dict = None):
        response = dict(
            message=message,
            status_code=status_code,
            data=data,
        )
        super().__init__(status_code, response, headers=None)
