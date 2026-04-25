"""
my_project Application routing module.
Version: 0.1.0
"""


# Import your pages here
from fletx.navigation import (
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router

from .pages import CounterPage, NotFoundPage

# Define MyProject routes here
routes = [
    {
        'path': '/',
        'component': CounterPage,
    },
    {
        'path': '/**',
        'component': NotFoundPage,
    },
]

@register_router
class MyProjectRouter(ModuleRouter):
    """my_project Routing Module."""

    name = 'my_project'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []