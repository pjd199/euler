from pkgutil import get_data


def load_resource(name: str) -> str:
    data = get_data("euler.problems", f"resources/{name}.txt")
    if data:
        return data.decode("utf-8")
    return ""
