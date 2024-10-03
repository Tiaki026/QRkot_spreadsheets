from pydantic import BaseModel


class CompletionDuration(BaseModel):
    days: int
    hours: int
    minutes: int
    seconds: int


class ProjectReport(BaseModel):
    name: str
    completion_duration: CompletionDuration
    description: str
