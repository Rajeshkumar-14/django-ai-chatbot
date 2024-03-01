from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings

# Initialize the OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def index(request):
    return render(request, "chatbot/index.html")


def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        print(user_message)
        if not user_message.strip():
            return JsonResponse({"message": "Empty message"}, status=400)

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
            )
            chat_response = response.choices[0].message.content.strip()
            return JsonResponse({"message": chat_response})
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid Request Method."}, status=405)
