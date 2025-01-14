from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    """
    exclui o tenant.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('tenant', None)

    def get_queryset_for_tenant(self, model):
        """
        objetos filtrados por tenant.
        """
        user = self.context['request'].user
        return model.objects.filter(tenant=user)