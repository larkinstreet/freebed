# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Youth.Status'
        db.add_column(u'youth_youth', 'Status',
                      self.gf('django.db.models.fields.CharField')(default='Pending', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Youth.Status'
        db.delete_column(u'youth_youth', 'Status')


    models = {
        u'youth.youth': {
            'Age_Verification': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'Bed_Gender': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'DOB': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'First_Checkin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Last_Checkin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Youth'},
            'Notes': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'Phone_Number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Rank': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['youth']