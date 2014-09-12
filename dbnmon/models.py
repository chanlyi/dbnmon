from django.db import models
from django.contrib import admin

# Application Connection Informations.
class MON_APPS_INFO(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	connections_top = models.IntegerField()
	appls_cur_cons = models.IntegerField()
	num_assoc_agent = models.IntegerField()
	agents_top = models.IntegerField()
	cord_agents_top = models.IntegerField()

class MON_APPS_LIST(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	username = models.CharField(max_length=255)
	appl_name = models.CharField(max_length=255)
	appl_handle = models.IntegerField()
	appl_id = models.IntegerField()
	db_name = models.CharField(max_length=255)
	agents_assigned = models.IntegerField()

class MON_APPS_EDUS(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	eduid = models.IntegerField()
	kernel_tid = models.IntegerField()
	edu_name = models.CharField(max_length=255)
	usr_use_cpu = models.IntegerField()
	sys_use_cpu = models.IntegerField()
	appl_handle = models.IntegerField()
	appl_id = models.IntegerField()
	l_anchid = models.IntegerField()
	l_stmtuid = models.IntegerField()
	sql_text = models.CharField(max_length=3000)
	num_exec = models.IntegerField()

class MON_OS_APPS_LIST(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	user_name = models.CharField(max_length=255)
	pid = models.IntegerField()
	cpu = models.IntegerField()
	mem = models.IntegerField()
	run_time = models.IntegerField()
	command = models.CharField(max_length=255)

# Bufferpool informations.
class MON_BP_INFO(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	bpname = models.CharField(max_length=255)
	pages = models.IntegerField()
	pagesize = models.IntegerField()
	data_hit_ratio = models.IntegerField()
	index_hit_ratio = models.IntegerField()
	total_hit_ratio = models.IntegerField()


# Tablespace Informations.
class MON_TS_INFO(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField()
	ts_name = models.CharField(max_length=255)
	ts_type = models.CharField(max_length=255)
	ts_pagesize = models.IntegerField()
	ts_total_pages = models.IntegerField()
	ts_usable_pages = models.IntegerField()
	ts_used_pages = models.IntegerField()
	ts_free_pages = models.IntegerField()
	ts_high_water = models.IntegerField()
	ts_autostorage = models.IntegerField()
	ts_autoresize = models.IntegerField()
	ts_status = models.CharField(max_length=255)

# Lock informations.

# Sort Informations.


#admin.site.register(BlogsPost,BlogPostAdmin)
#admin.site.register(Bufferpool,BufferpoolAdmin)

