class ModelSerializer:
    class Meta:
        model = None
        abstract = True

    def create(self, validated_data):
        instance = None
        # create a new instance with validated data
        return instance

    def update(self, instance, validated_data):
        # update the instance with validated data
        return instance

    def destroy(self, instance):
        # destroy the instance
        return
