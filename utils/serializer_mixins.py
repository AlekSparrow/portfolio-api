class CreateMixin:
    @property
    def request(self):
        return self._context["request"]

    def create(self, validated_data):
        validated_data.update(
            {
                "created_by": self.request.user,
            }
        )
        return super().create(validated_data)
