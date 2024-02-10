def is_easy(responses):
  for response in responses:
    if response == 1:
      return "HARD"
  return "EASY"


n = int(input())
inputs = []
for i in range(5):
    prompt = "Enter input {} (1 or 0): ".format(i + 1)
    while True:
        element = input(prompt)
        if element in ("1", "0"):
            inputs.append(int(element)) 
            break
        else:
            print("Invalid input. Please enter 1 or 0.")

is_easy(inputs)
