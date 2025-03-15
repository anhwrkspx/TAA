from langchain_ollama import OllamaLLM 
from langchain_ollama.llms import BaseLLM 
from langchain.chains.llm import LLMChain 
from langchain.chains.sql_database.query import create_sql_query_chain 
from langchain_core.prompts.prompt import PromptTemplate 
from langchain_community.tools import QuerySQLDataBaseTool 
from langchain_community.utilities.sql_database import SQLDatabase 
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser  
from langchain_core.runnables import RunnablePassthrough 
from operator import itemgetter 
from langchain_community.cache import InMemoryCache
from langchain_core.globals import set_llm_cache