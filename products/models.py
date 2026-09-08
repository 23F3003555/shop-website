from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("summer", "☀️ Summer"),
        ("winter", "❄️ Winter"),
        ("diwali", "🪔 Diwali"),
        ("spare_parts", "⚙️ Spare Parts"),
    ]

    SUBCATEGORY_CHOICES = [
        # Summer
        ("cooler", "Cooler"),
        ("cooler_spare_parts", "Cooler Spare Parts"),
        ("honeycomb", "Honeycomb / Cooler Grass"),
        ("table_fan", "Table Fan"),
        ("bullet_fan", "Bullet Fan"),
        ("stand_fan", "Stand Fan"),
        ("ceiling_fan", "Ceiling Fan"),

        # Winter
        ("sun_heater", "Sun Heater"),
        ("quartz_heater", "Quartz Heater"),
        ("immersion_rod", "Immersion Rod"),

        # Diwali
        ("copper_wire_light", "Copper Wire Light"),
        ("temple_light", "Temple Light"),
        ("multi_function_light", "Multi Function Light"),
        ("serial_light", "Serial / Decorative Light"),
        ("warm_white_light", "Warm White Light"),
        ("multi_colour_light", "Multi Colour Light"),

        # Spare Parts
        ("fan_spare_parts", "Fan Spare Parts"),
        ("motor", "Motor"),
        ("pump", "Cooler Pump"),
        ("cooler_motor", "Cooler Motor"),
        ("other_spare_parts", "Other Spare Parts"),
    ]

    name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    subcategory = models.CharField(
        max_length=60,
        choices=SUBCATEGORY_CHOICES
    )

    brand = models.CharField(
        max_length=100,
        blank=True
    )

    model = models.CharField(
        max_length=100,
        blank=True
    )

    size = models.CharField(
        max_length=100,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    features = models.TextField(
        blank=True
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name