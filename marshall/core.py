import functools

import jinja2
import openai


OPENAI_MODEL = None
OPENAI_KEY = None


def set_openai_key(key):
    global OPENAI_KEY
    OPENAI_KEY = key


def set_openai_model(model):
    global OPENAI_MODEL
    OPENAI_MODEL = model


def _generate_prompt(*, template, **kwargs):

    template = jinja2.Template(template.read_text())

    return template.render(**kwargs)


@functools.cache
def _call_openai(prompt):
    messages = [{"role": "user", "content": prompt}]

    if OPENAI_MODEL is None:
        raise RuntimeError("OPENAI_MODEL is not set")

    if OPENAI_KEY is None:
        raise RuntimeError("OPENAI_KEY is not set")

    response = openai.ChatCompletion.create(
        api_key=OPENAI_KEY,
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message["content"]


class _ipytohn_nice_string(str):

    def _ipython_display_(self):
        print(self)
