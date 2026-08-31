from typing import Optional
from pydantic import BaseModel, ConfigDict


class CropOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    crop_id: int
    crop_name: str
    variety: Optional[str] = None
