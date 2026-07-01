from pydantic import BaseModel
from typing import List, Optional


class Assessment(BaseModel):
    name: str
    url: str
    category: str

    description: str

    test_type: Optional[str] = None

    duration: Optional[str] = None

    remote_testing: Optional[bool] = None

    adaptive: Optional[bool] = None

    skills_measured: List[str] = []

    languages: List[str] = []