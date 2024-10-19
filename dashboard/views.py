from django.shortcuts import render
from rest_framework.generics import *
from home.models import *
from .serializers import *

# Create your views here.

# * =================== Slider Dashboard ===================


# class SliderListView(ListAPIView):
#     queryset = Sliders.objects.all()
#     serializer_class = SliderSerializer


# class SliderCreateView(CreateAPIView):
#     queryset = Sliders.objects.all()
#     serializer_class = SliderSerializer


# class SliderDetailView(RetrieveAPIView):
#     queryset = Sliders.objects.all()
#     serializer_class = SliderSerializer
#     lookup_field = 'id'


# class SliderUpdateView(UpdateAPIView):
#     queryset = Sliders.objects.all()
#     serializer_class = SliderSerializer
#     lookup_field = 'id'


# class SliderDeleteView(DestroyAPIView):
#     queryset = Sliders.objects.all()
#     serializer_class = SliderSerializer
#     lookup_field = 'id'

# # * =================== AboutUs Dashboard ===================


# class AboutUsListView(ListAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer


# class AboutUsCreateView(CreateAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer


# class AboutUsDetailView(RetrieveAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer
#     lookup_field = 'id'


# class AboutUsUpdateView(UpdateAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer
#     lookup_field = 'id'


# class AboutUsDeleteView(DestroyAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer
#     lookup_field = 'id'

# # * =================== ChooseUs Dashboard ===================


# class ChooseUsListView(ListAPIView):
#     queryset = ChooseUs.objects.all()
#     serializer_class = ChooseUsSerializer


# class ChooseUsCreateView(CreateAPIView):
#     queryset = ChooseUs.objects.all()
#     serializer_class = ChooseUsSerializer


# class ChooseUsDetailView(RetrieveAPIView):
#     queryset = ChooseUs.objects.all()
#     serializer_class = ChooseUsSerializer
#     lookup_field = 'id'


# class ChooseUsUpdateView(UpdateAPIView):
#     queryset = ChooseUs.objects.all()
#     serializer_class = ChooseUsSerializer
#     lookup_field = 'id'


# class ChooseUsDeleteView(DestroyAPIView):
#     queryset = ChooseUs.objects.all()
#     serializer_class = ChooseUsSerializer
#     lookup_field = 'id'

# # * =================== Service Dashboard ===================


# class ServiceListView(ListAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer


# class ServiceCreateView(CreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer


# class ServiceDetailView(RetrieveAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     lookup_field = 'id'


# class ServiceUpdateView(UpdateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     lookup_field = 'id'


# class ServiceDeleteView(DestroyAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     lookup_field = 'id'

# # * =================== Comments Dashboard ===================


# class CommentsListView(ListAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer


# class CommentsCreateView(CreateAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer


# class CommentsDetailView(RetrieveAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer
#     lookup_field = 'id'


# class CommentsUpdateView(UpdateAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer
#     lookup_field = 'id'


# class CommentsDeleteView(DestroyAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer
#     lookup_field = 'id'

# # * =================== Suggestions Dashboard ===================


# class SuggestionsListView(ListAPIView):
#     queryset = Suggestions.objects.all()
#     serializer_class = SuggestionsSerializer


# class SuggestionsCreateView(CreateAPIView):
#     queryset = Suggestions.objects.all()
#     serializer_class = SuggestionsSerializer


# class SuggestionsDetailView(RetrieveAPIView):
#     queryset = Suggestions.objects.all()
#     serializer_class = SuggestionsSerializer
#     lookup_field = 'id'


# class SuggestionsUpdateView(UpdateAPIView):
#     queryset = Suggestions.objects.all()
#     serializer_class = SuggestionsSerializer
#     lookup_field = 'id'


# class SuggestionsDeleteView(DestroyAPIView):
#     queryset = Suggestions.objects.all()
#     serializer_class = SuggestionsSerializer
#     lookup_field = 'id'

# # * =================== FAQ Dashboard ===================


# class FAQListView(ListAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer


# class FAQCreateView(CreateAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer


# class FAQDetailView(RetrieveAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer
#     lookup_field = 'id'


# class FAQUpdateView(UpdateAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer
#     lookup_field = 'id'


# class FAQDeleteView(DestroyAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer
#     lookup_field = 'id'

# # * =================== News Dashboard ===================


# class NewsListView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


# class NewsCreateView(CreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


# class NewsDetailView(RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     lookup_field = 'id'


# class NewsUpdateView(UpdateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     lookup_field = 'id'


# class NewsDeleteView(DestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     lookup_field = 'id'
