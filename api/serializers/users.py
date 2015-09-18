from rest_framework import serializers


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    # type
    type_of_user = serializers.SerializerMethodField('type_of_user')

    def type_of_user(self, instance):
        '''Get the type of user.'''
        return type(instance).__name__
