def print_block_of_text(text, line_width):
    index = 0
    while index < len(text):
        if (index + 1) % line_width == 0:
            print(text[index])
        else:
            print(text[index], end="")
        index += 1

    return ()




print_block_of_text("The proof of the pudding is in the eating", 8)
print()
print_block_of_text("The proof of the pudding is in the eating", 12)