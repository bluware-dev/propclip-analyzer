import sys
import typer

app = typer.Typer()


@app.command(help="Start clipboard recorder (daemon)")
def record():
    sys.exit(0)


@app.command(help="Manage captured snippets")
def manage():
    sys.exit(0)


@app.command(help="Process snippets with IA")
def process():
    sys.exit(0)


if __name__ == "__main__":
    app()