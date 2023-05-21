import pathlib

from .core import _generate_prompt, _call_openai, _ipytohn_nice_string


TEMPLATE = pathlib.Path(__file__).parent / "prompts" / "plot.jinja"


class EmptyObject:

    # NOTE. Just empty object with no methods or attributes.
    #       Since plot is 'side effect' function, we don't have anything to return.
    #       This was created to assign 'code' and 'prompt' attributes.
    #
    #       Don't tell my son. He thinks that I'm a good programmer.

    def _ipython_display_(self):
        pass


def generate(dataframe, user_query):
    prompt = _generate_prompt(
        template=TEMPLATE,
        dataframe=dataframe,
        user_query=user_query
    )

    plot_code = _call_openai(prompt)

    ret = EmptyObject()

    ret.prompt = _ipytohn_nice_string(prompt)
    ret.code = _ipytohn_nice_string(plot_code)

    exec(plot_code)

    return ret
