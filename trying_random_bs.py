prompt = """
given the following text message:  "how are you doing?", give percentages for each of the following categories below:
Urgency (does it require immediate attention):
Necessity (does the text sender need something):
Want (does the text sender want something):
Informational (is it just a normal text):
Planning (is something being planned):
Work/school related (self explanatory):
Meat pies at 251 (food):
With those percentages, should a user in mode: "work" (shouldn't be bothered unless important) be notified?

return only a json file with each field and their respective percentages and also yes or no and its confidence"""