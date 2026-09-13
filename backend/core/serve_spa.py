from pathlib import Path
import mimetypes

from django.http import FileResponse, HttpResponseNotFound
from django.views import View

FRONTEND_DIST = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"


class SpaFallbackView(View):
    """Serve the built React app (frontend/dist) from the same Django process.

    Real files under dist (assets, images) are served as-is; every other path
    is a client-side route and gets index.html. API/admin/media/static/health
    URLs never reach this view (see core.urls).
    """

    def get(self, request, path=""):
        target = (FRONTEND_DIST / path).resolve()
        try:
            target.relative_to(FRONTEND_DIST.resolve())
        except ValueError:
            return HttpResponseNotFound()

        if path and target.is_file():
            content_type, _ = mimetypes.guess_type(target.name)
            return FileResponse(
                target.open("rb"),
                content_type=content_type or "application/octet-stream",
            )

        index = FRONTEND_DIST / "index.html"
        if not index.is_file():
            return HttpResponseNotFound()
        return FileResponse(index.open("rb"), content_type="text/html")