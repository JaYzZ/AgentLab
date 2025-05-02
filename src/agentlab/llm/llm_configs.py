from agentlab.llm.chat_api import (
    AzureModelArgs,
    OpenAIModelArgs,
    OpenRouterModelArgs,
    SelfHostedModelArgs,
)

default_oss_llms_args = {
    "n_retry_server": 4,
    "temperature": 0.01,
}

CLOSED_SOURCE_APIS = [
    "openai",
    "reka",
    "test",
]

CHAT_MODEL_ARGS_DICT = {
    "openai/gpt-4o": OpenAIModelArgs(
        model_name="gpt-4o",
        max_total_tokens=128_000,
        max_input_tokens=128_000,
        max_new_tokens=4_096,  # I think this model has very small default value if we don't set max_new_tokens
        vision_support=True,
    ),
    "openai/gpt-4o-mini": OpenAIModelArgs(
        model_name="gpt-4o-mini",
        max_total_tokens=128_000,
        max_input_tokens=128_000,
        max_new_tokens=16_384,
        vision_support=True,
    ),
    "openai/o1-mini": OpenAIModelArgs(
        model_name="o1-mini",
        max_total_tokens=128_000,
        max_input_tokens=128_000,
        max_new_tokens=64_000,
        temperature=1e-1,
    ),
    "openai/o3-mini": OpenAIModelArgs(
        model_name="o3-mini",
        max_total_tokens=200_000,
        max_input_tokens=200_000,
        max_new_tokens=100_000,
        vision_support=False,
    ),
    "anthropic/claude-3.5-sonnet": OpenAIModelArgs(
        model_name="claude-3-5-sonnet-latest",
        max_total_tokens=200_000,
        max_input_tokens=200_000,
        max_new_tokens=8_192,
        temperature=1e-1,
        vision_support=True,
    ),
    "anthropic/claude-3.7-sonnet": OpenAIModelArgs(
        model_name="claude-3-7-sonnet-20250219",
        max_total_tokens=200_000,
        max_input_tokens=200_000,
        max_new_tokens=8_192,
        temperature=1e-1,
        vision_support=True,
    ),
    "azure/gpt-4o": AzureModelArgs(
        model_name="gpt-4o",
        deployment_name="gpt-4o",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=16_384,
        vision_support=True,
    ),
    "azure/gpt-4o-mini": AzureModelArgs(
        model_name="gpt-4o-mini",
        deployment_name="gpt-4o-mini",
        max_total_tokens=128_000,
        max_input_tokens=128_000,
        max_new_tokens=16_384,
        vision_support=True,
    ),
    # ---------------- OSS LLMs ----------------#
    "meta-llama/Meta-Llama-3-70B-Instruct": SelfHostedModelArgs(
        model_name="meta-llama/Meta-Llama-3-70B-Instruct",
        max_total_tokens=8_192,
        max_input_tokens=8_192 - 512,
        max_new_tokens=512,
        backend="huggingface",
        **default_oss_llms_args,
    ),
    "meta-llama/Meta-Llama-3-8B-Instruct": SelfHostedModelArgs(
        model_name="meta-llama/Meta-Llama-3-8B-Instruct",
        max_total_tokens=16_384,
        max_input_tokens=16_384 - 512,
        max_new_tokens=512,
        backend="huggingface",
        **default_oss_llms_args,
    ),
    "mistralai/Mixtral-8x22B-Instruct-v0.1": SelfHostedModelArgs(
        model_name="mistralai/Mixtral-8x22B-Instruct-v0.1",
        max_total_tokens=32_000,
        max_input_tokens=30_000,
        max_new_tokens=2_000,
        backend="huggingface",
        **default_oss_llms_args,
    ),
    # ---------------- OPENROUTER ----------------#
    "openrouter/deepseek/deepseek-r1": OpenRouterModelArgs(
        model_name="deepseek/deepseek-r1",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=128_000,
        temperature=1e-1,
    ),
    "openrouter/meta-llama/llama-3.1-405b-instruct": OpenRouterModelArgs(
        model_name="meta-llama/llama-3.1-405b-instruct",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=28_000,
        temperature=1e-1,
    ),
    "openrouter/meta-llama/llama-3.1-70b-instruct": OpenRouterModelArgs(
        model_name="meta-llama/llama-3.1-70b-instruct",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=28_000,
        temperature=1e-1,
    ),
    "openrouter/meta-llama/llama-3-70b-instruct": OpenRouterModelArgs(
        model_name="meta-llama/llama-3-70b-instruct",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=28_000,
        temperature=1e-1,
    ),
    "openrouter/meta-llama/llama-4-maverick": OpenRouterModelArgs(
        model_name="meta-llama/llama-4-maverick",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=28_000,
        temperature=1e-1,
        vision_support=True,
    ),
    "openrouter/meta-llama/llama-3.1-8b-instruct:free": OpenRouterModelArgs(
        model_name="meta-llama/llama-3.1-8b-instruct:free",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=28_000,
        temperature=1e-1,
    ),
    "openrouter/meta-llama/llama-3.1-8b-instruct": OpenRouterModelArgs(
        model_name="meta-llama/llama-3.1-8b-instruct",
        max_total_tokens=128_000,
        max_input_tokens=100_000,
        max_new_tokens=28_000,
        temperature=1e-1,
    ),
    "openrouter/qwen/qwen-2-72b-instruct": OpenRouterModelArgs(
        model_name="qwen/qwen-2-72b-instruct",
        max_total_tokens=32_000,
        max_input_tokens=30_000,
        max_new_tokens=2_000,
        temperature=1e-1,
    ),
}
