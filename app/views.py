# -------------------------------------------------------------------- URL CONFIGURATION
import pathlib
from django.http.response import HttpResponse

def graphiql(request):
    """Trivial view to serve the `graphiql.html` file."""
    del request
    graphiql_filepath = pathlib.Path(__file__).absolute().parent / "graphiql.html"
    with open(graphiql_filepath) as f:
        return HttpResponse(f.read())