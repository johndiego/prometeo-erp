# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Employee'
        db.create_table('hr_employee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partners.Job'], unique=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('hr', ['Employee'])

        # Adding model 'Timesheet'
        db.create_table('hr_timesheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hr.Employee'])),
        ))
        db.send_create_signal('hr', ['Timesheet'])

        # Adding unique constraint on 'Timesheet', fields ['employee', 'date']
        db.create_unique('hr_timesheet', ['employee_id', 'date'])

        # Adding model 'TimesheetEntry'
        db.create_table('hr_timesheetentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timesheet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['hr.Timesheet'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.Task'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('hr', ['TimesheetEntry'])

        # Adding model 'ExpenseVoucher'
        db.create_table('hr_expensevoucher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hr.Employee'])),
        ))
        db.send_create_signal('hr', ['ExpenseVoucher'])

        # Adding model 'ExpenseEntry'
        db.create_table('hr_expenseentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voucher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['hr.ExpenseVoucher'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='TRV', max_length=10)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('hr', ['ExpenseEntry'])

        # Adding model 'LeaveRequest'
        db.create_table('hr_leaverequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hr.Employee'])),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='CSL', max_length=10)),
        ))
        db.send_create_signal('hr', ['LeaveRequest'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Timesheet', fields ['employee', 'date']
        db.delete_unique('hr_timesheet', ['employee_id', 'date'])

        # Deleting model 'Employee'
        db.delete_table('hr_employee')

        # Deleting model 'Timesheet'
        db.delete_table('hr_timesheet')

        # Deleting model 'TimesheetEntry'
        db.delete_table('hr_timesheetentry')

        # Deleting model 'ExpenseVoucher'
        db.delete_table('hr_expensevoucher')

        # Deleting model 'ExpenseEntry'
        db.delete_table('hr_expenseentry')

        # Deleting model 'LeaveRequest'
        db.delete_table('hr_leaverequest')


    models = {
        'addressing.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '3'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'addressing.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '3'})
        },
        'addressing.socialprofile': {
            'Meta': {'object_name': 'SocialProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'default': "'TW'", 'max_length': '5'}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hr.employee': {
            'Meta': {'object_name': 'Employee'},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['partners.Job']", 'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'hr.expenseentry': {
            'Meta': {'ordering': "('voucher', 'date')", 'object_name': 'ExpenseEntry'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'TRV'", 'max_length': '10'}),
            'voucher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['hr.ExpenseVoucher']"})
        },
        'hr.expensevoucher': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'ExpenseVoucher'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Employee']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hr.leaverequest': {
            'Meta': {'ordering': "('start', 'type')", 'object_name': 'LeaveRequest'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Employee']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'CSL'", 'max_length': '10'})
        },
        'hr.timesheet': {
            'Meta': {'ordering': "('-date',)", 'unique_together': "(('employee', 'date'),)", 'object_name': 'Timesheet'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Employee']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hr.timesheetentry': {
            'Meta': {'ordering': "('-timesheet__date', 'start_time')", 'object_name': 'TimesheetEntry'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.Task']", 'null': 'True', 'blank': 'True'}),
            'timesheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['hr.Timesheet']"})
        },
        'notifications.stream': {
            'Meta': {'object_name': 'Stream'},
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linked_streams': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notifications.Stream']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'partners.contact': {
            'Meta': {'object_name': 'Contact'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['addressing.Address']", 'null': 'True', 'blank': 'True'}),
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taxonomy.Category']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_of_contact'", 'null': 'True', 'to': "orm['addressing.Address']"}),
            'main_phone_number': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_of_contact'", 'null': 'True', 'to': "orm['addressing.PhoneNumber']"}),
            'nickname': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_numbers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['addressing.PhoneNumber']", 'null': 'True', 'blank': 'True'}),
            'social_profiles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['addressing.SocialProfile']", 'null': 'True', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stream': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['notifications.Stream']", 'unique': 'True', 'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taxonomy.Tag']", 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'GMT'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'partners.job': {
            'Meta': {'object_name': 'Job'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Contact']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Partner']"}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'EMPLOYEE'", 'max_length': '30'})
        },
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['addressing.Address']", 'null': 'True', 'blank': 'True'}),
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assigned_partners'", 'null': 'True', 'to': "orm['auth.User']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_partners'", 'to': "orm['auth.User']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taxonomy.Category']", 'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['partners.Contact']", 'null': 'True', 'through': "orm['partners.Job']", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dashboard': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['widgets.Region']", 'unique': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_managed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_supplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'lead_status': ('django.db.models.fields.CharField', [], {'default': "'FIRST'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'main_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_of_partner'", 'null': 'True', 'to': "orm['addressing.Address']"}),
            'main_phone_number': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_of_partner'", 'null': 'True', 'to': "orm['addressing.PhoneNumber']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'phone_numbers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['addressing.PhoneNumber']", 'null': 'True', 'blank': 'True'}),
            'social_profiles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['addressing.SocialProfile']", 'null': 'True', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stream': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['notifications.Stream']", 'unique': 'True', 'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taxonomy.Tag']", 'null': 'True', 'blank': 'True'}),
            'terms_of_payment': ('django.db.models.fields.CharField', [], {'default': "'30'", 'max_length': '100'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'GMT'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'taxonomy.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['taxonomy.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taxonomy.tag': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'todo.task': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Task'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taxonomy.Category']", 'null': 'True', 'blank': 'True'}),
            'closed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['taxonomy.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'widgets.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['hr']
