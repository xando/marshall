import hashlib
import pathlib
import sys

from .core import _generate_prompt, _call_openai, _ipytohn_nice_string

TEMPLATE = pathlib.Path(__file__).parent / "prompts" / "python.jinja"


def generate(user_query):

    function_name = f"function_{hashlib.md5(user_query.encode()).hexdigest()}"
    version = f"{sys.version_info.major}.{sys.version_info.minor}"

    prompt = _generate_prompt(
        template=TEMPLATE,
        version=version,
        function_name=function_name,
        user_query=user_query
    )

    python_code = _call_openai(prompt)

    exec(python_code, globals())

    ret = globals()[function_name]
    ret.prompt = _ipytohn_nice_string(prompt)
    ret.code = _ipytohn_nice_string(python_code)

    return ret
