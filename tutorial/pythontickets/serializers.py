from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.pythontickets.models import Ticket, SEVERITY_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    assigned = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())
    reported = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'assigned', 'reported')

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        """ Update Method for User """
        # Fields allowed to be updated
        whitelisted_keys = ['email', 'username']
        for key in whitelisted_keys:
            instance[key] = validated_data.get(key, instance[key])

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('url', 'id', 'created', 'assignee', 'reporter', 'description',
        'penalty', 'severity', 'is_done', 'done_date')
