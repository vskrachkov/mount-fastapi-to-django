import typer

from django_fastapi.typer_application import application


@application.command()
def runserver(host: str = "localhost", port: int = 8000, debug: bool = True):
    try:
        import uvicorn
    except ImportError:
        typer.echo("Cannot star server, install uvicorn at first", err=True)
        raise typer.Exit(code=1)

    from server import application

    typer.echo("Starting server ...")
    uvicorn.run(application, host=host, port=port, debug=debug)


@application.command()
def hello():
    typer.echo('Hello')


if __name__ == "__main__":
    application()
