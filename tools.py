def calculator(question):
    numbers = []

    for word in question.replace("+", " ").split():
        if word.isdigit():
            numbers.append(int(word))

    if len(numbers) < 2:
        return "Please enter two numbers."

    a = numbers[0]
    b = numbers[1]

    if "plus" in question or "+" in question:
        return a + b

    if "minus" in question or "-" in question:
        return a - b

    if "multiply" in question or "*" in question:
        return a * b

    if "divide" in question or "/" in question:
        if b == 0:
            return "Cannot divide by zero."
        return a / b

    return "Please specify the operation."


def attendance_calculator(question):
    numbers = []

    for word in question.split():
        word = word.strip("%,.")

        if word.isdigit():
            numbers.append(int(word))

    if len(numbers) >= 2:
        attended = numbers[0]
        total = numbers[1]

        if total == 0:
            return "Total classes cannot be zero."

        percentage = (attended / total) * 100

        return f"Attendance Percentage: {percentage:.2f}%"

    return "Example: attendance 45 50"