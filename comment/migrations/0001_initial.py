# Generated by Django 2.2 on 2020-05-17 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=0)),
                ('text', models.TextField(default=0)),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_comment', to='comment.ItemComment')),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='root_comment', to='comment.ItemComment')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['comment_time'],
            },
        ),
    ]
