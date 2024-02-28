from langchain.llms import LLM
from langchain.configs import LLMConfig

# 配置你的 Azure OpenAI API 密钥和其他相关设置
azure_config = LLMConfig(
    llm_service="azure_openai",
    api_key="d9126dbbe5f2446890084390df86f329",  # 替换为你的 Azure OpenAI API 密钥
    # 其他可能的配置项...
)

# 创建一个 LLM 实例，使用 Azure OpenAI 服务
llm = LLM(azure_config)

# 使用 LLM 实例来生成文本
response = llm.invoke("给我一个很土但是听起来好养活的男孩小名", temperature=0)

# 打印生成的文本
print(response)