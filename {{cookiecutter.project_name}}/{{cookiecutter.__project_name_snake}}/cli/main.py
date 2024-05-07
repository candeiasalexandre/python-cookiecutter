import logging
import sys

import typer

app = typer.Typer()

@app.callback()
def send_logs_to_std_out() -> None:
    logger_level = logging.DEBUG

    root = logging.getLogger()
    root.setLevel(logger_level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logger_level)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    root.addHandler(handler)


@app.callback()
def main(logs_to_stdout: bool = False) -> None:
    if logs_to_stdout:
        send_logs_to_std_out()


def entrypoint() -> None:
    # this is a workaround to use as entrypoint when things run inside ipython
    # since if we use sys.exit() it will appear as if there was wan error during execution
    try:
        app()
    except SystemExit as sys_exit:
        if sys_exit.code != 0:
            raise sys_exit


if __name__ == "__main__":
    entrypoint()