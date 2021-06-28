# Generated by Django 3.2.4 on 2021-06-24 12:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for card, max 100chars.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for card. Max Length 255 chars', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image cropped to scale')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More detail here', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Enter a link or select a page'))])))]))], blank=True, null=True),
        ),
    ]
