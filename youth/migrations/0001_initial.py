# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Youth'
        db.create_table(u'youth_youth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('First_Name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Last_Name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Bed_Gender', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Phone_Number', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('DOB', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Age_Verification', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('Notes', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('First_Checkin', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Last_Checkin', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Rank', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'youth', ['Youth'])


    def backwards(self, orm):
        # Deleting model 'Youth'
        db.delete_table(u'youth_youth')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['youth']