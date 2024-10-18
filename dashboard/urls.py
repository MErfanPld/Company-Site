from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    # =============== Slider ===============
    path("sliders/", views.SliderListView.as_view(),
         name="slider_dashboard_list"),
    path("sliders/create/", views.SliderCreateView.as_view(),
         name="slider_dashboard_create"),
    path("sliders/<int:id>/", views.SliderDetailView.as_view(),
         name="slider_dashboard_detail"),
    path("sliders/<int:id>/update/", views.SliderUpdateView.as_view(),
         name="slider_dashboard_update"),
    path("sliders/<int:id>/delete/", views.SliderDeleteView.as_view(),
         name="slider_dashboard_delete"),

    # =============== AboutUs ===============
    path("about_us/", views.AboutUsListView.as_view(),
         name="about_us_dashboard_list"),
    path("about_us/create/", views.AboutUsCreateView.as_view(),
         name="about_us_dashboard_create"),
    path("about_us/<int:id>/", views.AboutUsDetailView.as_view(),
         name="about_us_dashboard_detail"),
    path("about_us/<int:id>/update/", views.AboutUsUpdateView.as_view(),
         name="about_us_dashboard_update"),
    path("about_us/<int:id>/delete/", views.AboutUsDeleteView.as_view(),
         name="about_us_dashboard_delete"),

    # =============== ChooseUs ===============
    path("choose_us/", views.ChooseUsListView.as_view(),
         name="choose_us_dashboard_list"),
    path("choose_us/create/", views.ChooseUsCreateView.as_view(),
         name="choose_us_dashboard_create"),
    path("choose_us/<int:id>/", views.ChooseUsDetailView.as_view(),
         name="choose_us_dashboard_detail"),
    path("choose_us/<int:id>/update/", views.ChooseUsUpdateView.as_view(),
         name="choose_us_dashboard_update"),
    path("choose_us/<int:id>/delete/", views.ChooseUsDeleteView.as_view(),
         name="choose_us_dashboard_delete"),

    # =============== Service ===============
    path("service/", views.ServiceListView.as_view(),
         name="service_dashboard_list"),
    path("service/create/", views.ServiceCreateView.as_view(),
         name="service_dashboard_create"),
    path("service/<int:id>/", views.ServiceDetailView.as_view(),
         name="service_dashboard_detail"),
    path("service/<int:id>/update/", views.ServiceUpdateView.as_view(),
         name="service_dashboard_update"),
    path("service/<int:id>/delete/", views.ServiceDeleteView.as_view(),
         name="service_dashboard_delete"),

    # =============== Comments ===============
    path("comments/", views.CommentsListView.as_view(),
         name="comments_dashboard_list"),
    path("comments/create/", views.CommentsCreateView.as_view(),
         name="comments_dashboard_create"),
    path("comments/<int:id>/", views.CommentsDetailView.as_view(),
         name="comments_dashboard_detail"),
    path("comments/<int:id>/update/", views.CommentsUpdateView.as_view(),
         name="comments_dashboard_update"),
    path("comments/<int:id>/delete/", views.CommentsDeleteView.as_view(),
         name="comments_dashboard_delete"),

    # =============== Suggestions ===============
    path("suggestions/", views.SuggestionsListView.as_view(),
         name="suggestions_dashboard_list"),
    path("suggestions/create/", views.SuggestionsCreateView.as_view(),
         name="suggestions_dashboard_create"),
    path("suggestions/<int:id>/", views.SuggestionsDetailView.as_view(),
         name="suggestions_dashboard_detail"),
    path("suggestions/<int:id>/update/", views.SuggestionsUpdateView.as_view(),
         name="suggestions_dashboard_update"),
    path("suggestions/<int:id>/delete/", views.SuggestionsDeleteView.as_view(),
         name="suggestions_dashboard_delete"),

    # =============== FAQ ===============
    path("faq/", views.FAQListView.as_view(),
         name="faq_dashboard_list"),
    path("faq/create/", views.FAQCreateView.as_view(),
         name="faq_dashboard_create"),
    path("faq/<int:id>/", views.FAQDetailView.as_view(),
         name="faq_dashboard_detail"),
    path("faq/<int:id>/update/", views.FAQUpdateView.as_view(),
         name="faq_dashboard_update"),
    path("faq/<int:id>/delete/", views.FAQDeleteView.as_view(),
         name="faq_dashboard_delete"),

    # =============== News ===============
    path("news/", views.NewsListView.as_view(),
         name="news_dashboard_list"),
    path("news/create/", views.NewsCreateView.as_view(),
         name="news_dashboard_create"),
    path("news/<int:id>/", views.NewsDetailView.as_view(),
         name="news_dashboard_detail"),
    path("news/<int:id>/update/", views.NewsUpdateView.as_view(),
         name="news_dashboard_update"),
    path("news/<int:id>/delete/", views.NewsDeleteView.as_view(),
         name="news_dashboard_delete"),
]
