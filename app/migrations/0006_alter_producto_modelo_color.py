from django.db import models


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_producto_modelo_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_modelo',
            name='color',
            field=models.CharField(max_length=7, blank=True, default='#FF0000'),        ),
    ]