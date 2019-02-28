from rest_framework_jwt.serializers  import JSONWebTokenSerializer


class EmailJWTSerializer(JSONWebTokenSerializer):

    @property
    def username_field(self):
        return 'email'