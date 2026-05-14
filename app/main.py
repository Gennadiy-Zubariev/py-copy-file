def copy_file(command: str) -> None:
    try:
        command, original_file, copy_file = command.split()
    except ValueError as e:
        print(f"Invalid command format: {e}")
        return

    if command == "cp" and original_file != copy_file:
        try:
            with open(original_file, "r") as original_file, open(
                copy_file, "w"
            ) as copy_file:
                content = original_file.read()
                copy_file.write(content)
        except FileNotFoundError:
            return
