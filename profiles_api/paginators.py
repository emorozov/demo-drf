from rest_framework import pagination
from rest_framework.response import Response


class TotalPagesCountPaginator(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


class TotalPagesCountPaginatorWith3Items(TotalPagesCountPaginator):
    page_size = 3
