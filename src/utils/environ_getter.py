import os


NO_TOKEN_DEFAULT_MESSAGE = "設定されていない環境変数があります。確認してください。"


def environ_getter(env_name: str, err_msg: str = NO_TOKEN_DEFAULT_MESSAGE):
    try:
        result = os.environ[env_name]
    except KeyError:
        raise RuntimeError(err_msg)

    return result
