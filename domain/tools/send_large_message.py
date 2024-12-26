async def send_large_message(message, text, max_length=4000):
    """
    Відправляє текст, розбиваючи його на частини, якщо він перевищує max_length.
    """
    while text:
        if len(text) > max_length:
            # Знаходимо останній перенос рядка перед лімітом
            split_index = text.rfind("\n", 0, max_length)
            if split_index == -1:  # Якщо переносів немає, ріжемо на max_length
                split_index = max_length
            await message.answer(text[:split_index])
            text = text[split_index:].strip()
        else:
            await message.answer(text)
            break
