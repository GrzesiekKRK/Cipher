import manager
from buffer import Buffer, Text


def main() -> None:
    command = manager.Manager()
    one = Text("For gogh and mog", 47, "Decrypted")
    Buffer.add(one)
    command.run_time()


if __name__ == "__main__":
    main()
