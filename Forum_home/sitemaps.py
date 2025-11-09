# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from machina.apps.forum_conversation.models import Topic, Post
from machina.apps.forum.models import Forum


class ForumSitemap(Sitemap):
    """Sitemap für Forum-Kategorien"""
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        # Nur öffentliche, sichtbare Foren
        return Forum.objects.filter(type=Forum.FORUM_POST).order_by('-last_post_on')

    def lastmod(self, obj):
        return obj.last_post_on if obj.last_post_on else obj.updated

    def location(self, obj):
        # Verwende reverse() statt get_absolute_url()
        return reverse('forum:forum', kwargs={'slug': obj.slug, 'pk': obj.pk})


class TopicSitemap(Sitemap):
    """Sitemap für Forum-Threads"""
    changefreq = "daily"
    priority = 0.7

    def items(self):
        # Nur genehmigte, nicht gelöschte Topics
        return Topic.objects.filter(
            approved=True,
            status=Topic.TOPIC_POST
        ).select_related('forum').order_by('-last_post_on')[:5000]

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        # Verwende reverse() mit korrekten Parametern
        return reverse('forum_conversation:topic', kwargs={
            'forum_slug': obj.forum.slug,
            'forum_pk': obj.forum.pk,
            'slug': obj.slug,
            'pk': obj.pk
        })


class RecentPostsSitemap(Sitemap):
    """Sitemap für die neuesten Beiträge"""
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(
            approved=True,
            topic__approved=True
        ).select_related('topic', 'topic__forum').order_by('-created')[:1000]

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        # Link zum Topic (Posts haben meist keine eigene URL)
        return reverse('forum_conversation:topic', kwargs={
            'forum_slug': obj.topic.forum.slug,
            'forum_pk': obj.topic.forum.pk,
            'slug': obj.topic.slug,
            'pk': obj.topic.pk
        })