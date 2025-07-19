from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if review.reviewer != request.user:
            return Response({'detail': 'Only the reviewer can update this.'}, status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        if review.reviewer != request.user:
            return Response({'detail': 'Only the reviewer can delete this.'}, status=403)
        return super().destroy(request, *args, **kwargs)
