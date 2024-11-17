from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *

from home.models import *
from .serializers import *

# Create your views here.

# * =================== Slider English Dashboard ===================


class SlidersEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer


class SlidersEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer


class SlidersEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer
    lookup_field = 'id'


class SlidersEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer
    lookup_field = 'id'


class SlidersEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersEnglish.objects.all()
    serializer_class = SliderEnglishSerializer
    lookup_field = 'id'

# * =================== Slider Arabic Dashboard ===================


class SlidersArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer


class SlidersArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer


class SlidersArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer
    lookup_field = 'id'


class SlidersArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer
    lookup_field = 'id'


class SlidersArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SlidersArabic.objects.all()
    serializer_class = SliderArabicSerializer
    lookup_field = 'id'

# * =================== AboutUs English Dashboard ===================


class AboutUsEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer


class AboutUsEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer


class AboutUsEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer
    lookup_field = 'id'


class AboutUsEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer
    lookup_field = 'id'


class AboutUsEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer
    lookup_field = 'id'

# * =================== AboutUs Arabic Dashboard ===================


class AboutUsArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer


class AboutUsArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer


class AboutUsArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer
    lookup_field = 'id'


class AboutUsArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer
    lookup_field = 'id'


class AboutUsArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer
    lookup_field = 'id'

# # * =================== ChooseUs English Dashboard ===================


class ChooseUsEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer


class ChooseUsEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer


class ChooseUsEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer
    lookup_field = 'id'


class ChooseUsEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer
    lookup_field = 'id'


class ChooseUsEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer
    lookup_field = 'id'

# # * =================== ChooseUs Arabic Dashboard ===================


class ChooseUsArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer


class ChooseUsArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer


class ChooseUsArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer
    lookup_field = 'id'


class ChooseUsArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer
    lookup_field = 'id'


class ChooseUsArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer
    lookup_field = 'id'

# # * =================== Service English Dashboard ===================


class ServiceEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer


class ServiceEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer


class ServiceEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer
    lookup_field = 'id'


class ServiceEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer
    lookup_field = 'id'


class ServiceEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceEnglish.objects.all()
    serializer_class = ServiceEnglishSerializer
    lookup_field = 'id'

# # * =================== Service Arabic Dashboard ===================


class ServiceArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer


class ServiceArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer


class ServiceArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer
    lookup_field = 'id'


class ServiceArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer
    lookup_field = 'id'


class ServiceArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceArabic.objects.all()
    serializer_class = ServiceArabicSerializer
    lookup_field = 'id'

# # * =================== Comments English Dashboard ===================


class CommentsEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer


class CommentsEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer


class CommentsEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer
    lookup_field = 'id'


class CommentsEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer
    lookup_field = 'id'


class CommentsEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsEnglish.objects.all()
    serializer_class = CommentsEnglishSerializer
    lookup_field = 'id'

# # * =================== Comments Arabic Dashboard ===================


class CommentsArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer


class CommentsArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer


class CommentsArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer
    lookup_field = 'id'


class CommentsArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer
    lookup_field = 'id'


class CommentsArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentsArabic.objects.all()
    serializer_class = CommentsArabicSerializer
    lookup_field = 'id'


# * =================== Suggestions English Dashboard ===================


class SuggestionsEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer


class SuggestionsEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer


class SuggestionsEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer
    lookup_field = 'id'


class SuggestionsEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer
    lookup_field = 'id'


class SuggestionsEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsEnglish.objects.all()
    serializer_class = SuggestionsEnglishSerializer
    lookup_field = 'id'

# * =================== Suggestions Arabic Dashboard ===================


class SuggestionsArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer


class SuggestionsArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer


class SuggestionsArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer
    lookup_field = 'id'


class SuggestionsArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer
    lookup_field = 'id'


class SuggestionsArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SuggestionsArabic.objects.all()
    serializer_class = SuggestionsArabicSerializer
    lookup_field = 'id'

# * =================== FAQ English Dashboard ===================


class FAQEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer


class FAQEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer


class FAQEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer
    lookup_field = 'id'


class FAQEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer
    lookup_field = 'id'


class FAQEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQEnglish.objects.all()
    serializer_class = FAQEnglishSerializer
    lookup_field = 'id'

# * =================== FAQ Arabic Dashboard ===================


class FAQArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer


class FAQArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer


class FAQArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer
    lookup_field = 'id'


class FAQArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer
    lookup_field = 'id'


class FAQArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FAQArabic.objects.all()
    serializer_class = FAQArabicSerializer
    lookup_field = 'id'


# * =================== News English Dashboard ===================


class NewsEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer


class NewsEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer


class NewsEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer
    lookup_field = 'id'


class NewsEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer
    lookup_field = 'id'


class NewsEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEnglish.objects.all()
    serializer_class = NewsEnglishSerializer
    lookup_field = 'id'


# * =================== News Arabic Dashboard ===================


class NewsArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer


class NewsArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer


class NewsArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer
    lookup_field = 'id'


class NewsArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer
    lookup_field = 'id'


class NewsArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsArabic.objects.all()
    serializer_class = NewsArabicSerializer
    lookup_field = 'id'


# * =================== Product English Dashboard ===================


class ProductEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer


class ProductEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer


class ProductEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer
    lookup_field = 'id'


class ProductEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer
    lookup_field = 'id'


class ProductEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductEnglish.objects.all()
    serializer_class = ProductEnglishSerializer
    lookup_field = 'id'


# * =================== Product Arabic Dashboard ===================


class ProductArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer


class ProductArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer


class ProductArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer
    lookup_field = 'id'


class ProductArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer
    lookup_field = 'id'


class ProductArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductArabic.objects.all()
    serializer_class = ProductArabicSerializer
    lookup_field = 'id'



# * =================== About Sliders English Dashboard ===================


class AboutSlidersEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersEnglish.objects.all()
    serializer_class = AboutSlidersEnglishSerializer


class AboutSlidersEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersEnglish.objects.all()
    serializer_class = AboutSlidersEnglishSerializer


class AboutSlidersEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersEnglish.objects.all()
    serializer_class = AboutSlidersEnglishSerializer
    lookup_field = 'id'


class AboutSlidersEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersEnglish.objects.all()
    serializer_class = AboutSlidersEnglishSerializer
    lookup_field = 'id'


class AboutSlidersEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersEnglish.objects.all()
    serializer_class = AboutSlidersEnglishSerializer
    lookup_field = 'id'


# * =================== About Sliders Arabic Dashboard ===================


class AboutSlidersArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersArabic.objects.all()
    serializer_class = AboutSlidersArabicSerializer


class AboutSlidersArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersArabic.objects.all()
    serializer_class = AboutSlidersArabicSerializer


class AboutSlidersArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersArabic.objects.all()
    serializer_class = AboutSlidersArabicSerializer
    lookup_field = 'id'


class AboutSlidersArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersArabic.objects.all()
    serializer_class = AboutSlidersArabicSerializer
    lookup_field = 'id'


class AboutSlidersArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutSlidersArabic.objects.all()
    serializer_class = AboutSlidersArabicSerializer
    lookup_field = 'id'


# * =================== Achievement English Dashboard ===================


class AchievementEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementEnglish.objects.all()
    serializer_class = AchievementEnglishSerializer


class AchievementEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementEnglish.objects.all()
    serializer_class = AchievementEnglishSerializer


class AchievementEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementEnglish.objects.all()
    serializer_class = AchievementEnglishSerializer
    lookup_field = 'id'


class AchievementEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementEnglish.objects.all()
    serializer_class = AchievementEnglishSerializer
    lookup_field = 'id'


class AchievementEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementEnglish.objects.all()
    serializer_class = AchievementEnglishSerializer
    lookup_field = 'id'


# * =================== Achievement Arabic Dashboard ===================


class AchievementArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementArabic.objects.all()
    serializer_class = AchievementArabicSerializer


class AchievementArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementArabic.objects.all()
    serializer_class = AchievementArabicSerializer


class AchievementArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementArabic.objects.all()
    serializer_class = AchievementArabicSerializer
    lookup_field = 'id'


class AchievementArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementArabic.objects.all()
    serializer_class = AchievementArabicSerializer
    lookup_field = 'id'


class AchievementArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AchievementArabic.objects.all()
    serializer_class = AchievementArabicSerializer
    lookup_field = 'id'


# * =================== Team English Dashboard ===================


class TeamEnglishListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamEnglish.objects.all()
    serializer_class = TeamEnglishSerializer


class TeamEnglishCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamEnglish.objects.all()
    serializer_class = TeamEnglishSerializer


class TeamEnglishDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamEnglish.objects.all()
    serializer_class = TeamEnglishSerializer
    lookup_field = 'id'


class TeamEnglishUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamEnglish.objects.all()
    serializer_class = TeamEnglishSerializer
    lookup_field = 'id'


class TeamEnglishDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamEnglish.objects.all()
    serializer_class = TeamEnglishSerializer
    lookup_field = 'id'


# * =================== Team Arabic Dashboard ===================


class TeamArabicListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamArabic.objects.all()
    serializer_class = TeamArabicSerializer


class TeamArabicCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamArabic.objects.all()
    serializer_class = TeamArabicSerializer


class TeamArabicDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamArabic.objects.all()
    serializer_class = TeamArabicSerializer
    lookup_field = 'id'


class TeamArabicUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamArabic.objects.all()
    serializer_class = TeamArabicSerializer
    lookup_field = 'id'


class TeamArabicDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeamArabic.objects.all()
    serializer_class = TeamArabicSerializer
    lookup_field = 'id'
