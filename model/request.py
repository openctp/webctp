from pydantic import BaseModel
from pydantic.dataclasses import dataclass

@dataclass
class WebCTPRequest(BaseModel):

    MessageType: str
    Param: dict[str, any] = {}
    RequestID: int = 0
