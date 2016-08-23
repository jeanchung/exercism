def encode(input):
    """
    Replaces runs (consecutive data elements) with one data value and count.
    """
    result = []
    count = 1
    for i, char in enumerate(input[1:]):
        if char == input[i]:
            count += 1
        else:
            if count > 1:
                result.append(str(count) + input[i])
            else:
                result.append(input[i])
            count = 1
    if count > 1:
        result.append(str(count) + input[-1])
    else:
        result.append(input[-1])
    return "".join(result)


def decode(encrypted_text):
    """
    Decodes text encoded with run-length encoding.
    """
    text = ""
    for char in encrypted_text:
        if not char.isdigit():
            # Add spaces to separate letters from digits
            text += "\n" + char + "\n"
        else:
            text += char
    as_list = text.split("\n")
    
    # Turn string numbers into integers
    for i, item in enumerate(as_list):
        if item.isdigit():
            as_list[i] = int(item)
         
    # Expand each letter to required quantity
    quant = 1
    decrypted_text = ""
    for item in as_list:
        if type(item) != int:
            decrypted_text += (item * quant)
            quant = 1
        else:
            quant = item
    
    return decrypted_text