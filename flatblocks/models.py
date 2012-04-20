from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from django.contrib.sites.models import Site
from django.conf import settings

from flatblocks.settings import CACHE_PREFIX


class FlatBlock(models.Model):
    """
    Think of a flatblock as a flatpage but for just part of a site. It's
    basically a piece of content with a given name (slug) and an optional
    title (header) which you can, for example, use in a sidebar of a website.
    """
    slug = models.CharField(max_length=255, unique=True,
                verbose_name=_('Slug'),
                help_text=_("A unique name used for reference in the templates"))
    header = models.CharField(blank=True, null=True, max_length=255,
                verbose_name=_('Header'),
                help_text=_("An optional header for this content"))
    content = models.TextField(verbose_name=_('Content'), blank=True, null=True)
    lang_code = models.CharField(verbose_name=_(u"language"), help_text="Language code, if this chunk is translated. Same format as LANGUAGE_CODE setting, e.g. sv-se, or de-de, etc.", blank=True, max_length=5, default=settings.LANGUAGE_CODE)
    site = models.ForeignKey(Site, null=True, blank=True, verbose_name=_('site'))

    def __unicode__(self):
        return u"%s, %s, %s" % (self.slug,str(self.site),self.lang_code)
    
    def save(self, *args, **kwargs):
        super(FlatBlock, self).save(*args, **kwargs)
        # Now also invalidate the cache used in the templatetag
        cache.delete('%s%s_%s_%s' % (CACHE_PREFIX, self.slug, self.lang_code, str(self.site)))

    class Meta:
        verbose_name = _('Flat block')
        verbose_name_plural = _('Flat blocks')
        unique_together = (('slug', 'lang_code', 'site'),)
