import dataclasses
import datetime

COMMIT_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M"


@dataclasses.dataclass
class Commit:
    timestamp: datetime.datetime
    repo: str
    title: str

    def __str__(self) -> str:
        timestamp = self.timestamp.strftime(COMMIT_TIMESTAMP_FORMAT)
        return f"{timestamp} - {self.repo} - {self.title}"
