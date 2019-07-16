# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-08 11:58


from __future__ import absolute_import, print_function, unicode_literals

from django.db import migrations
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0015_1_add_fk_to_document_id'),
        ('review', '0010_populate_review_assignments'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrequest',
            name='doc2',
            field=ietf.utils.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewrequest_set', to='doc.Document', to_field=b'id'),
        ),
        migrations.AddField(
            model_name='reviewwish',
            name='doc2',
            field=ietf.utils.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doc.Document', to_field=b'id'),
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='unused_review2',
            field=ietf.utils.models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc.Document', to_field='id'),
        ),
        migrations.AddField(
            model_name='reviewassignment',
            name='review2',
            field=ietf.utils.models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc.Document', to_field='id'),
        ),
        migrations.AlterField(
            model_name='reviewrequest',
            name='doc',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_revreq', to='doc.Document', to_field=b'name'),
        ),
        migrations.AlterField(
            model_name='reviewwish',
            name='doc',
            field=ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_revwish', to='doc.Document', to_field=b'name'),
        ),
        migrations.AlterField(
            model_name='reviewrequest',
            name='unused_review',
            field=ietf.utils.models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_unused_review', to='doc.Document', to_field=b'name'),
        ),
        migrations.AlterField(
            model_name='reviewassignment',
            name='review',
            field=ietf.utils.models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_reviewassignment', to='doc.Document', to_field=b'name'),
        ),
    ]
