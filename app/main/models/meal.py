class Meal:
    def __init__(self, name, description, created_at ,is_on_diet) -> None:
        self.name = name
        self.description = description,
        self.created_at = created_at,
        self.is_on_diet= is_on_diet

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "is_on_diet": self.is_on_diet

        }
