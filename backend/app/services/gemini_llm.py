import google.generativeai as genai
from llama_index.core.llms import CustomLLM, CompletionResponse, LLMMetadata
from app.core.config import settings
from pydantic import Field, PrivateAttr

class GeminiLLM(CustomLLM):
    model_name: str = Field(default="gemini-2.0-flash", exclude=True)
    context_window: int = Field(default=32768, exclude=True)
    num_output: int = Field(default=1024, exclude=True)

    _model = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self._model = genai.GenerativeModel(self.model_name)

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
            is_chat_model=True,
            is_function_calling_model=False,
        )

    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        response = self._model.generate_content(prompt)
        return CompletionResponse(text=response.text.strip())

    def stream_complete(self, prompt: str, **kwargs):
        yield self.complete(prompt)
