from dataclasses import dataclass, asdict


@dataclass
class Text:
    contents: str
    rot_type: int
    status: str


class Buffer:
    """List that keep data in run time. Allows also  transfer data to json file"""
    data = []

    @staticmethod
    def show_buffer() -> None:
        print("Currently in buffer:")
        for num, part in enumerate(Buffer.data, start=1):
            print(f"{num}. {part}\n")

    @staticmethod
    def add(value: Text):
        Buffer.data.append(value)

    @staticmethod
    def convert():
        temp = []
        for ele in Buffer.data:
            temp.append(asdict(ele))
        return temp
