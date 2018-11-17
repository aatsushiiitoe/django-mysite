from django.conf.urls import url
from django.contrib import admin

import manager.views as manager_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^worker_list/', manager_view.WorkerListView.as_view())  # URLとViewを組み合わせる！
]
