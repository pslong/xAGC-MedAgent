"""Integration with Baichuan's API."""
import functools
import json
from typing import Callable, Dict, List, Optional, Union

import numpy as np
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)

import outlines

import baichuan_client

__all__ = [
    "BaichuanCompletion",
]


def BaichuanCompletion(
    model_name: str,
) -> Callable:
    """Create a function that will call the Baichuan completion API.

    You should have the `Baichuan` package installed. Available models are listed
    in the `Baichuan documentation <https://platform.openai.com/docs/models/overview>`_.

    Parameters
    ----------
    model_name: str
        The name of the model as listed in the Baichuan documentation.
    Returns
    -------
    A function that will call Baichuan's completion API with the given parameters
    when passed a prompt.

    """
    call_api = call_completion_api
    format_prompt = lambda x: x
    extract_choice = lambda x: x["content"]

    def generate(
        prompt: str,
        *,
        samples=1,
        is_in=None,
    ):

        if is_in is not None:
            return generate_choice(prompt, is_in, samples)
        else:
            return generate_base(prompt, samples)

    @functools.partial(outlines.vectorize, signature="(),(m),(),()->(s)")
    async def generate_base(
        prompt: str, samples: int
    ) -> str:
        responses = await call_api(
            model_name,
            format_prompt(prompt),
        )

        print(responses)
        response_data = json.loads(responses)

        if samples == 1:
            results = np.array([extract_choice(response_data["data"]["messages"][0])])
        else:
            results = np.array(
                [extract_choice(response_data["data"]["messages"][i]) for i in range(samples)]
            )

        return results

    @functools.partial(outlines.vectorize, signature="(),(m),()->(s)")
    async def generate_choice(
        prompt: str, is_in: List[str], samples: int
    ) -> Union[List[str], str]:
        """Generate a sequence that must be one of many options.

        We tokenize every choice, iterate over the token lists, create a mask
        with the current tokens and generate one token. We progressively
        eliminate the choices that don't start with the currently decoded
        sequence.

        """

        decoded_samples = []
        for _ in range(samples):
            decoded: List[str] = []
            for i in range(max([len(word) for word in is_in])):
                response = await call_api(
                    model_name,
                    format_prompt(prompt),
                )
                print(response)
                # 将字符串转换为JSON
                response_data = json.loads(response)

                try:
                    message = response_data["data"]["messages"][0]
                    decoded.append(extract_choice(message))
                except TypeError:
                    print(type(response["data"]["messages"]))
                    print(response["data"]["messages"])

                prompt = prompt + "".join(decoded)

            decoded_samples.append("".join(decoded))

        return np.array(decoded_samples)

    return generate

retry_config = {
    "wait": wait_random_exponential(min=1, max=30),
    "stop": stop_after_attempt(6),
    "retry": retry_if_exception_type(OSError),
}


@retry(**retry_config)
async def call_completion_api(
    model: str,
    prompt: str
):
    response = baichuan_client.doRequest(
        model=model,
        prompt=prompt,
    )

    return response


@retry(**retry_config)
async def call_chat_completion_api(
    model: str,
    messages: List[Dict[str, str]]
):
    response = baichuan_client.doRequest(
        model=model,
        messages=messages,
    )

    return response

