# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FlatBlock.lang_code'
        db.add_column('flatblocks_flatblock', 'lang_code',
                      self.gf('django.db.models.fields.CharField')(default='en-us', max_length=5, blank=True),
                      keep_default=False)

        # Adding field 'FlatBlock.site'
        db.add_column('flatblocks_flatblock', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'FlatBlock', fields ['lang_code', 'slug', 'site']
        db.create_unique('flatblocks_flatblock', ['lang_code', 'slug', 'site_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'FlatBlock', fields ['lang_code', 'slug', 'site']
        db.delete_unique('flatblocks_flatblock', ['lang_code', 'slug', 'site_id'])

        # Deleting field 'FlatBlock.lang_code'
        db.delete_column('flatblocks_flatblock', 'lang_code')

        # Deleting field 'FlatBlock.site'
        db.delete_column('flatblocks_flatblock', 'site_id')

    models = {
        'flatblocks.flatblock': {
            'Meta': {'unique_together': "(('slug', 'lang_code', 'site'),)", 'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'default': "'en-us'", 'max_length': '5', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatblocks']