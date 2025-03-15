from pydantic import BaseModel, Field
from typing import *

class ChatRequest(BaseModel):
    prompt: str = Field(
        default="Code fastapi router"
    )

    context: Optional[str]= Field(
        default="Bạn là một giáo viên lập trình, bạn sẽ trả lời và giải thích cho học sinh của mình những kiến thức về phần mềm, AI.... Giữ câu trả lời của mình ngắn gọn và dễ hiểu "
    )