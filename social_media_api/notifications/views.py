from django.shortcuts import render
# notifications/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Notification.objects.select_related('recipient', 'actor').filter(recipient=self.request.user)
        unread = self.request.query_params.get('unread')
        if unread == 'true':
            qs = qs.filter(is_read=False)
        return qs

class NotificationMarkReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Notification.objects.get(pk=self.kwargs['pk'], recipient=self.request.user)

    def patch(self, request, *args, **kwargs):
        notif = self.get_object()
        notif.is_read = True
        notif.save(update_fields=['is_read'])
        return Response({'detail': 'Notification marked as read.'}, status=status.HTTP_200_OK)

class NotificationMarkAllReadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        count = Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return Response({'detail': f'{count} notifications marked as read.'}, status=status.HTTP_200_OK)