path('view_publishing', views.PublishingListView.as_view(), name='view_publishing.html'),
    path('add_publishing', views.PublishingCreateView.as_view(), name='add_publishing.html'),
    path('edit_publishing/<int:pk>', views.PublishingUpdateView.as_view(), name='edit_publishing.html'),
    path('delete_publishing/<int:pk>', views.PublishingDeleteView.as_view(), name='delete_publishing.html'),