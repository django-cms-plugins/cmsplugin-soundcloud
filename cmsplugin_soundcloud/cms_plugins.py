from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import SoundcloudPluginInstance
import soundcloud


class SoundcloudPlugin(CMSPluginBase):
    model = SoundcloudPluginInstance
    name = _("Soundcloud")
    render_template = "cms/plugins/soundcloud_plugin.html"

    def render(self, context, instance, placeholder):
        client = soundcloud.Client(client_id='d80704120a6cfa050f5e39423be487ba', use_ssl=False)
        embed_info = client.get('/oembed',
                                url=instance.track_url,
                                auto_play=instance.auto_play,
                                max_width=instance.max_width,
                                max_height=instance.max_height,
                                show_comment=instance.show_comments,
                                color=instance.color)
        context['widget'] = embed_info.html
        return context

plugin_pool.register_plugin(SoundcloudPlugin)