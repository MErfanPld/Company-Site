from django.shortcuts import render
from rest_framework.generics import *
from home.models import *
from .serializers import *

# Create your views here.

# * =================== Slider English Dashboard ===================


class SlidersEnglishListView(ListAPIView):
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer


class SlidersEnglishCreateView(CreateAPIView):
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer


class SlidersEnglishDetailView(RetrieveAPIView):
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer
    lookup_field = 'id'


class SlidersEnglishUpdateView(UpdateAPIView):
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer
    lookup_field = 'id'


class SlidersEnglishDeleteView(DestroyAPIView):
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer
    lookup_field = 'id'

# * =================== Slider Arabic Dashboard ===================


class SlidersArabicListView(ListAPIView):
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer


class SlidersArabicCreateView(CreateAPIView):
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer


class SlidersArabicDetailView(RetrieveAPIView):
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer
    lookup_field = 'id'


class SlidersArabicUpdateView(UpdateAPIView):
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer
    lookup_field = 'id'


class SlidersArabicDeleteView(DestroyAPIView):
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer
    lookup_field = 'id'

# * =================== AboutUs English Dashboard ===================


class AboutUsEnglishListView(ListAPIView):
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer


class AboutUsEnglishCreateView(CreateAPIView):
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer


class AboutUsEnglishDetailView(RetrieveAPIView):
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer
    lookup_field = 'id'


class AboutUsEnglishUpdateView(UpdateAPIView):
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer
    lookup_field = 'id'


class AboutUsEnglishDeleteView(DestroyAPIView):
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer
    lookup_field = 'id'

# * =================== AboutUs Arabic Dashboard ===================


class AboutUsArabicListView(ListAPIView):
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer


class AboutUsArabicCreateView(CreateAPIView):
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer


class AboutUsArabicDetailView(RetrieveAPIView):
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer
    lookup_field = 'id'


class AboutUsArabicUpdateView(UpdateAPIView):
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer
    lookup_field = 'id'


class AboutUsArabicDeleteView(DestroyAPIView):
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer
    lookup_field = 'id'

# # * =================== ChooseUs English Dashboard ===================


class ChooseUsEnglishListView(ListAPIView):
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer


class ChooseUsEnglishCreateView(CreateAPIView):
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer


class ChooseUsEnglishDetailView(RetrieveAPIView):
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer
    lookup_field = 'id'


class ChooseUsEnglishUpdateView(UpdateAPIView):
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer
    lookup_field = 'id'


class ChooseUsEnglishDeleteView(DestroyAPIView):
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer
    lookup_field = 'id'

# # * =================== ChooseUs Arabic Dashboard ===================


class ChooseUsArabicListView(ListAPIView):
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer


class ChooseUsArabicCreateView(CreateAPIView):
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer


class ChooseUsArabicDetailView(RetrieveAPIView):
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer
    lookup_field = 'id'


class ChooseUsArabicUpdateView(UpdateAPIView):
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer
    lookup_field = 'id'


class ChooseUsArabicDeleteView(DestroyAPIView):
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer
    lookup_field = 'id'

# # * =================== Service English Dashboard ===================


class ServiceEnglishListView(ListAPIView):
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer


class ServiceEnglishCreateView(CreateAPIView):
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer


class ServiceEnglishDetailView(RetrieveAPIView):
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer
    lookup_field = 'id'


class ServiceEnglishUpdateView(UpdateAPIView):
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer
    lookup_field = 'id'


class ServiceEnglishDeleteView(DestroyAPIView):
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer
    lookup_field = 'id'

# # * =================== Service Arabic Dashboard ===================


class ServiceArabicListView(ListAPIView):
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer


class ServiceArabicCreateView(CreateAPIView):
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer


class ServiceArabicDetailView(RetrieveAPIView):
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer
    lookup_field = 'id'


class ServiceArabicUpdateView(UpdateAPIView):
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer
    lookup_field = 'id'


class ServiceArabicDeleteView(DestroyAPIView):
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer
    lookup_field = 'id'

# # * =================== Comments English Dashboard ===================


class CommentsEnglishListView(ListAPIView):
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer


class CommentsEnglishCreateView(CreateAPIView):
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer


class CommentsEnglishDetailView(RetrieveAPIView):
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer
    lookup_field = 'id'


class CommentsEnglishUpdateView(UpdateAPIView):
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer
    lookup_field = 'id'


class CommentsEnglishDeleteView(DestroyAPIView):
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer
    lookup_field = 'id'

# # * =================== Comments Arabic Dashboard ===================


class CommentsArabicListView(ListAPIView):
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer


class CommentsArabicCreateView(CreateAPIView):
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer


class CommentsArabicDetailView(RetrieveAPIView):
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer
    lookup_field = 'id'


class CommentsArabicUpdateView(UpdateAPIView):
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer
    lookup_field = 'id'


class CommentsArabicDeleteView(DestroyAPIView):
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer
    lookup_field = 'id'


# * =================== Suggestions English Dashboard ===================


class SuggestionsEnglishListView(ListAPIView):
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer


class SuggestionsEnglishCreateView(CreateAPIView):
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer


class SuggestionsEnglishDetailView(RetrieveAPIView):
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer
    lookup_field = 'id'


class SuggestionsEnglishUpdateView(UpdateAPIView):
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer
    lookup_field = 'id'


class SuggestionsEnglishDeleteView(DestroyAPIView):
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer
    lookup_field = 'id'

# * =================== Suggestions Arabic Dashboard ===================


class SuggestionsArabicListView(ListAPIView):
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer


class SuggestionsArabicCreateView(CreateAPIView):
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer


class SuggestionsArabicDetailView(RetrieveAPIView):
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer
    lookup_field = 'id'


class SuggestionsArabicUpdateView(UpdateAPIView):
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer
    lookup_field = 'id'


class SuggestionsArabicDeleteView(DestroyAPIView):
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer
    lookup_field = 'id'

# * =================== FAQ English Dashboard ===================


class FAQEnglishListView(ListAPIView):
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer


class FAQEnglishCreateView(CreateAPIView):
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer


class FAQEnglishDetailView(RetrieveAPIView):
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer
    lookup_field = 'id'


class FAQEnglishUpdateView(UpdateAPIView):
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer
    lookup_field = 'id'


class FAQEnglishDeleteView(DestroyAPIView):
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer
    lookup_field = 'id'

# * =================== FAQ Arabic Dashboard ===================


class FAQArabicListView(ListAPIView):
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer


class FAQArabicCreateView(CreateAPIView):
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer


class FAQArabicDetailView(RetrieveAPIView):
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer
    lookup_field = 'id'


class FAQArabicUpdateView(UpdateAPIView):
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer
    lookup_field = 'id'


class FAQArabicDeleteView(DestroyAPIView):
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer
    lookup_field = 'id'


# * =================== News English Dashboard ===================


class NewsEnglishListView(ListAPIView):
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer


class NewsEnglishCreateView(CreateAPIView):
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer


class NewsEnglishDetailView(RetrieveAPIView):
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer
    lookup_field = 'id'


class NewsEnglishUpdateView(UpdateAPIView):
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer
    lookup_field = 'id'


class NewsEnglishDeleteView(DestroyAPIView):
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer
    lookup_field = 'id'


# * =================== News Arabic Dashboard ===================


class NewsArabicListView(ListAPIView):
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer


class NewsArabicCreateView(CreateAPIView):
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer


class NewsArabicDetailView(RetrieveAPIView):
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer
    lookup_field = 'id'


class NewsArabicUpdateView(UpdateAPIView):
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer
    lookup_field = 'id'


class NewsArabicDeleteView(DestroyAPIView):
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer
    lookup_field = 'id'


# * =================== Product English Dashboard ===================


class ProductEnglishListView(ListAPIView):
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer


class ProductEnglishCreateView(CreateAPIView):
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer


class ProductEnglishDetailView(RetrieveAPIView):
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer
    lookup_field = 'id'


class ProductEnglishUpdateView(UpdateAPIView):
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer
    lookup_field = 'id'


class ProductEnglishDeleteView(DestroyAPIView):
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer
    lookup_field = 'id'


# * =================== Product Arabic Dashboard ===================


class ProductArabicListView(ListAPIView):
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer


class ProductArabicCreateView(CreateAPIView):
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer


class ProductArabicDetailView(RetrieveAPIView):
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer
    lookup_field = 'id'


class ProductArabicUpdateView(UpdateAPIView):
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer
    lookup_field = 'id'


class ProductArabicDeleteView(DestroyAPIView):
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer
    lookup_field = 'id'
