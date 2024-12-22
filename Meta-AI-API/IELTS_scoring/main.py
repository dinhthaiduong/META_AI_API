from meta_ai_api import MetaAI
import json

mission = "Help me to grade this IELTS Writting Task 2 Essay."
with open("question.txt", "r") as file:
    question = "Question: " + file.read()
with open("essay.txt", "r") as file:
    student_answer = "Answer: " + file.read()
message_to_chatbot = mission + "\n" + question + "\n" + student_answer

ai = MetaAI()
response = ai.prompt(message=message_to_chatbot)

#num_lines = sum(1 for _ in open("output.txt"))
# with open("output.txt", "a") as f:
#     f.write(f"Answer {num_lines + 1}:")
#     json_string = json.dumps(responsse)
#     f.write(json_string)
with open("AI_response/output.txt", "a") as f:
    if "message" in response:
        answer = response["message"]
        f.write(answer)
    else:
        print("Không tìm thấy câu trả lời.")
    # for key, value in response.items():
    #     f.write(f"\"{key}\": \"{value}\"" + "\n")
    print("Finish!")