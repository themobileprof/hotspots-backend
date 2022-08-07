from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point


class Blacklist(models.Model):
    twitter_id = models.CharField(max_length=50)
    category = models.CharField(max_length=10)

    class Meta:
        db_table = 'blacklist'


class EventTags(models.Model):
    tag = models.CharField(max_length=10)
    synonyms = models.CharField(max_length=60)
    desc = models.CharField(max_length=40)

    class Meta:
        db_table = 'event_tags'


class Liveevents(models.Model):
    event_tag = models.ForeignKey(EventTags, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    source = models.CharField(max_length=38)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE)
    noise = models.IntegerField()
    value = models.IntegerField()
    notification_level = models.IntegerField()
    confirmed = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'liveEvents'


class Locations(models.Model):
    location = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    coord = models.PointField(srid=4326)
    state = models.ForeignKey('States', on_delete=models.CASCADE)

    class Meta:
        db_table = 'locations'
        unique_together = (('location', 'state'),)


class NotificationLogs(models.Model):
    user_subscriptions = models.ForeignKey('UserSubscriptions', on_delete=models.CASCADE)
    datesent = models.CharField(db_column='dateSent', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'notification_logs'


class Recommendations(models.Model):
    live_event = models.ForeignKey(Liveevents, models.DO_NOTHING)
    recommendation = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'recommendations'


class States(models.Model):
    state = models.CharField(max_length=15)
    coord = models.PointField(srid=4326)

    class Meta:
        db_table = 'states'


class SubscriptionTypes(models.Model):
    type = models.CharField(max_length=20)

    class Meta:
        db_table = 'subscription_types'


class TweetData(models.Model):
    tweet = models.CharField(max_length=200)
    twitter_user_id = models.CharField(max_length=50)
    tweet_date = models.CharField(max_length=10)
    tweet_time = models.CharField(max_length=10)
    status = models.CharField(max_length=33, blank=True, null=True)
    value = models.IntegerField()
    live_event = models.ForeignKey(Liveevents, models.DO_NOTHING)
    confirmed = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'tweet_data'


class UserSubscriptions(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(SubscriptionTypes, models.DO_NOTHING)
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    notification_level = models.IntegerField()

    class Meta:
        db_table = 'user_subscriptions'
        unique_together = (('user', 'location'),)



class Users(models.Model):
    id = models.OneToOneField(UserSubscriptions, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    twitter_id = models.CharField(max_length=50)
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'users'


class Whitelist(models.Model):
    twitter_id = models.CharField(max_length=50)
    category = models.CharField(max_length=17)

    class Meta:
        db_table = 'whitelist'
