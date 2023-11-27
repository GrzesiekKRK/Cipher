import manager
from buffer import Buffer, Text


def main() -> None:
    command = manager.Manager()
    one = Text(
        "If you are smartest person in the room, then you are in the wrong room",
        13,
        "Decrypted",
    )
    three = Text(
        "If you are smartest person in the room, then you are in the wrong room",
        47,
        "Decrypted",
    )
    two = Text(
        "If you are smartest person in the room, then you are in the wrong room",
        3,
        "Decrypted",
    )
    Buffer.add(one)
    Buffer.add(two)
    Buffer.add(three)
    command.run_time()


if __name__ == "__main__":
    main()
