from django.db import models
from cms.models.pluginmodel import CMSPlugin
# Create your models here.


class SoundcloudPluginInstance(CMSPlugin):
    track_url = models.URLField(verbose_name='URL',
                                help_text='A Soundcloud URL for a track, set, group, user.')
    auto_play = models.BooleanField(verbose_name='Play automatically',
                                    help_text='Whether the widget plays on load.')
    max_width = models.CharField(max_length=20, verbose_name='Maximum Width', blank=True, null=True,
                                 help_text='The maximum width in px or %.')
    max_height = models.CharField(max_length=20, verbose_name='Maximum Width', blank=True, null=True,
                                  help_text='The maximum height in px or %.')
    show_comments = models.BooleanField(verbose_name='Show Comments',
                                        help_text='Whether the player displays timed comments.')
    color = models.CharField(max_length=6, blank=True, null=True, verbose_name='Color',
                             help_text='The primary color of the widget as a hex triplet. (For example: ff0066)')