from typing import List, Dict
from dataclasses import dataclass, asdict


@dataclass
class Text:
    contents: str
    rot_type: int
    status: str


class Buffer:
    """List that keep data in run time. Allows transfer of  data to json file"""

    data: List[Text] = []

    @staticmethod
    def show_buffer() -> None:
        print("Currently in buffer:")
        for num, part in enumerate(Buffer.data, start=1):
            print(f"{num}. {part}\n")

    @staticmethod
    def add(value: Text) -> None:
        Buffer.data.append(value)

    @staticmethod
    def convert() -> list:
        """Convert Text object to dictionary"""
        return [asdict(ele) for ele in Buffer.data]

    @staticmethod
    def load_from_dict(data: Dict[str, List]):
        for element in data["data"]:
            custom = Text(element["contents"], element["rot_type"], element["status"])
            Buffer.add(custom)
