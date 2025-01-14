from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    """
    exclui o tenant.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('tenant', None)
