from typing import Optional, Type
from dotenv import load_dotenv

from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool

class AddInput(BaseModel):
    number_1: str = Field(description="First number")
    number_2: str = Field(description="Second number")


class AddTool(BaseTool):
    name = "AddTool"
    description = "Use this tool to add two numbers."
    args_schema : Type[BaseModel] = AddInput
    return_direct : bool = False

    def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        raise NotImplementedError("This tool is not implemented for sync usage.")
              
    async def _arun(self, number_1, number_2, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        return int(number_1) + int(number_2)
        

