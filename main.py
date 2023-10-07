import functions_framework

import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="PROJECT", location="us-central1")
parameters = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}

@functions_framework.http
def entrypoint(request):
    # Hard-coding an API Key is simple, but not recommend long-term
    if "X-Api-Key" in request.headers and request.headers["X-Api-Key"] == "CHANGE ME":
        request_json = request.get_json(silent=True)
        title = request_json['title']
        model = TextGenerationModel.from_pretrained("text-bison")
        response = model.predict(
            f"""Create a job description for a {title}""",
            **parameters
        )
        return response.text
    else:
        return ("", 401)