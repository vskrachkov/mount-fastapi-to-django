from starlette import routing

from django_fastapi import fastapi_application, django_application

application = routing.Router(
    [
        routing.Mount("/api", app=fastapi_application.application),
        routing.Mount("/", app=django_application.application),
    ]
)
